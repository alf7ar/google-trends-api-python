"""Fetch Google Trends data for keywords through an Apify Actor.

Usage: APIFY_TOKEN=... python trends.py "bitcoin" "ethereum" --geo EG --range "today 12-m"
"""
import argparse
import os

from apify_client import ApifyClient

ACTOR = "alfhar/google-trends-scraper-pro"


def get_trends(keywords, geo="", time_range="today 12-m", token=None):
    client = ApifyClient(token or os.environ["APIFY_TOKEN"])
    run = client.actor(ACTOR).call(
        run_input={"keywords": keywords, "geo": geo, "timeRange": time_range}
    )
    return list(client.dataset(run["defaultDatasetId"]).iterate_items())


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("keywords", nargs="+")
    ap.add_argument("--geo", default="")
    ap.add_argument("--range", default="today 12-m", dest="time_range")
    a = ap.parse_args()
    for item in get_trends(a.keywords, a.geo, a.time_range):
        print(item["keyword"], "avg", item["averageInterest"], "peak", item["peakDate"], item["peakValue"])
        for q in item["relatedQueries"]["rising"][:3]:
            print("  rising:", q["query"], q["formattedValue"])
