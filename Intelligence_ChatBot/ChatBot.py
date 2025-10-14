#setting up the chat prompting to users to ask questions continuously

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
# Ensure your 'vector.py' is accessible and defines 'retriever'
from vector import retriever


# --- Configuration ---
model = OllamaLLM(model="llama3.2")

# assign task to the business intelligence chat bot
template = """
You are an expert in answering questions about amazon products sales.
Here are some relevant reviews: {file_path}
Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# --- Interactive Q&A Loop ---
while True:
    print("-----------------------------------------")
    question = input("Ask your question (q to quit): ")
    
    if question.lower() == "q": 
        print("\n....Exiting Q&A session....\n")
        break

    print ("\n...Thinking...\n")    

    
    # 1. Retrieve Data
    # Ensure you are passing the correct variable to the 'file_path' key
    reviews = retriever.invoke(question)  
    
    # 2. Invoke Chain
    # Use the exact keys defined in the template: 'file_path' and 'question'
    result = chain.invoke({
        "file_path": reviews,  # Retrieved document
        "question": question   # User's question 
    }) 

    # 3. Print Response
    print("------------------RESPONSE-----------------------")
    print(result) 
    print("--------------------\n")
