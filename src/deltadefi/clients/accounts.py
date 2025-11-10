#
from typing import cast

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
    BuildTransferalTransactionResponse,
    GetOperationKeyResponse,
    GetOrderRecordResponse,
    GetOrderRecordsResponse,
    SubmitTransferalTransactionResponse,
)
from deltadefi.utils import check_required_parameter, check_required_parameters


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

        Args:
            status: The status of the order records to retrieve. It can be "openOrder",
                    "orderHistory", or "tradingHistory".
            limit: Optional; The maximum number of records to return. Defaults to 10, max 250.
            page: Optional; The page number for pagination. Defaults to 1.

        Returns:
            A GetOrderRecordsResponse object containing the order records.
        """
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
