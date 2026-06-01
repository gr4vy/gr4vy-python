"""Payment links: create -> get -> list -> expire (a full happy-path lifecycle)."""

from utils import fixtures


def test_create_get_list_expire(merchant):
    sdk = merchant.client
    ext = fixtures.unique_id("link", merchant.merchant_account_id)

    link = sdk.payment_links.create(
        amount=1299, country="US", currency="USD", external_identifier=ext
    )
    assert link.id is not None

    fetched = sdk.payment_links.get(payment_link_id=link.id)
    assert fetched.id == link.id

    listed = sdk.payment_links.list()
    assert listed is not None

    # expire() may return no body; confirm the call succeeds and the link is
    # still retrievable afterwards.
    sdk.payment_links.expire(payment_link_id=link.id)
    after_expire = sdk.payment_links.get(payment_link_id=link.id)
    assert after_expire.id == link.id
