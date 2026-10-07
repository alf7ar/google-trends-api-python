# google-trends-api-python

A tiny Python client that returns Google Trends data (interest over time, interest by region, related queries) as JSON, without pytrends.

## The problem

- [pytrends](https://github.com/GeneralMills/pytrends) is **archived on GitHub** (read-only, last push August 2024). It is unmaintained, so open issues will not be fixed.
- Google rate limits automated Google Trends requests (HTTP 429), so scripts that depend on a scraper library break often.

This repo calls a hosted [Apify Actor](https://apify.com/alfhar/google-trends-scraper-pro) instead and gives you one JSON item per keyword.

> **Disclosure:** the Apify Actor linked here was built by the author of this repo. It is a paid Actor (pay per event, about $0.003 per keyword plus a small start fee; check the Actor page for current prices). You need an Apify account and API token. This client is MIT licensed.

## Quick start

```bash
pip install -r requirements.txt
export APIFY_TOKEN=your_token_here
python trends.py bitcoin ethereum --geo EG --range "today 12-m"
```

Or from your own code:

```python
from trends import get_trends

for item in get_trends(["iphone", "samsung galaxy"], geo="SA", time_range="today 3-m"):
    print(item["keyword"], item["averageInterest"], item["peakDate"])
```

## Example output

Shortened sample, see [`example_output.json`](example_output.json):

| keyword | geo | averageInterest | peakDate | peakValue | top related query |
|---|---|---|---|---|---|
| bitcoin | EG | 32.32 | 2026-05-03 | 100 | bitcoin price |

## pytrends to this client

| pytrends | JSON field |
|---|---|
| `interest_over_time()` | `interestOverTime` |
| `interest_by_region()` | `interestByRegion` |
| `related_queries()` | `relatedQueries.top` / `.rising` |

Values are relative (0-100), like Google Trends itself, not absolute search counts.

## Links

- Apify Actor: https://apify.com/alfhar/google-trends-scraper-pro (built by the author of this repo)

## License

MIT
