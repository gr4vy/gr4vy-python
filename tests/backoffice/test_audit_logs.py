"""Audit logs: list (happy path)."""


def test_list_is_happy_path(merchant):
    sdk = merchant.client
    # The merchant has activity from setup, so this typically returns entries.
    listed = sdk.audit_logs.list()
    assert listed is not None
