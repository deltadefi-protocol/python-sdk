from typing import cast

from deltadefi.api import API
from deltadefi.responses.points import (
    ClaimQuestResponse,
    GetActiveQuestsResponse,
    GetLeaderboardResponse,
    GetLeaguesResponse,
    GetMyClaimsResponse,
    GetMyPointsResponse,
    GetMyRankResponse,
    GetPointsBreakdownResponse,
    GetPointsHistoryResponse,
    GetReferralInfoResponse,
    UpdateReferralCodeResponse,
)
from deltadefi.utils import check_required_parameter


class Points(API):
    """
    Points client for interacting with the DeltaDeFi Points/Rewards API.

    Provides access to points tracking, leaderboards, leagues, and quests.
    All endpoints require authentication via API key.
    """

    group_url_path = "/points"

    def __init__(self, api_key=None, base_url=None, **kwargs):
        super().__init__(api_key=api_key, base_url=base_url, **kwargs)

    # =========================================================================
    # Points - User's own data
    # =========================================================================

    def get_my_points(self, **kwargs) -> GetMyPointsResponse:
        """
        Get the current user's points summary.

        Returns:
            A GetMyPointsResponse object containing total points, season points,
            league, referral code, and last update timestamp.
        """
        url_path = "/me"
        return cast(
            "GetMyPointsResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_points_history(
        self, page: int = 1, per_page: int = 20, **kwargs
    ) -> GetPointsHistoryResponse:
        """
        Get the current user's points history with pagination.

        Args:
            page: Page number (default: 1).
            per_page: Items per page (default: 20).

        Returns:
            A dict containing points history entries.
        """
        payload = {"page": page, "per_page": per_page, **kwargs}
        url_path = "/me/history"
        return cast(
            "GetPointsHistoryResponse",
            self.send_request("GET", self.group_url_path + url_path, payload),
        )

    def get_referral_info(self, **kwargs) -> GetReferralInfoResponse:
        """
        Get the current user's referral information.

        Returns:
            A dict containing referral info (code, count, points earned).
        """
        url_path = "/me/referral"
        return cast(
            "GetReferralInfoResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_points_breakdown(self, **kwargs) -> GetPointsBreakdownResponse:
        """
        Get the current user's points breakdown by source.

        Returns:
            A dict containing points breakdown by category.
        """
        url_path = "/me/breakdown"
        return cast(
            "GetPointsBreakdownResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def update_referral_code(self, code: str, **kwargs) -> UpdateReferralCodeResponse:
        """
        Update the current user's referral code.

        Args:
            code: The new referral code.

        Returns:
            A dict containing the updated referral info.
        """
        check_required_parameter(code, "code")
        payload = {"code": code, **kwargs}
        url_path = "/me/referral-code"
        return cast(
            "UpdateReferralCodeResponse",
            self.send_request("PUT", self.group_url_path + url_path, payload),
        )

    # =========================================================================
    # Leaderboard
    # =========================================================================

    def get_leaderboard(
        self,
        page: int = 1,
        per_page: int = 20,
        season_id: int | None = None,
        **kwargs,
    ) -> GetLeaderboardResponse:
        """
        Get the points leaderboard with pagination.

        Args:
            page: Page number (default: 1).
            per_page: Items per page (default: 20).
            season_id: Optional season ID to filter by.

        Returns:
            A dict containing leaderboard entries.
        """
        payload = {"page": page, "per_page": per_page, **kwargs}
        if season_id is not None:
            payload["season_id"] = season_id

        url_path = "/leaderboard"
        return cast(
            "GetLeaderboardResponse",
            self.send_request("GET", self.group_url_path + url_path, payload),
        )

    def get_my_rank(self, season_id: int | None = None, **kwargs) -> GetMyRankResponse:
        """
        Get the current user's rank on the leaderboard.

        Args:
            season_id: Optional season ID to filter by.

        Returns:
            A dict containing the user's rank information.
        """
        payload = {**kwargs}
        if season_id is not None:
            payload["season_id"] = season_id

        url_path = "/leaderboard/me"
        return cast(
            "GetMyRankResponse",
            self.send_request("GET", self.group_url_path + url_path, payload),
        )

    # =========================================================================
    # Leagues
    # =========================================================================

    def get_leagues(self, **kwargs) -> GetLeaguesResponse:
        """
        Get available leagues.

        Returns:
            A dict containing league definitions.
        """
        url_path = "/leagues"
        return cast(
            "GetLeaguesResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    # =========================================================================
    # Quests
    # =========================================================================

    def get_active_quests(self, **kwargs) -> GetActiveQuestsResponse:
        """
        Get active quests for the current user.

        Returns:
            A dict containing active quest information.
        """
        url_path = "/quests/active"
        return cast(
            "GetActiveQuestsResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_my_claims(self, **kwargs) -> GetMyClaimsResponse:
        """
        Get the current user's quest claims.

        Returns:
            A dict containing the user's claimed quests.
        """
        url_path = "/quests/claims"
        return cast(
            "GetMyClaimsResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def claim_quest(self, quest_id: str, **kwargs) -> ClaimQuestResponse:
        """
        Claim a quest reward.

        Args:
            quest_id: The ID of the quest to claim.

        Returns:
            A dict containing the claim result.
        """
        check_required_parameter(quest_id, "quest_id")

        url_path = f"/quests/{quest_id}/claim"
        return cast(
            "ClaimQuestResponse",
            self.send_request("POST", self.group_url_path + url_path, kwargs),
        )
