"""
    Gr4vy API

    Welcome to the Gr4vy API reference documentation. Our API is still very much a work in product and subject to change.  # noqa: E501

    The version of the OpenAPI document: 1.1.0-beta
    Contact: code@gr4vy.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.three_d_secure_data_v1_v2 import ThreeDSecureDataV1V2
from openapi_client.model.transaction_payment_method_request import TransactionPaymentMethodRequest
globals()['ThreeDSecureDataV1V2'] = ThreeDSecureDataV1V2
globals()['TransactionPaymentMethodRequest'] = TransactionPaymentMethodRequest
from openapi_client.model.transaction_request import TransactionRequest


class TestTransactionRequest(unittest.TestCase):
    """TransactionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionRequest(self):
        """Test TransactionRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransactionRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()