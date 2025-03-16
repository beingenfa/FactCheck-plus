import json

import requests

from src.core.data_aggregator.config.api_keys import GNEWS_API_KEY, NEWSAPI_KEY, THENEWSAPI_KEY, APITUBE_KEY


class NewsAggregator:
    """Unified class for fetching and aggregating news from multiple APIs."""

    API_CONFIG = {
        "apitube": {
            "api_key": APITUBE_KEY,
            "base_url": "https://api.apitube.io/v1/news/everything",
            "params": lambda query, api_key: {"query": query, "lang": "en", "page": 1, "api_key": api_key},
            "response_key": "data",
        },
        "gnews": {
            "api_key": GNEWS_API_KEY,
            "base_url": "https://gnews.io/api/v4/search",
            "params": lambda query, api_key: {"q": query, "lang": "en", "token": api_key, "sortby": "relevance"},
            "response_key": "articles",
        },
        "newsapi": {
            "api_key": NEWSAPI_KEY,
            "base_url": "https://newsapi.org/v2/everything",
            "params": lambda query, api_key: {"q": query, "language": "en", "apiKey": api_key, "sortBy": "relevancy"},
            "response_key": "articles",
        },
        "thenewsapi": {
            "api_key": THENEWSAPI_KEY,
            "base_url": "https://api.thenewsapi.com/v1/news/all",
            "params": lambda query, api_key: {
                "search": query, "language": "en", "page": 1, "api_token": api_key, "sort": "relevance_score"
            },
            "response_key": "data",
        },
    }

    def __init__(self, services=None):
        """
        Initialize the aggregator with selected services.

        :param services: List of services to fetch news from (e.g., ["gnews", "newsapi"]).
                         If None, fetch from all available sources.
        """
        self.services = services if services else list(self.API_CONFIG.keys())

    def fetch_news(self, query):
        """
        Fetch news from all selected services.

        :param query: Search query string.
        :return: List of aggregated news articles.
        """
        all_articles = []

        for service_name in self.services:
            if service_name not in self.API_CONFIG:
                print(f"Skipping unsupported service: {service_name}")
                continue

            config = self.API_CONFIG[service_name]
            params = config["params"](query, config["api_key"])

            try:
                response = requests.get(config["base_url"], params=params)
                response.raise_for_status()
                articles = self._parse_response(service_name, response.json(), config["response_key"])
                all_articles.extend(articles)
            except requests.exceptions.RequestException as e:
                print(f"Error fetching from {service_name}: {e}")

        return all_articles

    @staticmethod
    def _parse_response(service_name, response, response_key):
        """
        Parse API response into a unified format.

        :param service_name: The news service being processed.
        :param response: JSON response from API.
        :param response_key: Key to extract articles.
        :return: List of formatted articles.
        """
        return [
            {
                "title": article.get("title", "No Title"),
                "description": article.get("description", ""),
                "content": article.get("content", ""),
                "url": article.get("url", ""),
                "image": article.get("image") or article.get("image_url") or article.get("urlToImage"),
                "published_at": article.get("publishedAt") or article.get("published_at", ""),
                "source": json.dumps(article.get("source", {})),
                "service": service_name,
                "meta": {
                    "relevance_score": article.get("relevance_score"),
                    "categories": article.get("categories", []),
                    "keywords": article.get("keywords", ""),
                } if service_name == "thenewsapi" else {},
            }
            for article in response.get(response_key, [])
        ]
