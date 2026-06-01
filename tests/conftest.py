"""Shared pytest fixtures for the E2E suite.

The ``merchant`` fixture provisions ONE isolated merchant account (+ mock-card
service) per test *module* and yields a merchant-scoped client. Per-module
isolation is what makes the suite safe to shard by directory across CI.
"""

import os
import sys

import pytest

# Make the test-only `utils` package importable from every shard directory
# (tests/flows, tests/processing, ...) without depending on pyproject's
# `pythonpath`, which Speakeasy regenerates. This conftest is unmanaged, so the
# path bootstrap survives an SDK regen.
sys.path.insert(0, os.path.dirname(__file__))

# pylint: disable=wrong-import-position
from utils.environment import setup_merchant
from utils.merchant import TestMerchant


@pytest.fixture(scope="module", name="merchant")
def merchant_fixture() -> TestMerchant:
    return setup_merchant()
