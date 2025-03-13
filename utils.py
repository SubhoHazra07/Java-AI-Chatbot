from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import os
from dotenv import load_dotenv
import google.generativeai as genai
import traceback

# Load environment variables
load_dotenv()

# Initialize Google Gemini API
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

# Initialize sentence transformer model
model = SentenceTransformer('all-MiniLM-L12-v2')

# Initialize Pinecone client
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=pinecone_api_key)

# Get the index
index_name = 'pookie-chatbot'
index = pc.Index(index_name)

def find_match(input_query):
    """
    Find matching context from Pinecone vector database
    """
    try:
        # Encode the input query
        input_embedding = model.encode(input_query).tolist()
        
        # Query Pinecone
        result = index.query(
            vector=input_embedding,
            top_k=2,
            include_metadata=True
        )
        
        # Extract and combine the text from the top 2 results
        if result.get('matches'):
            context = result['matches'][0]['metadata']['text']
            if len(result['matches']) > 1:
                context += "\n\n" + result['matches'][1]['metadata']['text']
            return context
        else:
            return "No relevant information found."
    except Exception as e:
        return f"Error retrieving context: {str(e)}"

def query_refiner(conversation, query):
    """
    Refine the user query based on conversation history using Gemini
    """
    try:
        # Try to get available models
        available_models = [model.name for model in genai.list_models()]
        
        # Choose the appropriate model based on availability
        if "gemini-1.5-pro" in available_models:
            model_name = "gemini-1.5-pro"
        elif "gemini-pro" in available_models:
            model_name = "gemini-pro"
        else:
            # Use the first available text model if neither preferred model is available
            for model_info in genai.list_models():
                if "generateContent" in model_info.supported_generation_methods:
                    model_name = model_info.name
                    break
            else:
                # If no suitable model is found, fall back to the original query
                return query
        
        # Initialize the Gemini model
        generation_config = {
            "temperature": 0.7,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 256,
        }
        
        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=generation_config
        )
        
        prompt = f"""Given the following user query and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base.

CONVERSATION LOG: 
{conversation}

Query: {query}

Refined Query:"""

        response = model.generate_content(prompt)
        
        return response.text.strip()
    except Exception as e:
        # Print detailed error for debugging
        print(f"Error in query_refiner: {str(e)}")
        print(traceback.format_exc())
        # Return original query if refinement fails
        return query

def get_conversation_string(session_state):
    """
    Get conversation history as a string
    """
    conversation_string = ""
    for i in range(len(session_state['responses']) - 1):
        if i < len(session_state['requests']):
            conversation_string += "Human: " + session_state['requests'][i] + "\n"
            conversation_string += "Bot: " + session_state['responses'][i + 1] + "\n"
    return conversation_string