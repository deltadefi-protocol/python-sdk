#
from typing import Literal, cast
import warnings

from sidan_gin import Asset, UTxO

from deltadefi.api import API
from deltadefi.models.models import OrderStatusType
from deltadefi.responses import (
    BuildDepositTransactionResponse,
    BuildWithdrawalTransactionResponse,
    CreateNewAPIKeyResponse,
    GetAccountBalanceResponse,
    GetDepositRecordsResponse,
    GetWithdrawalRecordsResponse,
    SubmitDepositTransactionResponse,
    SubmitWithdrawalTransactionResponse,
)
from deltadefi.responses.accounts import (
    BuildRequestTransferalTransactionResponse,
    BuildTransferalTransactionResponse,
    CreateSpotAccountResponse,
    GetAPIKeyResponse,
    GetMaxDepositResponse,
    GetOpenOrdersResponse,
    GetOperationKeyResponse,
    GetOrderRecordResponse,
    GetOrderRecordsResponse,
    GetSpotAccountResponse,
    GetTradeOrdersResponse,
    GetTradesResponse,
    GetTransferalRecordResponse,
    GetTransferalRecordsResponse,
    SubmitRequestTransferalTransactionResponse,
    SubmitTransferalTransactionResponse,
    UpdateSpotAccountResponse,
)
from deltadefi.utils import check_required_parameter, check_required_parameters

TransferalType = Literal["deposit", "withdrawal"]


class Accounts(API):
    """
    Accounts client for interacting with the DeltaDeFi API.
    """

    group_url_path = "/accounts"

    def __init__(self, api_key=None, base_url=None, **kwargs):
        super().__init__(api_key=api_key, base_url=base_url, **kwargs)

    def get_operation_key(self, **kwargs) -> GetOperationKeyResponse:
        """
        Get the encrypted operation key.

        Returns:
            A GetOperationKeyResponse object containing the encrypted operation key and its hash.
        """

        url_path = "/operation-key"
        return cast(
            "GetOperationKeyResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def create_new_api_key(self, **kwargs) -> CreateNewAPIKeyResponse:
        """
        Create a new API key.

        Returns:
            A CreateNewAPIKeyResponse object containing the new API key.
        """

        url_path = "/new-api-key"
        return cast(
            "CreateNewAPIKeyResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_deposit_records(self, **kwargs) -> GetDepositRecordsResponse:
        """
        Get deposit records.

        Returns:
            A GetDepositRecordsResponse object containing the deposit records.
        """
        url_path = "/deposit-records"
        return cast(
            "GetDepositRecordsResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_withdrawal_records(self, **kwargs) -> GetWithdrawalRecordsResponse:
        """
        Get withdrawal records.

        Returns:
            A GetWithdrawalRecordsResponse object containing the withdrawal records.
        """
        url_path = "/withdrawal-records"
        return cast(
            "GetWithdrawalRecordsResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_order_records(
        self, status: OrderStatusType, **kwargs
    ) -> GetOrderRecordsResponse:
        """
        Get order records.

        .. deprecated::
            Use :meth:`get_open_orders`, :meth:`get_trade_orders`, or :meth:`get_trades` instead.

        Args:
            status: The status of the order records to retrieve. It can be "openOrder",
                    "orderHistory", or "tradingHistory".
            limit: Optional; The maximum number of records to return. Defaults to 10, max 250.
            page: Optional; The page number for pagination. Defaults to 1.

        Returns:
            A GetOrderRecordsResponse object containing the order records.
        """
        warnings.warn(
            "get_order_records is deprecated. Use get_open_orders, get_trade_orders, "
            "or get_trades instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        check_required_parameter(status, "status")
        payload = {"status": status, **kwargs}

        url_path = "/order-records"
        return cast(
            "GetOrderRecordsResponse",
            self.send_request("GET", self.group_url_path + url_path, payload),
        )

    def get_order_record(self, order_id: str, **kwargs) -> GetOrderRecordResponse:
        """
        Get a single order record by order ID.

        Args:
            order_id: The ID of the order to retrieve.

        Returns:
            A GetOrderRecordResponse object containing the order record.
        """
        check_required_parameter(order_id, "order_id")

        url_path = f"/order/{order_id}"
        return cast(
            "GetOrderRecordResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_account_balance(self, **kwargs) -> GetAccountBalanceResponse:
        """
        Get account balance.

        Returns:
            A GetAccountBalanceResponse object containing the account balance.
        """
        url_path = "/balance"
        return cast(
            "GetAccountBalanceResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def build_deposit_transaction(
        self, deposit_amount: list[Asset], input_utxos: list[UTxO], **kwargs
    ) -> BuildDepositTransactionResponse:
        """
        Build a deposit transaction.

        Args:
            data: A BuildDepositTransactionRequest object containing the deposit transaction details.

        Returns:
            A BuildDepositTransactionResponse object containing the built deposit transaction.
        """

        check_required_parameters(
            [[deposit_amount, "deposit_amount"], [input_utxos, "input_utxos"]]
        )
        payload = {
            "deposit_amount": deposit_amount,
            "input_utxos": input_utxos,
            **kwargs,
        }

        url_path = "/deposit/build"
        return cast(
            "BuildDepositTransactionResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )

    def build_withdrawal_transaction(
        self, withdrawal_amount: list[Asset], **kwargs
    ) -> BuildWithdrawalTransactionResponse:
        """
        Build a withdrawal transaction.

        Args:
            data: A BuildWithdrawalTransactionRequest object containing the withdrawal transaction details.

        Returns:
            A BuildWithdrawalTransactionResponse object containing the built withdrawal transaction.
        """

        check_required_parameter(withdrawal_amount, "withdrawal_amount")
        payload = {"withdrawal_amount": withdrawal_amount, **kwargs}

        url_path = "/withdrawal/build"
        return cast(
            "BuildWithdrawalTransactionResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )

    def build_transferal_transaction(
        self, transferal_amount: list[Asset], to_address: str, **kwargs
    ) -> BuildTransferalTransactionResponse:
        """
        Build a transferal transaction.

        Args:
            data: A BuildTransferalTransactionRequest object containing the transferal transaction details.

        Returns:
            A BuildTransferalTransactionResponse object containing the built transferal transaction.
        """

        check_required_parameters(
            [[transferal_amount, "transferal_amount"], [to_address, "to_address"]]
        )
        payload = {
            "transferal_amount": transferal_amount,
            "to_address": to_address,
            **kwargs,
        }

        url_path = "/transferal/build"
        return cast(
            "BuildTransferalTransactionResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )

    def submit_deposit_transaction(
        self, signed_tx: str, **kwargs
    ) -> SubmitDepositTransactionResponse:
        """
        Submit a deposit transaction.

        Args:
            data: A SubmitDepositTransactionRequest object containing the deposit transaction details.

        Returns:
            A SubmitDepositTransactionResponse object containing the submitted deposit transaction.
        """

        check_required_parameter(signed_tx, "signed_tx")
        payload = {"signed_tx": signed_tx, **kwargs}

        url_path = "/deposit/submit"
        return cast(
            "SubmitDepositTransactionResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )

    def submit_withdrawal_transaction(
        self, signed_tx: str, **kwargs
    ) -> SubmitWithdrawalTransactionResponse:
        """
        Submit a withdrawal transaction.

        Args:
            data: A SubmitWithdrawalTransactionRequest object containing the withdrawal transaction details.

        Returns:
            A SubmitWithdrawalTransactionResponse object containing the submitted withdrawal transaction.
        """

        check_required_parameter(signed_tx, "signed_tx")
        payload = {"signed_tx": signed_tx, **kwargs}

        url_path = "/withdrawal/submit"
        return cast(
            "SubmitWithdrawalTransactionResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )

    def submit_transferal_transaction(
        self, signed_tx: str, **kwargs
    ) -> SubmitTransferalTransactionResponse:
        """
        Submit a transferal transaction.

        Args:
            data: A SubmitTransferalTransactionRequest object containing the transferal transaction details.

        Returns:
            A SubmitTransferalTransactionResponse object containing the submitted transferal transaction.
        """

        check_required_parameter(signed_tx, "signed_tx")
        payload = {"signed_tx": signed_tx, **kwargs}

        url_path = "/transferal/submit"
        return cast(
            "SubmitTransferalTransactionResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )

    def build_request_transferal_transaction(
        self,
        transferal_amount: list[Asset],
        from_address: str,
        transferal_type: TransferalType,
        **kwargs,
    ) -> BuildRequestTransferalTransactionResponse:
        """
        Build a request transferal transaction.

        Args:
            transferal_amount: The list of assets to transfer.
            from_address: The address to request the transferal from.
            transferal_type: The type of transferal ("deposit" or "withdrawal").

        Returns:
            A BuildRequestTransferalTransactionResponse object containing the tx_hex.
        """

        check_required_parameters(
            [
                [transferal_amount, "transferal_amount"],
                [from_address, "from_address"],
                [transferal_type, "transferal_type"],
            ]
        )
        payload = {
            "transferal_amount": transferal_amount,
            "from_address": from_address,
            "transferal_type": transferal_type,
            **kwargs,
        }

        url_path = "/request-transferal/build"
        return cast(
            "BuildRequestTransferalTransactionResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )

    def submit_request_transferal_transaction(
        self, signed_tx: str, **kwargs
    ) -> SubmitRequestTransferalTransactionResponse:
        """
        Submit a request transferal transaction.

        Args:
            signed_tx: The signed transaction hex string.

        Returns:
            A SubmitRequestTransferalTransactionResponse object containing the tx_hash.
        """

        check_required_parameter(signed_tx, "signed_tx")
        payload = {"signed_tx": signed_tx, **kwargs}

        url_path = "/request-transferal/submit"
        return cast(
            "SubmitRequestTransferalTransactionResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )

    def get_spot_account(self, **kwargs) -> GetSpotAccountResponse:
        """
        Get the spot account details.

        Returns:
            A GetSpotAccountResponse object containing the spot account details.
        """
        url_path = "/spot-account"
        return cast(
            "GetSpotAccountResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def create_spot_account(
        self,
        user_id: str,
        encrypted_operation_key: str,
        operation_key_hash: str,
        is_script_operation_key: bool,
        **kwargs,
    ) -> CreateSpotAccountResponse:
        """
        Create a new spot account.

        Args:
            user_id: The user ID for the spot account.
            encrypted_operation_key: The encrypted operation key.
            operation_key_hash: The hash of the operation key.
            is_script_operation_key: Whether the operation key is a script key.

        Returns:
            A CreateSpotAccountResponse object containing the created spot account details.
        """
        check_required_parameters(
            [
                [user_id, "user_id"],
                [encrypted_operation_key, "encrypted_operation_key"],
                [operation_key_hash, "operation_key_hash"],
                [is_script_operation_key, "is_script_operation_key"],
            ]
        )
        payload = {
            "user_id": user_id,
            "encrypted_operation_key": encrypted_operation_key,
            "operation_key_hash": operation_key_hash,
            "is_script_operation_key": is_script_operation_key,
            **kwargs,
        }

        url_path = "/spot-account"
        return cast(
            "CreateSpotAccountResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )

    def update_spot_account(
        self,
        user_id: str,
        encrypted_operation_key: str,
        **kwargs,
    ) -> UpdateSpotAccountResponse:
        """
        Update the spot account.

        Args:
            user_id: The user ID for the spot account.
            encrypted_operation_key: The new encrypted operation key.

        Returns:
            An UpdateSpotAccountResponse object containing the updated spot account details.
        """
        check_required_parameters(
            [
                [user_id, "user_id"],
                [encrypted_operation_key, "encrypted_operation_key"],
            ]
        )
        payload = {
            "user_id": user_id,
            "encrypted_operation_key": encrypted_operation_key,
            **kwargs,
        }

        url_path = "/spot-account"
        return cast(
            "UpdateSpotAccountResponse",
            self.send_request("PATCH", self.group_url_path + url_path, payload),
        )

    def get_transferal_records(self, **kwargs) -> GetTransferalRecordsResponse:
        """
        Get transferal records.

        Args:
            limit: Optional; The maximum number of records to return (1-250).
            page: Optional; The page number for pagination (1-1000).
            status: Optional; Filter by status ("pending" or "confirmed").

        Returns:
            A GetTransferalRecordsResponse object containing the transferal records.
        """
        url_path = "/transferal-records"
        return cast(
            "GetTransferalRecordsResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_transferal_record_by_tx_hash(
        self, tx_hash: str, **kwargs
    ) -> GetTransferalRecordResponse:
        """
        Get a transferal record by transaction hash.

        Args:
            tx_hash: The transaction hash of the transferal.

        Returns:
            A GetTransferalRecordResponse object containing the transferal record.
        """
        check_required_parameter(tx_hash, "tx_hash")

        url_path = f"/transferal-records/{tx_hash}"
        return cast(
            "GetTransferalRecordResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_api_key(self, **kwargs) -> GetAPIKeyResponse:
        """
        Get the current API key details.

        Returns:
            A GetAPIKeyResponse object containing the API key and created_at timestamp.
        """
        url_path = "/api-key"
        return cast(
            "GetAPIKeyResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_max_deposit(self, **kwargs) -> GetMaxDepositResponse:
        """
        Get the maximum deposit amount.

        Returns:
            A GetMaxDepositResponse object containing the max_deposit value.
        """
        url_path = "/max-deposit"
        return cast(
            "GetMaxDepositResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_open_orders(self, symbol: str, **kwargs) -> GetOpenOrdersResponse:
        """
        Get open orders for a given symbol.

        Args:
            symbol: The trading pair symbol (e.g., "ADAUSDM").
            limit: Optional; The maximum number of records to return (1-250).
            page: Optional; The page number for pagination (1-1000).

        Returns:
            A GetOpenOrdersResponse object containing the open orders.
        """
        check_required_parameter(symbol, "symbol")
        payload = {"symbol": symbol, **kwargs}

        url_path = "/open-orders"
        return cast(
            "GetOpenOrdersResponse",
            self.send_request("GET", self.group_url_path + url_path, payload),
        )

    def get_trade_orders(self, symbol: str, **kwargs) -> GetTradeOrdersResponse:
        """
        Get trade orders (order history) for a given symbol.

        Args:
            symbol: The trading pair symbol (e.g., "ADAUSDM").
            limit: Optional; The maximum number of records to return (1-250).
            page: Optional; The page number for pagination (1-1000).

        Returns:
            A GetTradeOrdersResponse object containing the trade orders.
        """
        check_required_parameter(symbol, "symbol")
        payload = {"symbol": symbol, **kwargs}

        url_path = "/trade-orders"
        return cast(
            "GetTradeOrdersResponse",
            self.send_request("GET", self.group_url_path + url_path, payload),
        )

    def get_trades(self, symbol: str, **kwargs) -> GetTradesResponse:
        """
        Get account trades (execution records) for a given symbol.

        Args:
            symbol: The trading pair symbol (e.g., "ADAUSDM").
            limit: Optional; The maximum number of records to return (1-250).
            page: Optional; The page number for pagination (1-1000).

        Returns:
            A GetTradesResponse object containing the account trades.
        """
        check_required_parameter(symbol, "symbol")
        payload = {"symbol": symbol, **kwargs}

        url_path = "/trades"
        return cast(
            "GetTradesResponse",
            self.send_request("GET", self.group_url_path + url_path, payload),
        )
