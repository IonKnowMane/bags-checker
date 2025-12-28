from requests import get
from json import loads, dump

def main() -> None:
    response = get("https://api2.bags.fm/api/v1/token-launch/top-tokens/lifetime-fees")
    data: dict = loads(response.text)
    results: list = []
    export: dict = {}

    if data["success"]:
        for i, t in enumerate(data["response"]):
            info: dict[str, str | float | int] = {}
            total_fees = float(t.get("lifetimeFees", 0))
            info["mint"] = t["token"]
            info["link"] = f"https://bags.fm/{t["token"]}"
            info["totalFees"] = round(total_fees / (10 ** 9), 2)
            print(f"{i}) {t["tokenInfo"]["symbol"]} - total fees: {round(total_fees / (10 ** 9), 2)} SOL")
            print(t["token"])
            users = []
            for i, c in enumerate(t.get("creators", [])):
                print(f"{c['providerUsername'] or "missing"} | {c["royaltyBps"] / 100} | {round(float(c["totalClaimed"]) / (10 ** 9), 2)} SOL")
                total_fees -= float(c["totalClaimed"])
                user = {
                    "isCreator": c["isCreator"],
                    "claimedSol": round(float(c["totalClaimed"]) / (10 ** 9), 2),
                    "provider": c["provider"],
                    "providerUsername": c["providerUsername"],
                    "link": f"https://x.com/{c['providerUsername']}" if c["provider"] == "twitter" else None,
                    "royaltySplit": c["royaltyBps"] / 100
                        }
                users.append(user)
            unclaimed = round(total_fees / (10 ** 9), 2)
            info["users"] = users
            info["unclaimedSol"] = unclaimed
            print(f"{unclaimed} SOL available!")
            print("\n")
            results.append(info)

    export["data"] = results

    with open(".\\exports\\bags_top_100.json", "w", encoding="utf-8") as f:
        dump(export, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
