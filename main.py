import streamlit as st
from streamlit_chat import message
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from utils import get_conversation_string, query_refiner, find_match

# Load environment variables
load_dotenv()

# Set up the page
st.set_page_config(page_title="Pookie Chatbot", page_icon="🤖")
st.subheader("Pookie Chatbot is Here: Ask Any Questions!")

# Initialize session state variables
if 'responses' not in st.session_state:
    st.session_state['responses'] = ['How can I assist you?']

if 'requests' not in st.session_state:
    st.session_state['requests'] = []

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Initialize Gemini AI client
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    st.error("Google API key not found. Please set GOOGLE_API_KEY in your .env file.")
    st.stop()

# Initialize LLM with Gemini
try:
    # Try with the latest model name convention
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro", # Updated model name
        google_api_key=google_api_key,
        temperature=0.7
    )
except Exception as e:
    st.error(f"Error initializing Gemini AI: {str(e)}")
    
    # Show available models to help troubleshoot
    try:
        import google.generativeai as genai
        genai.configure(api_key=google_api_key)
        models = genai.list_models()
        st.error("Available models:")
        for model in models:
            st.error(f"- {model.name}")
    except Exception:
        pass
    
    st.stop()

# Create chat prompt template
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Answer the question as truthfully as possible using the provided context, "
        "and if the answer is not contained within the text below, say 'I don't know'"
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

# Create the conversation chain
chain = prompt | llm | StrOutputParser()

# Create containers for chat interface
response_container = st.container()
text_container = st.container()

# User input
with text_container:
    query = st.text_input("Query:", key="input")
    if query:
        with st.spinner("Processing..."):
            try:
                # Get conversation history
                conversation_string = get_conversation_string(st.session_state)
                
                # Refine the query
                refined_query = query_refiner(conversation_string, query)
                
                # Display refined query (optional - can be commented out)
                st.subheader("Refined Query:")
                st.write(refined_query)
                
                # Get context from vector database
                context = find_match(refined_query)
                
                # Format the input with context
                formatted_input = f"Context:\n{context}\n\nQuery:\n{query}"
                
                # Get response from LLM
                response = chain.invoke({
                    "input": formatted_input,
                    "chat_history": st.session_state['chat_history']
                })
                
                # Update session state
                st.session_state['requests'].append(query)
                st.session_state['responses'].append(response)
                
                # Update chat history
                st.session_state['chat_history'].append(HumanMessage(content=query))
                st.session_state['chat_history'].append(AIMessage(content=response))
                
                # Limit history to last 10 messages
                if len(st.session_state['chat_history']) > 10:
                    st.session_state['chat_history'] = st.session_state['chat_history'][-10:]
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Display chat history
with response_container:
    if st.session_state['responses']:
        for i in range(len(st.session_state['responses'])):
            message(st.session_state['responses'][i], key=str(i))
            if i < len(st.session_state['requests']):
                message(st.session_state["requests"][i], is_user=True, key=str(i) + '_user')