"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from gr4vy import models, utils
from gr4vy._hooks import SDKHooks
from gr4vy.account_updater import AccountUpdater
from gr4vy.audit_logs import AuditLogs
from gr4vy.buyers import Buyers
from gr4vy.card_scheme_definitions import CardSchemeDefinitions
from gr4vy.checkout_sessions import CheckoutSessions
from gr4vy.digital_wallets import DigitalWallets
from gr4vy.gift_cards import GiftCards
from gr4vy.merchant_accounts import MerchantAccounts
from gr4vy.models import internal
from gr4vy.payment_methods import PaymentMethods
from gr4vy.payment_options import PaymentOptions
from gr4vy.payment_service_definitions import PaymentServiceDefinitions
from gr4vy.payment_services import PaymentServices
from gr4vy.payouts import Payouts
from gr4vy.refunds import Refunds
from gr4vy.transactions import Transactions
from gr4vy.types import OptionalNullable, UNSET
import httpx
from typing import Any, Callable, Dict, Optional, Union, cast
import weakref


class Gr4vy(BaseSDK):
    r"""Gr4vy: The Gr4vy API."""

    account_updater: AccountUpdater
    buyers: Buyers
    payment_methods: PaymentMethods
    gift_cards: GiftCards
    card_scheme_definitions: CardSchemeDefinitions
    digital_wallets: DigitalWallets
    transactions: Transactions
    refunds: Refunds
    payment_options: PaymentOptions
    payment_service_definitions: PaymentServiceDefinitions
    payment_services: PaymentServices
    audit_logs: AuditLogs
    checkout_sessions: CheckoutSessions
    merchant_accounts: MerchantAccounts
    payouts: Payouts

    def __init__(
        self,
        bearer_auth: Optional[Union[Optional[str], Callable[[], Optional[str]]]] = None,
        merchant_account_id: Optional[str] = None,
        id: Optional[str] = None,
        server: Optional[str] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param bearer_auth: The bearer_auth required for authentication
        :param merchant_account_id: Configures the merchant_account_id parameter for all supported operations
        :param id: Allows setting the id variable for url substitution
        :param server: The server by name to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        client_supplied = True
        if client is None:
            client = httpx.Client()
            client_supplied = False

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        async_client_supplied = True
        if async_client is None:
            async_client = httpx.AsyncClient()
            async_client_supplied = False

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        security: Any = None
        if callable(bearer_auth):
            # pylint: disable=unnecessary-lambda-assignment
            security = lambda: models.Security(bearer_auth=bearer_auth())
        else:
            security = models.Security(bearer_auth=bearer_auth)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        server_defaults: Dict[str, Dict[str, str]] = {
            "production": {
                "id": id or "example",
            },
            "sandbox": {
                "id": id or "example",
            },
        }

        _globals = internal.Globals(
            merchant_account_id=utils.get_global_from_env(
                merchant_account_id, "GR4VY_MERCHANT_ACCOUNT_ID", str
            ),
        )

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                client_supplied=client_supplied,
                async_client=async_client,
                async_client_supplied=async_client_supplied,
                globals=_globals,
                security=security,
                server_url=server_url,
                server=server,
                server_defaults=server_defaults,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        weakref.finalize(
            self,
            close_clients,
            cast(ClientOwner, self.sdk_configuration),
            self.sdk_configuration.client,
            self.sdk_configuration.client_supplied,
            self.sdk_configuration.async_client,
            self.sdk_configuration.async_client_supplied,
        )

        self._init_sdks()

    def _init_sdks(self):
        self.account_updater = AccountUpdater(self.sdk_configuration)
        self.buyers = Buyers(self.sdk_configuration)
        self.payment_methods = PaymentMethods(self.sdk_configuration)
        self.gift_cards = GiftCards(self.sdk_configuration)
        self.card_scheme_definitions = CardSchemeDefinitions(self.sdk_configuration)
        self.digital_wallets = DigitalWallets(self.sdk_configuration)
        self.transactions = Transactions(self.sdk_configuration)
        self.refunds = Refunds(self.sdk_configuration)
        self.payment_options = PaymentOptions(self.sdk_configuration)
        self.payment_service_definitions = PaymentServiceDefinitions(
            self.sdk_configuration
        )
        self.payment_services = PaymentServices(self.sdk_configuration)
        self.audit_logs = AuditLogs(self.sdk_configuration)
        self.checkout_sessions = CheckoutSessions(self.sdk_configuration)
        self.merchant_accounts = MerchantAccounts(self.sdk_configuration)
        self.payouts = Payouts(self.sdk_configuration)

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.client is not None
            and not self.sdk_configuration.client_supplied
        ):
            self.sdk_configuration.client.close()
        self.sdk_configuration.client = None

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.async_client is not None
            and not self.sdk_configuration.async_client_supplied
        ):
            await self.sdk_configuration.async_client.aclose()
        self.sdk_configuration.async_client = None
