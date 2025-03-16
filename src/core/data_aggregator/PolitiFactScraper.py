import requests
import newspaper

from bs4 import BeautifulSoup

class PolitiFactScraper:
    """Scrapes a PolitiFact article, extracts sources that article used to verify the claim,
     fetches content from each of the sources and returns the scraped data."""

    def __init__(self):
        pass

    def return_page_content(self, article_url):
        """Fetch the main article content from PolitiFact."""

        article_data = {}
        response = self.return_response(article_url)
        if response:
            soup = BeautifulSoup(response.text, "html.parser")

            article_data["claim"] = self._return_claim(soup)
            article_data["claim check"] = self._return_claim_verification(soup)
            article_data["content"] =  self._return_politico_page_content(soup)
            article_data["sources"] = self.return_sources_with_content(soup)

            return article_data
        return None

    @staticmethod
    def return_response(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Error fetching article: {e}")
            return False

    @staticmethod
    def _return_claim(soup):
        claim = soup.find("div", "m-statement__quote").text.strip()
        return claim

    @staticmethod
    def _return_claim_verification(soup):
        return soup.find("div", "m-statement__meter").find("picture").find("img").attrs[
            'alt'].upper()

    @staticmethod
    def _return_politico_page_content(soup):
        # Content after removing unnecessary elements
        for tag in soup(["script", "style", "meta", "noscript"]):
            tag.extract()

        return " ".join(soup.stripped_strings)

    def return_sources_with_content(self, soup):
        """Extracts source supporting the claim verification from the article."""
        sources_data = self._get_sources_supporting_the_claim_verification(soup)
        for source in sources_data:
            if 'content_url' in source.keys():
                try:
                    obj = newspaper.article(source['content_url'])
                    source['title'] = obj.title
                    source['authors'] = obj.authors
                    source['_robots'] = obj.meta_data.get('robots',None)
                    source['published_at'] = obj.publish_date.__str__()
                    source['text'] = obj.text_cleaned
                except Exception as e:
                    print(f"{source['content_url']} extraction failed due to {e}")
                    # No action needed, but shouldn't break flow of execution either.
        return sources_data

    @staticmethod
    def _get_sources_supporting_the_claim_verification(soup):
        sources_data = []
        sources_box = soup.find("article", "m-superbox__content")
        for listed_source in sources_box.find_all("p"):
            source_data = { 'title': listed_source.text.strip()}
            if listed_source.find("a"):
                source_data['content_url'] = listed_source.find("a")["href"]
            sources_data.append(source_data)
        return sources_data

    @staticmethod
    def return_politico_page_content(url):
        """Fetch and extract content from a given source URL."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract title
            title = soup.title.string.strip() if soup.title else "No Title"

            # Remove scripts & styles
            for tag in soup(["script", "style", "meta", "noscript"]):
                tag.extract()

            # Extract text content
            content = " ".join(soup.stripped_strings)[:5000]  # Limit content size

            return {"url": url, "title": title, "content": content}

        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return {"url": url, "title": "Failed to fetch", "content": ""}
