from func import get_claim_stats, get_claimable_positions, get_fee_share_wallet
from json import dumps

USERNAME: str = "winrar"
PROVIDER: str = "twitter"
MINT: str = "8fCWwxUWryzMWFS8WfuC7Tebkg5nWMQ4xrzrw7yJBAGS"
WALLET: str = "73qpRfXrjubTxhALJf2czmGVdadmk2PinmDM1aaHm5PV"

def main() -> None:
    status_code, response = get_claimable_positions(WALLET)
    print(status_code)
    print(dumps(response, indent=2))

if __name__ == "__main__":
    main()