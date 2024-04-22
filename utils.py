import yaml
from llama_index.llms.gemini import Gemini
from llama_index.core import ServiceContext
from llama_index.embeddings.gemini import GeminiEmbedding
from google_scholar_tool import GoogleScholarToolSpec
from main_theme_extractor_tool import ThemeExtractorTool
from llama_index.core.agent import ReActAgent
from llama_index.core.memory import ChatMemoryBuffer

memory = ChatMemoryBuffer.from_defaults(token_limit=3900)

# Carregar o arquivo YAML
with open('credentials.yaml', 'r') as file:
    credenciais = yaml.safe_load(file)
# Acessar as credenciais
gemini_api_key = credenciais['gemini_api_key']
serpapi_api_key = credenciais['serpapi_api_key']

llm=Gemini(model_name="models/gemini-1.0-pro-001", api_key=gemini_api_key)
service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=GeminiEmbedding(model_name="models/embedding-001", api_key=gemini_api_key)
)

def get_tools_list():
    scholar_tool = GoogleScholarToolSpec(serpapi_api_key).to_tool_list()
    query_key = ThemeExtractorTool(llm).to_tool_list()

    tools = scholar_tool + query_key
    return tools

def create_agent(tools):
    context = """
    You are responsible for summarizing the bibliographical references for a search. \n
    You will be given a question and must use the tools available to find the central theme \n
    of the search from the query and obtain papers related to that theme. 
    \n\n
    You should respond with:\n
    * The answer to the question asked by the user\n
    * And the references of all the articles found, including names, authors and access links
    """

    agent = ReActAgent.from_tools(
        tools,
        llm=llm,
        verbose=True,
        context=context,
        memory=memory
    )

    return agent

def parse_refs(sources):
    all_refs = "References:\n\n"
    for tool in sources:
        if tool.tool_name == 'google_scholar_query':
            for ref in tool.raw_output:   
                ref_str = f"{ref['title']}\n\n{ref['authors_reviews_year_pub']}\n\n{ref['link']}\n\n"
                all_refs+=ref_str

    return all_refs
    