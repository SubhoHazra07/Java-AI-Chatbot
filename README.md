# AI-Powered Java Chatbot

# Pookie Chatbot

![Screenshot 2025-03-13 184712](https://github.com/user-attachments/assets/79394e30-13f6-4bc8-8440-a2cbee42f0af)


---

## Table of Contents

## 1. Introduction  
## 2. Project Overview  
## 3. Tech Stacks  
## 4. Features  
## 5. Architecture  
## 6. Installation and Setup  
## 7. Usage  
## 8. Deployment  
## 9. Conclusion  
## 10. Acknowledgements  
## 11. References  

---

## Introduction

Pookie Chatbot is an AI-powered conversational assistant designed to provide intelligent responses to user queries. It leverages advanced natural language processing (NLP) techniques and integrates with Google Gemini AI for enhanced interaction. The chatbot is built using Streamlit for the frontend and utilizes Pinecone for efficient vector search operations.

## Project Overview

The Pookie Chatbot project aims to create a Java-based AI chatbot that seamlessly integrates structured query processing with natural language understanding. It refines user inputs, retrieves relevant context from a vector database, and generates accurate responses using Google Gemini AI. The chatbot supports Java Queries for processing structured data-based queries, enabling it to interact with databases and execute specific commands effectively. With its advanced NLP capabilities, it maintains a dynamic conversation history to enhance user experience and response accuracy.

## Tech Stacks

- **Python**: The primary programming language used for developing the chatbot and integrating various components.  
- **NLP (Natural Language Processing)**: Employed to analyze and understand user input, allowing the chatbot to provide relevant responses.  
- **NLTK (Natural Language Toolkit)**: Used for text processing, tokenization, vectorization, and language analysis.  
- **Streamlit**: Enables users to interact with the chatbot through a user-friendly web interface.  
- **Langchain**: Enhances the chatbot's language capabilities.  
- **Google Gemini API**: Integrated to provide advanced language processing capabilities.  
- **Pinecone (Vector Store)**: Utilized for efficient storage and retrieval of vectorized data.  
- **GitHub**: The project is maintained in a private repository for version control and collaboration.  

## Features

- **Question Answering**: Provides precise and context-aware answers to Java-related queries.  
- **Explanation Generation**: Generates detailed explanations for complex Java concepts.  
- **Interactive Conversations**: Engages users with a natural and dynamic conversation flow.  
- **Personalization**: Adapts to user preferences and maintains context.  
- **Multi-Modal Interface**: Supports text-based interactions with potential expansion to code snippet generation.  
- **Advanced Language Capabilities**: Handles complex Java-related queries, multi-turn conversations, contextual reasoning, and sentiment-based responses.  

## Architecture

1. **User Input**: Users ask Java-related questions through the Streamlit-based web interface.  
2. **Query Processing**: The chatbot understands the user's question using NLP and breaks it down into meaningful components.  
3. **Text Chunking**: Relevant Java-related reference materials (PDFs, documentation, etc.) are split into smaller text chunks.  
4. **Embedding Generation**: Each chunk is converted into vector embeddings using Sentence Transformers.  
5. **Vector Storage & Retrieval**: The embeddings are stored in Pinecone, allowing for fast and accurate retrieval of relevant documents.  
6. **Contextual Search**: When a user asks a question, the chatbot retrieves the most relevant text chunks from Pinecone.  
7. **Response Generation**: The chatbot sends the retrieved context to Google Gemini AI, which formulates a structured and relevant response.  
8. **Answer Presentation**: The chatbot presents the answer in an easy-to-understand format.  
9. **Session Management**: The chatbot maintains a conversation history, allowing users to ask follow-up questions.  
10. **Continuous Improvement**: The chatbot refines its responses over time by analyzing user interactions.  

## Installation and Setup

1. Clone the repository from GitHub:  
   ```sh
   git clone https://github.com/SubhoHazra07/Java-AI-Chatbot.git
   ```
2. Install the required dependencies:  
   ```sh
   pip install -r requirements.txt
   ```
3. Set up Pinecone and create a vector store for Java concepts.  
4. Obtain API keys for Pinecone and Gemini API.  
5. Replace the API keys in the `.env` file:  
   ```sh
   GOOGLE_API_KEY=your_google_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   ```
6. Run the chatbot using:  
   ```sh
   streamlit run main.py
   ```

## Usage

- **Streamlit App**: [Pookie Chatbot](https://pookie-chatbot.streamlit.app/)  
- **GitHub Repository**: [Java-AI-Chatbot](https://github.com/SubhoHazra07/Java-AI-Chatbot.git)  

### Using GitHub:

1. Clone the repository:  
   ```sh
   git clone https://github.com/SubhoHazra07/Java-AI-Chatbot.git
   ```
2. Navigate to the project folder and run:  
   ```sh
   streamlit run main.py
   ```
3. Access the chatbot via a web browser.  

## Deployment

1. **Push the code** to a public GitHub repository.  
2. **Set Up Secret Keys** instead of uploading `.env` file.  
3. **Deploy the Application**:  
   - Click "New App" on Streamlit Cloud.  
   - Select the GitHub repository where your chatbot is stored.  
   - Choose the main script file (`main.py`).  
   - Click "Deploy."  
4. Once deployed, access the chatbot via the Streamlit link.  

## Conclusion

Pookie Chatbot is an AI-powered assistant that helps users with Java-related queries using NLP, Google Gemini AI, and Pinecone for fast, accurate responses. The chatbot improves over time and has potential for future upgrades.  

## Acknowledgments

We thank all contributors and the open-source community for supporting the frameworks used in this project.  

## References

- [NLTK Documentation](https://www.nltk.org/)  
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [Langchain Documentation](https://langchain.ai/docs/)  
- [Google Gemini API Documentation](https://ai.google.dev/gemini-api/docs)  
- [Pinecone Documentation](https://www.pinecone.io/docs/)  
- [Streamlit Cloud Deployment](https://docs.streamlit.io/deploy/streamlit-community-cloud)  
- [Programming with Java](https://iasyc.in/download/book/Programming_With_Java_A_primer_3e_by_balagurusamy.pdf)  
- [Java Notes](https://www.iitk.ac.in/esc101/share/downloads/javanotes5.pdf)  

---

### Demo Chat with Pookie🎀  
Try out the chatbot and enhance your Java learning experience!

<p align="center">
  <img src="https://github.com/user-attachments/assets/6da51d22-8b42-4ec0-932a-98175c2764be" alt="Image 1" width="45%"/>
  <img src="https://github.com/user-attachments/assets/236dc3aa-8bf5-4464-9b76-e48d0b912e1c" alt="Image 2" width="45%"/>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/5df147e5-2fd3-4421-8046-7d2572ececee" alt="Image 1" width="45%"/>
  <img src="https://github.com/user-attachments/assets/9e2f1055-5e5d-4174-932f-747571a5bd7c" alt="Image 2" width="45%"/>
</p>




