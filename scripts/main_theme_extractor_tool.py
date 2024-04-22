from llama_index.core.tools.tool_spec.base import BaseToolSpec
import yaml
from llama_index.llms.gemini import Gemini

class ThemeExtractorTool(BaseToolSpec):
    spec_functions = ["extract_theme"]

    def __init__(self, llm) -> None:
        """Initialize with parameters."""
        self.llm = llm

    def extract_theme(self, query: str) -> str:
        """
        Uses a large language model to identify the main theme of a query.

        Args:
            query (str): The question for which the main theme is to be identified.

        Returns:
            str: The main theme extracted from the query.
        """
        prompt = f"""
        You are an useful assistant that will receive a question and return the main theme of the question.
        Example:
        User: What are the limitations of large language models?
        Model: large language model  
        User: {query}
        Model:
        """
        query_space = self.llm.complete(prompt).text.strip()
        return query_space

# Uso da classe
if __name__ == "__main__":
    # Substitua 'llm' pelo seu objeto de modelo de linguagem real.
    # Carregar o arquivo YAML
    with open('credentials.yaml', 'r') as file:
        credenciais = yaml.safe_load(file)
    # Acessar as credenciais
    gemini_api_key = credenciais['gemini_api_key']
    llm=Gemini(model_name="models/gemini-1.0-pro-001", api_key=gemini_api_key)
    theme_extractor = ThemeExtractorTool(llm)
    query = "What are the main techniques for segmenting cancer nodules in lung images?"
    theme = theme_extractor.extract_theme(query)
    print(f"The main theme of the query is: '{theme}'")
