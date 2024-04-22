import streamlit as st
import pandas as pd
import numpy as np
from scripts.utils import get_tools_list, create_agent, parse_refs

st.title('ResearchBuddy')

gemini_api_key = st.sidebar.text_input('Gemini API Key', type='password')
serpapi_api_key = st.sidebar.text_input('SerpAPI API Key', type='password')

start_message = """
Hi, I'm ResearchBuddy! I use Google's Gemini model to help you with your literature search.

To work, I need you to add the API keys requested in the sidebar. 

I use these APIs to:
* Collect article data directly from Google Scholar to answer your questions.
* Formulate a user-friendly answer to your question.

To obtain the API keys, go to the following links:

[Gemini](https://ai.google.dev/)

[SerpAPI](https://serpapi.com/users/sign_up)

"""

with st.chat_message("assistant"):
    st.markdown(start_message)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("Ask your question here...")

if gemini_api_key and serpapi_api_key:

    if query:
        with st.chat_message("user"):
            st.markdown(query)

        try:
            st.session_state.messages.append({"role": "user", "content": query})
            
            tools = get_tools_list(serpapi_api_key, gemini_api_key)
            agent = create_agent(tools, gemini_api_key)
            response = agent.chat(query)
            papers = parse_refs(response.sources)

            with st.chat_message("assistant"):
                st.markdown(str(response))
            st.session_state.messages.append({"role": "assistant", "content": str(response)})

            with st.chat_message("assistant"):
                st.markdown(papers)
            st.session_state.messages.append({"role": "assistant", "content": papers})
        except:
            with st.chat_message("assistant"):
                st.markdown("I couldn't find any papers related to your question. Try writing it in a different way.")

else:
    with st.chat_message("assistant"):
        st.markdown("Please add the requested API keys to the sidebar.")