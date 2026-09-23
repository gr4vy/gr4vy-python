"""Roles: list (happy path)."""


def test_list_is_happy_path(merchant):
    sdk = merchant.client
    # Roles are defined per instance, so don't assume any exist — just that every
    # item returned is a well-formed role.
    listed = sdk.roles.list()
    assert listed is not None
    for role in listed.result.items:
        assert role.id
        assert role.slug
