from requests import get
from json import loads
from typing import Any
from dotenv import load_dotenv
from os import getenv

load_dotenv()
BAGS = getenv("BAGS_API_KEY")


def get_claim_stats(mint: str) -> tuple[int, dict[str, Any]]:

    url = "https://public-api-v2.bags.fm/api/v1/token-launch/claim-stats"

    headers = {"x-api-key": BAGS}
    params = {"tokenMint": mint}

    response = get(url, headers=headers, params=params)
    data = loads(response.text)

    return response.status_code, data


def get_claimable_positions(pubkey: str) -> tuple[int, dict[str, Any]]:

    url = "https://public-api-v2.bags.fm/api/v1/token-launch/claim-stats"

    headers = {"x-api-key": BAGS}
    params = {"wallet": pubkey}

    response = get(url, headers=headers, params=params)
    data = loads(response.text)

    return response.status_code, data


def get_fee_share_wallet(username: str, provider: str) -> tuple[int, dict[str, Any]]:

    url = "https://public-api-v2.bags.fm/api/v1/token-launch/fee-share/wallet/v2"

    headers = {"x-api-key": BAGS}
    params = {"provider": provider, "username": username}

    response = get(url, headers=headers, params=params)
    data = loads(response.text)

    return response.status_code, data
