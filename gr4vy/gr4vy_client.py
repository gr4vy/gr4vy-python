import base64
import json
import sys
import textwrap
import uuid
from datetime import datetime, timedelta, timezone
from os import environ

import cryptography.hazmat.primitives.hashes as hashes
import cryptography.hazmat.primitives.serialization as serialization
import jose.jwk
from jwt import api_jwt
from pem import parse_file

from gr4vy.gr4vy_api.openapi_client import ApiClient, ApiException, Configuration
from gr4vy.gr4vy_api.openapi_client.api import (
    api_logs_api,
    audit_logs_api,
    buyers_api,
    card_scheme_definitions_api,
    checkout_sessions_api,
    digital_wallets_api,
    payment_method_tokens_api,
    payment_methods_api,
    payment_options_api,
    payment_service_definitions_api,
    payment_services_api,
    reports_api,
    roles_api,
    transactions_api,
)

VERSION = 0.5
PYTHON_VERSION = "{}.{}.{}".format(
    sys.version_info[0], sys.version_info[1], sys.version_info[2]
)


class Gr4vyClient:
    def __init__(self, gr4vyId, private_key_file, environment):
        self.gr4vyId = gr4vyId
        self.private_key_file = private_key_file
        self.environment = environment
        self.GenerateToken()
        self.CreateConfiguration()
        self.CreateClient()

    def private_key_file_to_string(self):
        if environ.get("PRIVATE_KEY") is not None:
            private_key_string = environ.get("PRIVATE_KEY")
        else:
            private_key_string = str(parse_file(self.private_key_file)[0])
        private_key_pem = textwrap.dedent(private_key_string).encode()

        private_pem = serialization.load_pem_private_key(private_key_pem, password=None)

        jwk = jose.jwk.construct(private_pem, algorithm="ES512").to_dict()

        kid = str(self.thumbprint(jwk))
        return private_key_string, kid

    def GenerateToken(self, scopes=["*.read", "*.write"], embed_data=None):
        private_key, kid = self.private_key_file_to_string()
        data = {
            "iss": "Gr4vy SDK {} - {}".format(VERSION, PYTHON_VERSION),
            "nbf": datetime.now(tz=timezone.utc),
            "exp": datetime.now(tz=timezone.utc) + timedelta(hours=4800),
            "jti": str(uuid.uuid4()),
            "scopes": scopes,
        }
        if embed_data:
            data["embed"] = embed_data
            data["scopes"] = ["embed.read", "embed.write"]
        self.token = api_jwt.encode(
            data, private_key, algorithm="ES512", headers={"kid": kid}
        )
        return self.token

    def GenerateEmbedToken(self, embed_data):
        self.GenerateToken(embed_data=embed_data)
        return self.token

    def CreateConfiguration(self):
        if self.gr4vyId.endswith(".app"):
            host = self.gr4vyId
        else:
            if self.environment != "production":
                host = "https://api.{}.{}.gr4vy.app".format(
                    self.environment, self.gr4vyId
                )
            else:
                host = "https://api.{}.gr4vy.app".format(self.gr4vyId)
        self.configuration = Configuration(access_token=self.token, host=host)

    def CreateClient(self):
        self.client = ApiClient(self.configuration)

    def ListAuditLogs(self, **kwargs):
        with self.client as api_client:
            try:
                # Get buyer
                client = audit_logs_api.AuditLogsApi(api_client)
                api_response = client.list_audit_logs(**kwargs)
                return api_response
            except ApiException as e:
                print("Exception when calling AuditLogsApi->list_audit_logs: %s\n" % e)

    def ListBuyers(self, **kwargs):
        with self.client as api_client:
            try:
                # Get buyer
                client = buyers_api.BuyersApi(api_client)
                api_response = client.list_buyers(**kwargs)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->list_buyer: %s\n" % e)

    def GetBuyer(self, buyer_id):
        with self.client as api_client:
            try:
                # Get buyer
                client = buyers_api.BuyersApi(api_client)
                api_response = client.get_buyer(buyer_id)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->get_buyer: %s\n" % e)

    def AddBuyer(self, buyer_request):
        with self.client as api_client:
            try:
                # Get buyer
                client = buyers_api.BuyersApi(api_client)
                api_response = client.add_buyer(buyer_request=buyer_request)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->add_buyer: %s\n" % e)

    def UpdateBuyer(self, buyer_id, buyer_update):
        with self.client as api_client:
            try:
                # Get buyer
                client = buyers_api.BuyersApi(api_client)
                api_response = client.update_buyer(
                    buyer_id=buyer_id, buyer_update=buyer_update
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->update_buyer: %s\n" % e)

    def DeleteBuyer(self, buyer_id):
        with self.client as api_client:
            try:
                # Get buyer
                client = buyers_api.BuyersApi(api_client)
                api_response = client.delete_buyer(buyer_id=buyer_id)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def GetBuyerShippingDetails(self, buyer_id):
        with self.client as api_client:
            try:
                # Get buyer
                client = buyers_api.BuyersApi(api_client)
                api_response = client.get_buyer_shipping_details(buyer_id=buyer_id)
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling BuyersApi->get_buyer_shipping_details: %s\n"
                    % e
                )

    def AddBuyerShippingDetails(self, buyer_id, shipping_detail_request=None):
        with self.client as api_client:
            try:
                # Get buyer
                client = buyers_api.BuyersApi(api_client)
                api_response = client.add_buyer_shipping_detail(
                    buyer_id=buyer_id, shipping_detail_request=shipping_detail_request
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling BuyersApi->get_buyer_shipping_details: %s\n"
                    % e
                )

    def UpdateBuyerShippingDetails(
        self, buyer_id, shipping_detail_id, shipping_detail_update_request=None
    ):
        with self.client as api_client:
            try:
                # Get buyer
                client = buyers_api.BuyersApi(api_client)
                api_response = client.update_buyer_shipping_detail(
                    buyer_id=buyer_id,
                    shipping_detail_id=shipping_detail_id,
                    shipping_detail_update_request=shipping_detail_update_request,
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling BuyersApi->get_buyer_shipping_details: %s\n"
                    % e
                )

    def DeleteBuyerShippingDetails(self, buyer_id, shipping_detail_id):
        with self.client as api_client:
            try:
                # Get buyer
                client = buyers_api.BuyersApi(api_client)
                api_response = client.delete_buyer_shipping_detail(
                    buyer_id=buyer_id, shipping_detail_id=shipping_detail_id
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling BuyersApi->get_buyer_shipping_details: %s\n"
                    % e
                )

    def ListCardSchemeDefintions(self, **kwargs):
        with self.client as api_client:
            try:
                # Get buyer
                client = card_scheme_definitions_api.CardSchemeDefinitionsApi(
                    api_client
                )
                api_response = client.list_card_scheme_definitions(**kwargs)
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling BuyersApi->get_buyer_shipping_details: %s\n"
                    % e
                )

    def GetCheckoutSession(self, checkout_session_id):
        with self.client as api_client:
            try:
                # Get buyer
                client = checkout_sessions_api.CheckoutSessionsApi(api_client)
                api_response = client.get_checkout_session(
                    checkout_session_id=checkout_session_id
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->get_buyer: %s\n" % e)

    def AddCheckoutSession(self, **kwargs):
        with self.client as api_client:
            try:
                # Get buyer
                client = checkout_sessions_api.CheckoutSessionsApi(api_client)
                api_response = client.add_checkout_session(**kwargs)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->add_buyer: %s\n" % e)

    def UpdateCheckoutSessionFields(
        self, checkout_session_id, checkout_session_secure_fields_update=None
    ):
        with self.client as api_client:
            try:
                # Get buyer
                client = checkout_sessions_api.CheckoutSessionsApi(api_client)
                api_response = client.update_checkout_session_fields(
                    checkout_session_id=checkout_session_id,
                    checkout_session_secure_fields_update=checkout_session_secure_fields_update,
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->update_buyer: %s\n" % e)

    def DeleteCheckoutSession(self, checkout_session_id):
        with self.client as api_client:
            try:
                # Get buyer
                client = checkout_sessions_api.CheckoutSessionsApi(api_client)
                api_response = client.delete_checkout_session(
                    checkout_session_id=checkout_session_id
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def RegisterDigitalWallets(self, digital_wallet_request):
        with self.client as api_client:
            try:
                # Get buyer
                client = digital_wallets_api.DigitalWalletsApi(api_client)
                api_response = client.register_digital_wallet(
                    digital_wallet_request=digital_wallet_request
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def ListDigitalWallets(self, **kwargs):
        with self.client as api_client:
            try:
                # Get buyer
                client = digital_wallets_api.DigitalWalletsApi(api_client)
                api_response = client.list_digital_wallets(**kwargs)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def GetDigitalWallet(self, digital_wallet_id):
        with self.client as api_client:
            try:
                # Get buyer
                client = digital_wallets_api.DigitalWalletsApi(api_client)
                api_response = client.get_digital_wallet(
                    digital_wallet_id=digital_wallet_id
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def UpdateDigitalWallet(self, digital_wallet_id, digital_wallet_update=None):
        with self.client as api_client:
            try:
                # Get buyer
                client = digital_wallets_api.DigitalWalletsApi(api_client)
                api_response = client.update_digital_wallet(
                    digital_wallet_id=digital_wallet_id,
                    digital_wallet_update=digital_wallet_update,
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def DeregisterDigitalWallets(self, digital_wallet_id):
        with self.client as api_client:
            try:
                # Get buyer
                client = digital_wallets_api.DigitalWalletsApi(api_client)
                api_response = client.deregister_digital_wallet(
                    digital_wallet_id=digital_wallet_id
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def GetPaymentMethod(self, payment_method_id):
        with self.client as api_client:
            try:
                # Get buyer
                client = payment_methods_api.PaymentMethodsApi(api_client)
                api_response = client.get_payment_method(
                    payment_method_id=payment_method_id
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentMethodsApi->get_payment_method: %s\n"
                    % e
                )

    def ListBuyerPaymentMethods(self, buyer_id, **kwargs):
        with self.client as api_client:
            try:
                # Get buyer
                client = payment_methods_api.PaymentMethodsApi(api_client)
                api_response = client.list_buyer_payment_methods(
                    buyer_id=buyer_id, **kwargs
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentMethodsApi->get_payment_method: %s\n"
                    % e
                )

    def ListPaymentMethods(self, **kwargs):
        with self.client as api_client:
            try:
                client = payment_methods_api.PaymentMethodsApi(api_client)
                api_response = client.list_payment_methods(**kwargs)
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentMethodsApi->list_payment_methods: %s\n"
                    % e
                )

    def StorePaymentMethod(self, payment_method_request):
        with self.client as api_client:
            try:
                client = payment_methods_api.PaymentMethodsApi(api_client)
                api_response = client.store_payment_method(
                    payment_method_request=payment_method_request
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentMethodsApi->store_payment_method: %s\n"
                    % e
                )

    def DeletePaymentMethod(self, payment_method_id):
        with self.client as api_client:
            try:
                client = payment_methods_api.PaymentMethodsApi(api_client)
                api_response = client.delete_payment_method(
                    payment_method_id=payment_method_id
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentMethodsApi->delete_payment_method: %s\n"
                    % e
                )

    def ListPaymentMethodTokens(self, payment_method_id):
        with self.client as api_client:
            try:
                client = payment_method_tokens_api.PaymentMethodTokensApi(api_client)
                api_response = client.list_payment_method_tokens(
                    payment_method_id=payment_method_id
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentMethodTokensApi->list_payment_method_tokens: %s\n"
                    % e
                )

    def ListPaymentOptions(self, **kwargs):
        with self.client as api_client:
            try:
                client = payment_options_api.PaymentOptionsApi(api_client)
                api_response = client.list_payment_options(**kwargs)
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentOptionsApi->list_payment_options: %s\n"
                    % e
                )

    def GetPaymentServiceDefinition(self, payment_service_definition_id):
        with self.client as api_client:
            try:
                client = payment_service_definitions_api.PaymentServiceDefinitionsApi(
                    api_client
                )
                api_response = client.get_payment_service_definition(
                    payment_service_definition_id=payment_service_definition_id
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentServiceDefinitionsApi->get_payment_service_definition: %s\n"
                    % e
                )

    def ListPaymentServiceDefintions(self, **kwargs):
        with self.client as api_client:
            try:
                client = payment_service_definitions_api.PaymentServiceDefinitionsApi(
                    api_client
                )
                api_response = client.list_payment_service_definitions(**kwargs)
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentServiceDefinitionsApi->get_payment_service_definition: %s\n"
                    % e
                )

    def ListPaymentServices(self, **kwargs):
        with self.client as api_client:
            try:
                client = payment_services_api.PaymentServicesApi(api_client)
                api_response = client.list_payment_services(**kwargs)
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentServicesApi->list_payment_services: %s\n"
                    % e
                )

    def AddPaymentService(self, payment_service_request):
        with self.client as api_client:
            try:
                client = payment_services_api.PaymentServicesApi(api_client)
                api_response = client.add_payment_service(
                    payment_service_request=payment_service_request
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentServicesApi->add_payment_service: %s\n"
                    % e
                )

    def DeletePaymentService(self, payment_service_id):
        with self.client as api_client:
            try:
                client = payment_services_api.PaymentServicesApi(api_client)
                api_response = client.delete_payment_service(
                    payment_service_id=payment_service_id
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentServicesApi->delete_payment_service: %s\n"
                    % e
                )

    def GetPaymentService(self, payment_service_id):
        with self.client as api_client:
            try:
                client = payment_services_api.PaymentServicesApi(api_client)
                api_response = client.get_payment_service(
                    payment_service_id=payment_service_id
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentServicesApi->get_payment_service: %s\n"
                    % e
                )

    def UpdatePaymentService(self, payment_service_id, payment_service_update):
        with self.client as api_client:
            try:
                client = payment_services_api.PaymentServicesApi(api_client)
                api_response = client.update_payment_service(
                    payment_service_id=payment_service_id,
                    payment_service_update=payment_service_update,
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling PaymentServicesApi->update_payment_service: %s\n"
                    % e
                )

    def ListAllReportExecutions(self, **kwargs):
        with self.client as api_client:
            try:
                # Get buyer
                client = reports_api.ReportsApi(api_client)
                api_response = client.list_all_report_executions(**kwargs)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def GetReportExecutions(self, report_execution_id):
        with self.client as api_client:
            try:
                # Get buyer
                client = reports_api.ReportsApi(api_client)
                api_response = client.get_report_execution(
                    report_execution_id=report_execution_id
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def AddReport(self, report_create):
        with self.client as api_client:
            try:
                # Get buyer
                client = reports_api.ReportsApi(api_client)
                api_response = client.add_report(report_create=report_create)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def ListReports(self, **kwargs):
        with self.client as api_client:
            try:
                # Get buyer
                client = reports_api.ReportsApi(api_client)
                api_response = client.list_reports(**kwargs)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def GetReport(self, report_id):
        with self.client as api_client:
            try:
                # Get buyer
                client = reports_api.ReportsApi(api_client)
                api_response = client.get_report(report_id=report_id)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def UpdateReport(self, report_id, report_update=None):
        with self.client as api_client:
            try:
                # Get buyer
                client = reports_api.ReportsApi(api_client)
                api_response = client.update_report(
                    report_id=report_id, report_update=report_update
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def ListExecutionsForAReport(self, report_id, **kwargs):
        with self.client as api_client:
            try:
                # Get buyer
                client = reports_api.ReportsApi(api_client)
                api_response = client.list_report_executions(
                    report_id=report_id, **kwargs
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def GenerateDownloadUrlForReportExecution(self, report_id, report_execution_id):
        with self.client as api_client:
            try:
                # Get buyer
                client = reports_api.ReportsApi(api_client)
                api_response = client.generate_download_url(
                    report_id=report_id, report_execution_id=report_execution_id
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def AuthorizeNewTransaction(self, transaction_request):
        with self.client as api_client:
            try:
                client = transactions_api.TransactionsApi(api_client)
                api_response = client.authorize_new_transaction(
                    transaction_request=transaction_request
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling TransactionsApi->authorize_new_transaction: %s\n"
                    % e
                )

    def CaptureTransaction(self, transaction_id, transaction_capture_request):
        with self.client as api_client:
            try:
                client = transactions_api.TransactionsApi(api_client)
                api_response = client.capture_transaction(
                    transaction_id=transaction_id,
                    transaction_capture_request=transaction_capture_request,
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling TransactionsApi->capture_transaction: %s\n"
                    % e
                )

    def GetTransaction(self, transaction_id):
        with self.client as api_client:
            try:
                client = transactions_api.TransactionsApi(api_client)
                api_response = client.get_transaction(transaction_id=transaction_id)
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling TransactionsApi->capture_transaction: %s\n"
                    % e
                )

    def ListTransactions(self, **kwargs):
        with self.client as api_client:
            try:
                client = transactions_api.TransactionsApi(api_client)
                api_response = client.list_transactions(**kwargs)
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling TransactionsApi->capture_transaction: %s\n"
                    % e
                )

    def RefundTransaction(self, transaction_id, transaction_refund_request=None):
        with self.client as api_client:
            try:
                client = transactions_api.TransactionsApi(api_client)
                api_response = client.refund_transaction(
                    transaction_id=transaction_id,
                    transaction_refund_request=transaction_refund_request,
                )
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling TransactionsApi->capture_transaction: %s\n"
                    % e
                )

    def VoidTransaction(self, transaction_id):
        with self.client as api_client:
            try:
                client = transactions_api.TransactionsApi(api_client)
                api_response = client.void_transaction(transaction_id=transaction_id)
                return api_response
            except ApiException as e:
                print(
                    "Exception when calling TransactionsApi->capture_transaction: %s\n"
                    % e
                )

    def AddReport(self, report_create):
        with self.client as api_client:
            try:
                # Get buyer
                client = reports_api.ReportsApi(api_client)
                api_response = client.add_report(report_create=report_create)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def ListRoles(self, **kwargs):
        with self.client as api_client:
            try:
                # Get buyer
                client = roles_api.RolesApi(api_client)
                api_response = client.list_roles(**kwargs)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def ListRolesAssignments(self, **kwargs):
        with self.client as api_client:
            try:
                # Get buyer
                client = roles_api.RolesApi(api_client)
                api_response = client.list_role_assignments(**kwargs)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def AddRoleAssignment(self, role_assignment_request):
        with self.client as api_client:
            try:
                # Get buyer
                client = roles_api.RolesApi(api_client)
                api_response = client.add_role_assignment(
                    role_assignment_request=role_assignment_request
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def DeleteRoleAssignment(self, role_assignment_id):
        with self.client as api_client:
            try:
                # Get buyer
                client = roles_api.RolesApi(api_client)
                api_response = client.delete_role_assignment(
                    role_assignment_id=role_assignment_id
                )
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def ListApiErrorLogs(self, **kwargs):
        with self.client as api_client:
            try:
                # Get buyer
                client = api_logs_api.APILogsApi(api_client)
                api_response = client.list_api_logs(**kwargs)
                return api_response
            except ApiException as e:
                print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)

    def b64e(self, value: bytes) -> str:
        return base64.urlsafe_b64encode(value).decode("utf8").strip("=")

    def thumbprint(self, jwk: dict) -> str:
        claims = {k: v for k, v in jwk.items() if k in {"kty", "crv", "x", "y"}}
        json_claims = json.dumps(claims, separators=(",", ":"), sort_keys=True)
        digest = hashes.Hash(hashes.SHA256())
        digest.update(json_claims.encode("utf8"))
        return self.b64e(digest.finalize())


class Gr4vyClientWithBaseUrl(Gr4vyClient):
    def __init__(self, base_url, private_key, environment):
        super().__init__(base_url, private_key, environment)
