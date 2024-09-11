import base64
import collections
import json
import sys
import textwrap
import typing
import urllib
import uuid
from datetime import datetime, timedelta, timezone
from os import environ

import cryptography.hazmat.primitives.hashes as hashes
import cryptography.hazmat.primitives.serialization as serialization
import jose.jwk
import requests
from jwt import api_jwt
from pem import parse_file

VERSION = 0.5
PYTHON_VERSION = "{}.{}.{}".format(
    sys.version_info[0], sys.version_info[1], sys.version_info[2]
)


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


class Gr4vyError(Exception):
    def __init__(self, message, details, http_status_code) -> None:

        super().__init__(
            f"Error Reason: {message} \n Error Details: {details} \n HTTP Status Code: {http_status_code}"
        )

        self.details = details


class Gr4vyClient:
    def __init__(
        self, gr4vyId, private_key_file, environment, merchant_account_id=None
    ):
        self.gr4vyId = gr4vyId
        self.private_key_file = private_key_file
        self.environment = environment
        self.merchant_account_id = (
            merchant_account_id if merchant_account_id else "default"
        )
        self.session = requests.Session()
        self.base_url = self._generate_base_url()
        self.token = self.generate_token()

    def _private_key_file_to_string(self):
        if environ.get("PRIVATE_KEY") is not None:
            private_key_string = environ.get("PRIVATE_KEY")
        else:
            private_key_string = str(parse_file(self.private_key_file)[0])
        private_key_pem = textwrap.dedent(private_key_string).encode()

        private_pem = serialization.load_pem_private_key(private_key_pem, password=None)

        jwk = jose.jwk.construct(private_pem, algorithm="ES512").to_dict()

        kid = str(self._thumbprint(jwk))
        return private_key_string, kid

    def _generate_base_url(self):
        if self.gr4vyId.endswith(".app"):
            base_url = self.gr4vyId
        else:
            if self.environment != "production":
                base_url = "https://api.{}.{}.gr4vy.app".format(
                    self.environment, self.gr4vyId
                )
            else:
                base_url = "https://api.{}.gr4vy.app".format(self.gr4vyId)
        return base_url

    def generate_token(
        self, scopes=["*.read", "*.write"], embed_data=None, checkout_session_id=None
    ):
        private_key, kid = self._private_key_file_to_string()
        data = {
            "iss": "Gr4vy SDK {} - {}".format(VERSION, PYTHON_VERSION),
            "nbf": datetime.now(tz=timezone.utc),
            "exp": datetime.now(tz=timezone.utc) + timedelta(hours=4800),
            "jti": str(uuid.uuid4()),
            "scopes": scopes,
        }
        if embed_data:
            data["embed"] = embed_data
            data["scopes"] = ["embed"]
        if checkout_session_id:
            data["checkout_session_id"] = checkout_session_id
        token = api_jwt.encode(
            data, private_key, algorithm="ES512", headers={"kid": kid}
        )
        return token

    def _prepare_params(self, value: dict[str, typing.Any]) -> dict[str, typing.Any]:
        def _filter_none(value: typing.Any) -> typing.Any:
            if isinstance(value, list):
                return [_filter_none(item) for item in value if item is not None]

            if isinstance(value, dict):
                return {k: _filter_none(v) for k, v in value.items() if v is not None}

            return value

        return _filter_none(value)

    def _request(
        self,
        method: str,
        path: str,
        params: typing.Optional[dict[str, object]] = None,
        query: typing.Optional[dict[str, typing.Any]] = None,
    ):

        url = urllib.parse.urljoin(self.base_url, path)

        params = self._prepare_params(params) if params else params

        headers = {"X-GR4VY-MERCHANT-ACCOUNT-ID": self.merchant_account_id}

        response = self.session.request(
            method,
            url,
            params=query,
            json=params,
            auth=BearerAuth(self.token),
            headers=headers,
        )

        try:
            json_data = response.json()
        except requests.JSONDecodeError:
            json_data = None

        data = json_data if isinstance(json_data, dict) else {"data": json_data}
        if not response.ok:
            raise Gr4vyError(
                message=data.get("message"),
                details=data.get("details"),
                http_status_code=response.status_code,
            )
        return json_data

    def _b64e(self, value: bytes) -> str:
        return base64.urlsafe_b64encode(value).decode("utf8").strip("=")

    def _thumbprint(self, jwk: dict) -> str:
        claims = {k: v for k, v in jwk.items() if k in {"kty", "crv", "x", "y"}}
        json_claims = json.dumps(claims, separators=(",", ":"), sort_keys=True)
        digest = hashes.Hash(hashes.SHA256())
        digest.update(json_claims.encode("utf8"))
        return self._b64e(digest.finalize())

    def generate_embed_token(self, embed_data, checkout_session_id=None):
        token = self.generate_token(embed_data=embed_data, checkout_session_id=checkout_session_id)
        return token

    def list_audit_logs(self, **kwargs):
        response = self._request("get", "/audit-logs", query=kwargs)
        print(response)
        return response

    def list_buyers(self, **kwargs):
        response = self._request("get", "/buyers", query=kwargs)
        return response

    def get_buyer(self, buyer_id):
        response = self._request("get", f"/buyers/{buyer_id}")
        return response

    def create_new_buyer(self, **kwargs):
        print(kwargs)
        response = self._request("post", f"/buyers", params=kwargs)
        return response

    def update_buyer(self, buyer_id, **kwargs):
        response = self._request("put", f"/buyers/{buyer_id}", params=kwargs)
        return response

    def delete_buyer(self, buyer_id):
        response = self._request("delete", f"/buyers/{buyer_id}")
        return response

    def get_buyer_shipping_details(self, buyer_id):
        response = self._request("get", f"/buyers/{buyer_id}/shipping-details")
        return response

    def add_buyer_shipping_details(self, buyer_id, **kwargs):
        response = self._request(
            "post", f"/buyers/{buyer_id}/shipping-details", params=kwargs
        )
        return response

    def update_buyer_shipping_details(self, buyer_id, shipping_detail_id, **kwargs):
        response = self._request(
            "put",
            f"/buyers/{buyer_id}/shipping-details/{shipping_detail_id}",
            params=kwargs,
        )
        return response

    def delete_buyer_shipping_details(self, buyer_id, shipping_detail_id):
        response = self._request(
            "delete", f"/buyers/{buyer_id}/shipping-details/{shipping_detail_id}"
        )
        return response

    def list_card_scheme_definitions(self):
        response = self._request("get", f"/card-scheme-definitions")
        return response

    def get_checkout_session(self, checkout_session_id):
        response = self._request("get", f"/checkout/sessions/{checkout_session_id}")
        return response

    def create_new_checkout_session(self, **kwargs):
        response = self._request("post", f"/checkout/sessions", params=kwargs)
        return response
    
    def update_checkout_session(self, checkout_session_id, **kwargs):
        response = self._request(
            "put", f"/checkout/sessions/{checkout_session_id}", params=kwargs)
        return response

    def update_checkout_session_fields(self, checkout_session_id, **kwargs):
        response = self._request(
            "put", f"/checkout/sessions/{checkout_session_id}/fields", params=kwargs
        )
        return response

    def delete_checkout_session(self, checkout_session_id):
        response = self._request("delete", f"/checkout/sessions/{checkout_session_id}")
        return response

    def register_digital_wallets(self, **kwargs):
        response = self._request("post", f"/digital-wallets", params=kwargs)
        return response

    def list_digital_wallets(self):
        response = self._request("get", f"/digital-wallets")
        return response

    def get_digital_wallet(self, digital_wallet_id):
        response = self._request("get", f"/digital-wallets/{digital_wallet_id}")
        return response

    def update_digital_wallet(self, digital_wallet_id, **kwargs):
        response = self._request(
            "put", f"/digital-wallets/{digital_wallet_id}", params=kwargs
        )
        return response

    def deregister_digital_wallet(self, digital_wallet_id):
        response = self._request("delete", f"/digital-wallets/{digital_wallet_id}")
        return response

    def get_stored_payment_method(self, payment_method_id):
        response = self._request("get", f"/payment-methods/{payment_method_id}")
        return response

    def list_buyer_payment_methods(self, **kwargs):
        response = self._request("get", f"/buyers/payment-methods", query=kwargs)
        return response

    def list_payment_methods(self, **kwargs):
        response = self._request("get", "/payment-methods", query=kwargs)
        return response

    def store_payment_method(self, **kwargs):
        response = self._request("post", f"/payment-methods", params=kwargs)
        return response

    def delete_payment_method(self, payment_method_id):
        response = self._request("delete", f"/payment-methods/{payment_method_id}")
        return response

    def list_payment_method_tokens(self, payment_method_id):
        response = self._request("get", f"/payment-methods/{payment_method_id}/tokens")
        return response

    def list_payment_options(self, **kwargs):
        response = self._request("get", "/payment-options", query=kwargs)
        return response

    def post_list_payment_options(self, **kwargs):
        response = self._request("post", f"/payment-options", params=kwargs)
        return response

    def get_payment_service_definition(self, payment_service_definition_id):
        response = self._request(
            "get", f"/payment-service-definitions/{payment_service_definition_id}"
        )
        return response

    def list_payment_service_definitions(self, **kwargs):
        response = self._request("get", "/payment-service-definitions", query=kwargs)
        return response

    def list_payment_services(self, **kwargs):
        response = self._request("get", "/payment-services", query=kwargs)
        return response

    def create_new_payment_service(self, **kwargs):
        response = self._request("post", f"/payment-services", params=kwargs)
        return response

    def delete_payment_service(self, payment_service_id):
        response = self._request("delete", f"/payment-services/{payment_service_id}")
        return response

    def get_payment_service(self, payment_service_id):
        response = self._request("get", f"/payment-services/{payment_service_id}")
        return response

    def update_payment_service(self, payment_service_id, **kwargs):
        response = self._request(
            "put", f"/payment-services/{payment_service_id}", params=kwargs
        )
        return response

    def list_all_report_executions(self, **kwargs):
        response = self._request("get", f"/report-executions", query=kwargs)
        return response

    def get_report_executions(self, report_execution_id):
        response = self._request("get", f"/report-executions/{report_execution_id}")
        return response

    def create_new_report(self, **kwargs):
        response = self._request("post", f"/reports", query=kwargs)
        return response

    def list_reports(self, **kwargs):
        response = self._request("get", f"/reports", query=kwargs)
        return response

    def get_report(self, report_id):
        response = self._request("get", f"/reports/{report_id}")
        return response

    def update_report(self, report_id, **kwargs):
        response = self._request("put", f"/reports/{report_id}", params=kwargs)
        return response

    def list_executions_for_report(self, report_id, **kwargs):
        response = self._request(
            "get", f"/reports/{report_id}/executions", query=kwargs
        )
        return response

    def generate_download_url_for_report_execution(
        self, report_id, report_execution_id
    ):
        response = self._request(
            "post", f"/reports/{report_id}/executions/{report_execution_id}/url"
        )
        return response

    def create_new_transaction(self, **kwargs):
        response = self._request("post", f"/transactions", params=kwargs)
        return response

    def capture_transaction(self, transaction_id, **kwargs):
        response = self._request(
            "post", f"/transactions/{transaction_id}/capture", params=kwargs
        )
        return response

    def get_transaction(self, transaction_id):
        response = self._request("get", f"/transactions/{transaction_id}")
        return response

    def sync_transaction(self, transaction_id):
        response = self._request("post", f"/transactions/{transaction_id}/sync")
        return response


    def list_transactions(self, **kwargs):
        response = self._request("get", "/transactions", query=kwargs)
        return response

    def refund_transaction(self, transaction_id, **kwargs):
        response = self._request(
            "post", f"/transactions/{transaction_id}/refunds", params=kwargs
        )
        return response

    def void_transaction(self, transaction_id):
        response = self._request("post", f"/transactions/{transaction_id}/void")
        return response

    def create_new_report(self, **kwargs):
        response = self._request("post", f"/reports", params=kwargs)
        return response

    def list_roles(self, **kwargs):
        response = self._request("get", "/roles", query=kwargs)
        return response

    def list_role_assignments(self, **kwargs):
        response = self._request("get", "/roles/assignments", query=kwargs)
        return response

    def create_new_role_assignment(self, **kwargs):
        response = self._request("post", "/roles/assignments", params=kwargs)
        return response

    def delete_role_assignment(self, role_assignment_id):
        response = self._request("get", f"/roles/assignments/{role_assignment_id}")
        return response

    def list_api_error_logs(self, **kwargs):
        response = self._request("get", "/api-logs", query=kwargs)
        return response


class Gr4vyClientWithBaseUrl(Gr4vyClient):
    def __init__(self, base_url, private_key, environment):
        super().__init__(base_url, private_key, environment)
