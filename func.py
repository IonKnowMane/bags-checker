from requests import get
from json import dumps
from typing import Any
from dotenv import load_dotenv
from os import getenv

load_dotenv()
BAGS = getenv("BAGS_API_KEY")


def get_claim_stats(mint: str) -> tuple[str, dict[str, Any]]:

    url = "https://public-api-v2.bags.fm/api/v1/token-launch/claim-stats"

    headers = {"x-api-key": "bags_prod_e6S981xsTfDMUQI4ZDMspsf2sBeFQbR6THaOSg40nsY"}
    params = {"tokenMint": mint}

    response = get(url, headers=headers, params=params)

    return response.status_code, response.json


def get_claimable_positions(pubkey: str) -> tuple[str, dict[str, Any]]:

    url = "https://public-api-v2.bags.fm/api/v1/token-launch/claim-stats"

    headers = {"x-api-key": "bags_prod_e6S981xsTfDMUQI4ZDMspsf2sBeFQbR6THaOSg40nsY"}
    params = {"tokenMint": mint}

    response = get(url, headers=headers, params=params)

    return response.status_code, response.json