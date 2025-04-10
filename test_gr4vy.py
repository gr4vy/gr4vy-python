import base64
import json
import logging

from gr4vy import Gr4vyClient, Gr4vyClientWithBaseUrl
from gr4vy.gr4vy_client import Gr4vyError

gr4vy_id = "spider"
private_key_location = "./private_key.pem"
environment = "sandbox"
client = Gr4vyClient(
    gr4vy_id,
    private_key_location,
    environment=environment,
    merchant_account_id="default",
)
# client.configuration.debug = True


def test_create_client():
    assert client


def test_gr4vy_client_with_baseUrl():
    assert Gr4vyClientWithBaseUrl(
        "https://{}.gr4vy.app".format(gr4vy_id),
        "private_key.pem",
        environment=environment,
    )


def test_list_audit_logs():
    assert client.list_audit_logs()


def test_list_buyers():
    assert client.list_buyers()


def test_create_new_buyer():
    buyer_request = {"display_name": "Test"}
    buyer_id = client.create_new_buyer(**buyer_request)["id"]
    assert buyer_id


def test_get_buyer():
    buyers = client.list_buyers()["items"]
    if buyers and buyers[0]:
        buyer_id = buyers[0]["id"]
        assert client.get_buyer(buyer_id)


def test_update_buyer():
    for buyer in client.list_buyers()["items"]:
        if buyer["display_name"] == "Test":
            buyer_id = buyer["id"]

    assert client.update_buyer(buyer_id=buyer_id)


def test_list_buyer_payment_methods():
    for buyer in client.list_buyers()["items"]:
        if buyer["display_name"] == "Test":
            buyer_id = buyer["id"]

    assert client.list_buyer_payment_methods(buyer_id=buyer_id)


def test_add_shipping_details():
    for buyer in client.list_buyers()["items"]:
        if buyer["display_name"] == "Test":
            buyer_id = buyer["id"]

    shipping_detail_request = {
        "first_name": "John",
        "last_name": "Lunn",
        "email_address": "john@example.com",
        "phone_number": "+1234567890",
        "address": None,
    }

    assert client.add_buyer_shipping_details(buyer_id, **shipping_detail_request)


def test_get_shipping_details():
    for buyer in client.list_buyers()["items"]:
        if buyer["display_name"] == "Test":
            buyer_id = buyer["id"]
            assert client.get_buyer_shipping_details(buyer_id=buyer_id)


def test_update_buyer_shipping_details():
    for buyer in client.list_buyers()["items"]:
        if buyer["display_name"] == "Test":
            buyer_id = buyer["id"]
            shipping_detail_id = client.get_buyer_shipping_details(buyer_id=buyer_id)[
                "items"
            ][0]["id"]
            shipping_detail_update_request = {"phone_number": "+15555555"}
            assert client.update_buyer_shipping_details(
                buyer_id=buyer_id,
                shipping_detail_id=shipping_detail_id,
                **shipping_detail_update_request,
            )


def test_delete_buyer_shipping_details():
    for buyer in client.list_buyers()["items"]:
        if buyer["display_name"] == "Test":
            buyer_id = buyer["id"]
            shipping_detail_id = client.get_buyer_shipping_details(buyer_id=buyer_id)[
                "items"
            ][0]["id"]
            try:
                client.delete_buyer_shipping_details(
                    buyer_id=buyer_id, shipping_detail_id=shipping_detail_id
                )
            except KeyError:
                logging.debug("No  buyer shipping detail to delete")
                assert False


def test_delete_buyer():
    for buyer in client.list_buyers()["items"]:
        if buyer["display_name"] == "Test":
            buyer_id = buyer["id"]

    try:
        client.delete_buyer(buyer_id=buyer_id)
    except KeyError:
        logging.debug("No buyer's to delete")
        assert False


def test_list_card_scheme_definitons():
    assert client.list_card_scheme_definitions()


def test_add_checkout_sessions():
    assert client.create_new_checkout_session()


def test_get_checkout_session():
    checkout_session_id = client.create_new_checkout_session()["id"]
    assert client.get_checkout_session(checkout_session_id=checkout_session_id)


def test_update_checkout_session():
    checkout_session_id = client.create_new_checkout_session()["id"]
    checkout_session_secure_fields_update = {
        "payment_method": {
            "method": "card",
            "number": "4111111111111111",
            "expiration_date": "11/25",
            "security_code": "123",
        }
    }
    try:
        client.update_checkout_session_fields(
            checkout_session_id=checkout_session_id,
            **checkout_session_secure_fields_update,
        )
    except:
        assert False


def test_delete_checkout_session():
    checkout_session_id = client.create_new_checkout_session()["id"]
    try:
        client.delete_checkout_session(checkout_session_id=checkout_session_id)
    except:
        logging.debug("No checkout session to delete")
        assert False


""" def test_register_digital_wallet():
    digital_wallet_request = {
        "provider":"apple",
        "merchant_name":"Gr4vy",
        "merchant_url":"https://example.com",
        "domain_names":["example.com"],
        "accept_terms_and_conditions": True
    }
    try:
        client.register_digital_wallets(**digital_wallet_request)
    except Gr4vyError as e:
        if e.message == "Request conflicts with existing record":
            assert True
        else:
            assert False """


def test_list_digital_wallets():
    assert client.list_digital_wallets()


""" def test_update_digital_wallets():
    digital_wallet_id = client.list_digital_wallets()["items"][0].get("id")
    digital_wallet_update = {
        "merchant_name": "Gr4vy",
        "domain_names": ["example.com"],
    }
    assert client.update_digital_wallet(
        digital_wallet_id=digital_wallet_id, **digital_wallet_update
    ) """


def test_get_digital_wallet():
    digital_wallet_id = client.list_digital_wallets()["items"][0].get("id")
    assert client.get_digital_wallet(digital_wallet_id=digital_wallet_id)


def tes_deregister_digital_wallets():
    digital_wallet_id = client.list_digital_wallets()["items"][0].get("id")
    assert client.deregister_digital_wallet(digital_wallet_id=digital_wallet_id)


def test_list_payment_methods():
    assert client.list_payment_methods()


def test_store_payment_method():
    payment_method_request = {
        "method": "card",
        "number": "4111111111111111",
        "expiration_date": "11/25",
        "security_code": "123",
    }
    assert client.store_payment_method(**payment_method_request)


def test_get_stored_payment_method():
    payment_method_id = client.list_payment_methods()["items"][0]["id"]
    assert client.get_stored_payment_method(payment_method_id)


""" def test_list_payment_method_tokens():
    payment_method_request = {
        "method":"card",
        "number":"4111111111111111",
        "expiration_date":"11/25",
        "security_code":"123",
    }
    payment_method = client.store_payment_method(**payment_method_request)
    payment_method_id = payment_method.get('id')
    assert client.list_payment_method_tokens(payment_method_id)
 """


def test_delete_payment_method():
    payment_method_id = client.list_payment_methods()["items"][0]["id"]
    assert client.delete_payment_method(payment_method_id) == None


def test_list_payment_options():
    assert client.list_payment_options()


def test_post_list_payment_options():
    payment_options_request = {
        "currency": "USD",
        "country": "US",
        "amount": 1000,
        "metadata": {"TypeOfPayment": "purchase", "Carbon_FootPrint": "10"},
    }
    assert client.post_list_payment_options(**payment_options_request)


def test_get_payment_service_definitions():
    payment_service_definitions = client.list_payment_service_definitions(limit=1)
    assert client.get_payment_service_definition(
        payment_service_definitions["items"][0]["id"]
    )


def test_list_payment_service_defintions():
    assert client.list_payment_service_definitions()


def test_list_payment_services():
    assert client.list_payment_services()


def test_create_new_payment_service():
    api_key = {"key": "api_key", "value": "12345678"}
    merchant_account = {"key": "merchant_account", "value": "12345678"}
    live_endpoint_prefix = {"key": "live_endpoint_prefix", "value": "phillip"}
    payment_service_definition_id = "adyen-card"
    payment_service_request = {
        "display_name": "TestAddService",
        "fields": [api_key, merchant_account, live_endpoint_prefix],
        "accepted_countries": ["US"],
        "accepted_currencies": ["USD"],
        "payment_service_definition_id": payment_service_definition_id,
        "three_d_secure_enabled": False,
    }
    payment_service_id = client.create_new_payment_service(**payment_service_request)[
        "id"
    ]
    assert payment_service_id


def test_get_payment_service():
    payment_services = client.list_payment_services()["items"]
    if client.list_payment_services()["items"][0]:
        assert client.get_payment_service(payment_services[0].get("id"))


def test_update_payment_service():
    for payment_service in client.list_payment_services(limit=100)["items"]:
        if payment_service["display_name"] == "TestAddService":
            payment_service_id = payment_service["id"]

            api_key = {"key": "api_key", "value": "12345678"}
            merchant_account = {"key": "merchant_account", "value": "12345678"}
            live_endpoint_prefix = {"key": "live_endpoint_prefix", "value": "testing"}

            payment_service_update = {
                "display_name": "TestAddService",
                "fields": [api_key, merchant_account, live_endpoint_prefix],
                "accepted_countries": ["US"],
                "accepted_currencies": ["USD"],
                "three_d_secure_enabled": False,
            }

            assert client.update_payment_service(
                payment_service_id=payment_service_id,
                **payment_service_update,
            )


def test_delete_payment_service():
    for payment_service in client.list_payment_services(limit=100)["items"]:
        if payment_service["display_name"] == "TestAddService":
            payment_service_id = payment_service["id"]
            try:
                client.delete_payment_service(payment_service_id)
            except:
                assert False


def test_list_all_report_executions():
    assert client.list_all_report_executions()


def test_get_reportExections():
    report_execution_id = client.list_all_report_executions()["items"][0].get(
        "id", None
    )
    assert client.get_report_executions(report_execution_id=report_execution_id)


def test_create_new_report():
    report_create = {
        "name": "Failed Authorizations 042022",
        "description": "Transactions that failed to authorize in April 2022",
        "schedule": "monthly",
        "schedule_enabled": True,
        "schedule_timezone": "Europe/London",
        "spec": {
            "model": "transactions",
            "params": {
                "sort": [{"field": "captured_at", "order": "desc"}],
                "fields": [
                    "id",
                    "external_identifier",
                    "status",
                    "created_at",
                    "authorized_at",
                    "captured_at",
                    "voided_at",
                    "amount",
                    "currency",
                    "captured_amount",
                    "refunded_amount",
                    "method",
                    "scheme",
                    "payment_service_transaction_id",
                    "payment_service_id",
                    "payment_service_definition_id",
                    "payment_service_display_name",
                    "raw_response_code",
                    "raw_response_description",
                    "metadata",
                    "three_d_secure_status",
                    "three_d_secure_eci",
                    "three_d_secure_auth_resp",
                    "three_d_secure_method",
                ],
                "filters": {
                    "method": None,
                    "scheme": None,
                    "status": ["capture_succeeded"],
                    "currency": None,
                    "metadata": None,
                    "voided_at": None,
                    "created_at": None,
                    "captured_at": {
                        "end": "2023-03-02T22:59:59+00:00",
                        "start": "2023-02-28T23:00:00+00:00",
                    },
                    "authorized_at": None,
                    "three_d_secure_eci": None,
                    "three_d_secure_status": None,
                    "three_d_secure_auth_resp": None,
                },
            },
        },
    }
    assert client.create_new_report(**report_create)


def test_list_reports():
    assert client.list_reports()


def test_get_report():
    report_id = client.list_reports()["items"][0].get("id", None)
    assert client.get_report(report_id=report_id)


def test_update_report():
    for report in client.list_reports()["items"]:
        if report.get("name") == "Failed Authorizations 042022":
            report_id = report.get("id")
            report_update = {
                "name": "Failed Authorizations 0420221",
                "description": "Transactions that failed to authorize in April 2022",
                "schedule_enabled": True,
            }
            assert client.update_report(report_id=report_id, **report_update)


def test_list_transactions():
    assert client.list_transactions()


# def test_list_role_assignments():
#    assert client.list_role_assignments(assignee_type='user')


def test_list_roles():
    assert client.list_roles()


def test_create_new_transaction():
    transaction_request = {
        "amount": 1299,
        "currency": "USD",
        "intent": "authorize",
        "payment_method": {
            "method": "card",
            "number": "4111111111111111",
            "expiration_date": "11/25",
            "security_code": "123",
            "redirect_url": "https://example.com/callback",
        },
    }
    transaction = client.create_new_transaction(**transaction_request)

    assert transaction["status"] in [
        "authorization_succeeded",
        "buyer_approval_pending",
    ]


def test_capture_transaction():
    transaction_request = {
        "amount": 1299,
        "currency": "USD",
        "intent": "authorize",
        "payment_method": {
            "method": "card",
            "number": "4111111111111111",
            "expiration_date": "11/25",
            "security_code": "123",
            "redirect_url": "https://example.com/callback",
        },
    }

    transaction = client.create_new_transaction(**transaction_request)

    if transaction["status"] == "authorization_succeeded":
        transaction_id = transaction["id"]
        transaction_capture_request = {"amount": 1299}
        capture = client.capture_transaction(
            transaction_id=transaction_id, **transaction_capture_request
        )
        assert capture["status"] == "capture_succeeded"


def test_list_transactions():
    assert client.list_transactions()


def test_get_transaction():
    transaction_id = client.list_transactions()["items"][0]["id"]
    assert client.get_transaction(transaction_id)


def test_refund_transaction():
    transaction_request = {
        "amount": 1299,
        "currency": "USD",
        "intent": "authorize",
        "payment_method": {
            "method": "card",
            "number": "4111111111111111",
            "expiration_date": "11/25",
            "security_code": "123",
            "redirect_url": "https://example.com/callback",
        },
    }
    transaction = client.create_new_transaction(**transaction_request)

    logging.debug("===")
    logging.debug(transaction)
    logging.debug("===")
    if transaction["status"] == "authorization_succeeded":

        transaction_capture_request = {"amount": 1299}
        capture = client.capture_transaction(
            transaction.get("id"), **transaction_capture_request
        )

        logging.debug(capture)
        if capture["status"] == "capture_succeeded":
            transaction_refund_request = {"amount": 1299}

            refund = client.refund_transaction(
                transaction["id"], **transaction_refund_request
            )

            logging.debug(refund)
            assert refund["status"] in ["succeeded", "processing"]


def test_void_transaction():
    transaction_request = {
        "amount": 1299,
        "currency": "USD",
        "intent": "authorize",
        "payment_method": {
            "method": "card",
            "number": "4111111111111111",
            "expiration_date": "11/25",
            "security_code": "123",
            "redirect_url": "https://example.com/callback",
        },
    }
    transaction = client.create_new_transaction(**transaction_request)

    logging.debug("===")
    logging.debug(transaction)
    logging.debug("===")
    if transaction["status"] == "authorization_succeeded":

        void = client.void_transaction(transaction.get("id"))

        logging.debug(void)
        assert void["status"] == "authorization_voided"


def test_generate_embed_token():
    embed_data = {
        "amount": 1299,
        "currency": "USD",
    }
    jwt_token = client.generate_embed_token(embed_data=embed_data)

    # Extract the payload part of the token
    payload_b64 = jwt_token.split(".")[1]

    # Add padding to the base64-encoded payload
    padding = "=" * (len(payload_b64) % 4)
    padded_payload_b64 = payload_b64 + padding

    # Decode the base64-encoded payload
    decoded_payload = base64.b64decode(padded_payload_b64).decode("utf-8")

    # Convert the decoded payload to a dictionary
    decoded_dict = json.loads(decoded_payload)

    assert decoded_dict["embed"]["amount"] == 1299
    assert decoded_dict["embed"]["currency"] == "USD"


def test_generate_embed_token_with_checkout_session():
    checkout_session_id = client.create_new_checkout_session().get("id")
    embed_data = {
        "amount": 1234,
        "currency": "SEK",
    }
    jwt_token = client.generate_embed_token(
        embed_data=embed_data, checkout_session_id=checkout_session_id
    )
    assert jwt_token

    # Extract the payload part of the token
    payload_b64 = jwt_token.split(".")[1]

    # Add padding to the base64-encoded payload
    padding = "=" * (len(payload_b64) % 4)
    padded_payload_b64 = payload_b64 + padding

    # Decode the base64-encoded payload
    decoded_payload = base64.b64decode(padded_payload_b64).decode("utf-8")

    # Convert the decoded payload to a dictionary
    decoded_dict = json.loads(decoded_payload)

    assert decoded_dict["embed"]["amount"] == 1234
    assert decoded_dict["embed"]["currency"] == "SEK"
    assert decoded_dict["checkout_session_id"] == checkout_session_id
