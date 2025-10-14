# LLM-Powered Business Intelligence ChatBot

## Objective: Develop a Chatbot that can answer business intelligence and data-related questions by querying a sample database using natural language processing

### Introduction
In Many Organizations, accessing specific data insights requires knowledge of complex questy language like SQL or Kusto(KQL). This project aims to simplify this process by creating a conversational interface that allows anyone to ask a question and receive a data-driven answer.

### Key Features: 
  #Front-end: interface for user input
  #Back-end:Receive user's questions
  #Integration: LLM to convert natural language questions into SQL or KQL queries
  #Execution: Generate query againts a sample database
  #Output: PResentation of the result back to the user in a readable format

### How it works
A user enter a question into the chat interface
The frontend sends the requestion to the python backend
The backend calls the LLM API, providing the user's questions and a prompt that instructs the model on how to generate a database query
the LLM return the generated query
The backend executes the query against the database
The result is formatted and returned to the frontend, which displays the answer to the user

### Methodologies
Code: python
LLM Integration: llama 3.2
RAG: retrieved from vector database 
Data Source: from Kaggle csv file amazon product sales
  
  

## 📦 Amazon Product Sales Q&A Chatbot
This project implements a Retrieval-Augmented Generation (RAG) pipeline that allows users to ask continuous questions about Amazon product sales and reviews. The chatbot uses a local Large Language Model (LLM) powered by Ollama and retrieves relevant context from a local vector database.

### ✨ Features
Continuous Q&A: Engage in a persistent chat session until explicitly quitting.

Local LLM Integration: Uses the llama3.2 model via Ollama, ensuring privacy and local execution.

Retrieval-Augmented Generation (RAG): Answers are grounded in actual product review data retrieved from a vector database for factual accuracy.

Modular Design: Separates the vector database/retrieval logic (vector.py) from the application logic.

### 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

***Python 3.8+***

***LLM Integration : Ollama - llama3.2** from the local LLM server

***Dependencies: Required Python libraries include "pandas", langchain-core, langchain-ollama***

***Data Source: kaggle.*** amazon product sales csv file


### ⚙️ Setup and Installation

**Step 1:Install Ollama and Download the Model**

You must have the Ollama server running locally.

Install Ollama: Follow the instructions on the Ollama website for your operating system (macOS, Linux, or Windows).

Pull the Model: Open your terminal or command prompt and download the required model:

ollama pull llama3.2

**Step 2: Install Python Dependencies**

Navigate to your project directory and install the necessary libraries, including pandas for data handling and the LangChain components.

pip install pandas langchain langchain-core langchain-ollama

(Note: If your vector store requires other libraries like chromadb or faiss, you must install those as well.)

**Step 3: Data and Vector Database Setup**

This chatbot relies on two files that are built in our project environment:

**file_path (CSV):** original Amazon product sales data file (e.g., amazon_products_sales_data.csv).

**vector.py:** This file must contain the logic to load the data from file_path, create a vector store, and define the retriever object, which is then imported into the main chatbot script.

Best practice: Ensure your vector.py script is executed at least once to create and persist the vector database before running the chatbot.

**Step 4: ChatBot Python Script**

Once the data and retriever are set up, import your dependencies and write python script 

### ▶️ Usage
Start the Chatbot: Run the main Python script (First make sure you've saved the primary application code, for example as chatbot.py):

python chatbot.py

Interact: The terminal will prompt you to ask questions continuously.

-----------------------------------------
Ask your question (q to quit): What are currently the top 2 rated products?


-------RESPONSE--------

[The Llama 3.2 generated answer based on retrieved reviews.]
--------------------

-----------------------------------------
Ask your question (q to quit): What is the average price of the high-rated items?

...Thinking...
#### ... and so on

**Exit: To end the session, type q and press Enter.**
