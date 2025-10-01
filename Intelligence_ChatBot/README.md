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
the LLM retuen the generated query
The backend esecutes the query againts the database
The result is formatted and returned to the frontend, which displays the answer to the user

### Methodologies
Frontend: 
Backend:
LLM Integration: API Calls to model [xx]
Database:
Data Source:
  
  

