from requests import get
from json import loads, dump

def main() -> None:
    response = get("https://api2.bags.fm/api/v1/token-launch/top-tokens/lifetime-fees")
    data: dict[str, str | dict] = loads(response.text)
    results: dict[str, dict[str, str | float | int]] = {}

    if data["success"]:
        for i, t in enumerate(data["response"]):
            info: dict[str, str | float | int] = {}
            total_fees = float(t.get("lifetimeFees", 0))
            info["mint"] = t
            info["link"] = f"https://bags.fm/{t}"
            info["totalFees"] = total_fees
            if total_fees > 0:
                print(f"{i}) {t["tokenInfo"]["symbol"]} - total fees: {round(total_fees / (10 ** 9), 2)} SOL")
                print(t["token"])
                users: dict[int, str] = {}
                for i, c in enumerate(t.get("creators", [])):
                    print(f"{c['providerUsername'] or "missing"} | {c["royaltyBps"] / 100} | {round(float(c["totalClaimed"]) / (10 ** 9), 2)} SOL")
                    total_fees -= float(c["totalClaimed"])
                    if c["provider"] == "twitter":
                        users[i]["link"] = f"x.com/{c['providerUsername']}"
                    users[i] = {
                        "provider": c["provider"],
                        "providerUsername": c["providerUsername"],
                        "claimedSol": round(float(c["totalClaimed"]) / (10 ** 9), 2),
                        "royaltySplit": c["royaltyBps"] / 100,
                        "isCreator": c["isCreator"]
                                }
                unclaimed = round(total_fees / (10 ** 9), 2)
                print(f"{unclaimed} SOL available!")
            print("\n")

    with open(".\\exports\\bags_top_100.json", "w", encoding="utf-8") as f:
        dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
