"""Account updater: submitting a job needs the account-updater feature enabled on
the merchant (and an encryption key), which the mock env lacks — so the job
create is reached at the request level."""

from utils import fixtures, reach


def test_jobs_create_is_reached(merchant):
    sdk = merchant.client
    pm = sdk.payment_methods.create(request_body=fixtures.approving_card())

    reach.reaches(
        lambda: sdk.account_updater.jobs.create(payment_method_ids=[pm.id]),
        "account_updater.jobs.create",
    )
