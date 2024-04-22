from llama_index.core.tools.tool_spec.base import BaseToolSpec
import yaml
import requests
import urllib.parse
from typing import Optional, List, Dict
from datetime import datetime


class GoogleScholarToolSpec(BaseToolSpec):
    spec_functions = ["google_scholar_query"]

    def __init__(self, api_key: Optional[str] = None) -> None:
        """Initialize with parameters."""
        self.api_key = api_key

    def google_scholar_query(self, query: str, num_papers: int = 5) -> List[Dict]:
        """
        Make a query to Google Scholar to find papers with their titles, abstracts, authors, publication year, publication venue, and DOI.
        Filters the results to only include papers from the last two years using as_ylo and as_yhi parameters.

        Example inputs:
            "deep learning"
            "quantum mechanics applications"

        Args:
            query (str): The query to be passed to Google Scholar.
            num_papers (int): The maximum number of papers to retrieve.
        """
        current_year = datetime.now().year
        query_url = f"https://serpapi.com/search.json?engine=google_scholar&q={urllib.parse.quote_plus(query)}&api_key={self.api_key}&as_ylo={current_year-2}&as_yhi={current_year}"
        response = requests.get(query_url)
        papers = []
        results_processed = 0

        while results_processed < num_papers and query_url:
            response = requests.get(query_url)
            if response.status_code == 200:
                data = response.json()
                results = data.get('organic_results', [])
                for paper in results:
                    if results_processed >= num_papers:
                        break
                    title = paper.get('title')
                    snippet = paper.get('snippet')
                    infos = paper.get('publication_info')
                    pub_infos = infos.get('summary')
                    link = paper.get('link')
                    papers.append({
                        "title": title,
                        "abstract": snippet,
                        "authors_reviews_year_pub": pub_infos,
                        "link": link
                    })
                    results_processed += 1
                # Update query_url to the next page if available and needed
                query_url = data.get('serpapi_pagination', {}).get('next') if results_processed < num_papers else None

        return papers

# Uso da classe
if __name__ == "__main__":
    # Carregar o arquivo YAML
    with open('credentials.yaml', 'r') as file:
        credenciais = yaml.safe_load(file)
    # Acessar as credenciais
    serpapi_api_key = credenciais['serpapi_api_key']

    scholar_tool = GoogleScholarToolSpec(api_key=serpapi_api_key)
    query = "classification of lung diseases on CT images"
    num_papers = 10  # Define quantos papers você deseja retornar
    results = scholar_tool.google_scholar_query(query, num_papers=num_papers)
    for paper in results:
        print(f"Title: {paper['title']}")
        print(f"Abstract: {paper['abstract']}")
        print(f"{paper['authors_reviews_year_pub']}")
        print(f"Link: {paper['link']}\n")