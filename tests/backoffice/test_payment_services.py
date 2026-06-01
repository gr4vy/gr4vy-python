"""Payment services: create/get/update(partial)/list/delete + verify + session,
plus the definitions, payment-options and card-scheme-definitions read
sub-resources."""

from utils import reach


def _new_service(sdk):
    return sdk.payment_services.create(
        display_name="Secondary service",
        payment_service_definition_id="mock-card",
        fields=[{"key": "merchant_id", "value": "test"}],
        accepted_currencies=["USD"],
        accepted_countries=["US"],
        active=True,
    )


def test_crud_with_partial_update(merchant):
    sdk = merchant.client

    created = _new_service(sdk)
    assert created.id is not None
    assert created.display_name == "Secondary service"

    fetched = sdk.payment_services.get(payment_service_id=created.id)
    assert fetched.id == created.id

    # Partial update: change only display_name.
    updated = sdk.payment_services.update(
        payment_service_id=created.id, display_name="Renamed service"
    )
    assert updated.display_name == "Renamed service"
    # Accepted currencies (untouched) are preserved.
    assert updated.accepted_currencies == ["USD"]

    listed = sdk.payment_services.list()
    assert listed is not None

    sdk.payment_services.delete(payment_service_id=created.id)


def test_verify_and_session_are_reached(merchant):
    sdk = merchant.client
    created = _new_service(sdk)

    reach.reaches(
        lambda: sdk.payment_services.verify(
            payment_service_definition_id="mock-card",
            fields=[{"key": "merchant_id", "value": "test"}],
        ),
        "payment_services.verify",
    )
    reach.reaches(
        lambda: sdk.payment_services.session(
            payment_service_id=created.id, request_body={}
        ),
        "payment_services.session",
    )


def test_read_sidecars(merchant):
    sdk = merchant.client

    # Definitions: list + get + session (reached).
    definitions = sdk.payment_service_definitions.list()
    assert definitions is not None

    mock_card = sdk.payment_service_definitions.get(payment_service_definition_id="mock-card")
    assert mock_card is not None

    reach.reaches(
        lambda: sdk.payment_service_definitions.session(
            payment_service_definition_id="mock-card", request_body={}
        ),
        "payment_service_definitions.session",
    )

    # Payment options + card-scheme definitions: happy paths.
    options = sdk.payment_options.list(country="US", currency="USD", amount=1299)
    assert options is not None

    schemes = sdk.card_scheme_definitions.list()
    assert schemes is not None
