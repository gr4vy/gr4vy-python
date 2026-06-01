"""Reporting endpoints. The list/get/put/executions endpoints are reached without
depending on a successful create (they accept missing-id 4xx). `POST /reports`
is a real happy path: unlike the PHP SDK (whose UnionHandler could not serialise
the `spec` union), pydantic serialises the discriminated `spec` cleanly, so the
create reaches a 2xx with a `transactions` report spec."""

from utils import MISSING_ID, fixtures, reach


def test_list_endpoints(merchant):
    sdk = merchant.client
    # GET /reports and GET /report-executions.
    assert sdk.reports.list() is not None
    assert sdk.report_executions.list() is not None


def test_get_and_put_are_reached(merchant):
    sdk = merchant.client
    reach.reaches(lambda: sdk.reports.get(report_id=MISSING_ID), "reports.get")
    reach.reaches(
        lambda: sdk.reports.put(report_id=MISSING_ID, name="Renamed"),
        "reports.put",
    )


def test_executions_endpoints(merchant):
    sdk = merchant.client
    reach.reaches(
        lambda: sdk.reports.executions.list(report_id=MISSING_ID),
        "reports.executions.list",
    )
    reach.reaches(
        lambda: sdk.reports.executions.get(report_execution_id=MISSING_ID),
        "reports.executions.get",
    )
    reach.reaches(
        lambda: sdk.reports.executions.url(
            report_id=MISSING_ID, report_execution_id=MISSING_ID
        ),
        "reports.executions.url",
    )


def test_create_is_happy_path(merchant):
    sdk = merchant.client
    report = sdk.reports.create(
        name=fixtures.unique_id("report", merchant.merchant_account_id),
        schedule="daily",
        schedule_enabled=False,
        spec={
            "model": "transactions",
            "params": {
                "fields": ["id", "status"],
                "filters": {"status": ["capture_succeeded"]},
                "sort": [{"field": "created_at", "order": "desc"}],
            },
        },
    )
    assert report.id is not None
