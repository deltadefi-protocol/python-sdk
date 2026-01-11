from dataclasses import dataclass
from typing import Any, TypedDict


@dataclass
class GetMyPointsResponse(TypedDict):
    """
    Response for GET /points/me

    Known schema from espresso jigger_service.go
    """

    total_points: str
    season_points: str
    league: str
    referral_code: str
    updated_at: str


# All other Points responses are passthrough from Jigger service.
# Using dict[str, Any] as the response type since espresso returns interface{}
# and just proxies the Jigger response directly.

GetPointsHistoryResponse = dict[str, Any]
"""Response for GET /points/me/history - Passthrough from Jigger"""

GetReferralInfoResponse = dict[str, Any]
"""Response for GET /points/me/referral - Passthrough from Jigger"""

GetPointsBreakdownResponse = dict[str, Any]
"""Response for GET /points/me/breakdown - Passthrough from Jigger"""

UpdateReferralCodeResponse = dict[str, Any]
"""Response for PUT /points/me/referral-code - Passthrough from Jigger"""

GetLeaderboardResponse = dict[str, Any]
"""Response for GET /points/leaderboard - Passthrough from Jigger"""

GetMyRankResponse = dict[str, Any]
"""Response for GET /points/leaderboard/me - Passthrough from Jigger"""

GetLeaguesResponse = dict[str, Any]
"""Response for GET /points/leagues - Passthrough from Jigger"""

GetActiveQuestsResponse = dict[str, Any]
"""Response for GET /points/quests/active - Passthrough from Jigger"""

GetMyClaimsResponse = dict[str, Any]
"""Response for GET /points/quests/claims - Passthrough from Jigger"""

ClaimQuestResponse = dict[str, Any]
"""Response for POST /points/quests/:questId/claim - Passthrough from Jigger"""
