from datetime import datetime, timedelta
from typing import Any, Dict, Optional

import pandas as pd
import requests

session = "<Enter your session cookie here>"
private_leaderboard_id = "<Enter private leaderboard id>"

def fetch_aoc_private_leaderboard_stats() -> Dict[str, Any]:
    cookies = {'session': session}
    return requests.get(f'https://adventofcode.com/2022/leaderboard/private/view/{private_leaderboard_id}.json', cookies=cookies).json()


def parse_time(dt: Optional[int]) -> Optional[str]:
    if dt is None:
        return None

    return (datetime.utcfromtimestamp(dt) + timedelta(hours=5, minutes=30)).__str__()

def main():
    results = []
    data = fetch_aoc_private_leaderboard_stats()

    for mem in data.get("members", {}).values():
        for day, parts in mem["completion_day_level"].items():
            person = {
                "Name": mem["name"],
                "Day": day,
                "Part 1": parse_time(parts.get("1", {}).get("get_star_ts")),
                "Part 2": parse_time(parts.get("2", {}).get("get_star_ts"))
            }
            results.append(person)

    df = pd.DataFrame(results)
    df.to_csv(f"./{datetime.now().date().__str__()}.csv")


if __name__ == "__main__":
    main()
