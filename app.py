import streamlit as st
import pandas as pd
import numpy as np
from utils import get_tools_list, create_agent, parse_refs

st.title('ResearchBuddy')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("Ask your question here...")

if query:
    with st.chat_message("user"):
        st.markdown(query)

    try:
        st.session_state.messages.append({"role": "user", "content": query})
        
        tools = get_tools_list()
        agent = create_agent(tools)
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

