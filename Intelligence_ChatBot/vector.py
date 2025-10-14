from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

file_path ='../EmmaAIProjects/Intelligence_ChatBot/Kaggle_DataSet/amazon_products_sales_data_cleaned.csv' 

df = pd.read_csv(file_path)
#df = pd.read_csv("amazon_products_sales_data_cleaned.csv")
embeddings = OllamaEmbeddings(model ="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)


if add_documents:
    documents =[]
    ids =[]

    for i, row in df.iterrows():
        document =Document(
            content = str(row["product_title"]) + " " +str(row["product_rating"]) + " " + str(row["total_reviews"]) + " "+ str(row["purchased_last_month"]),
            metadata={"discounted_price":row["discounted_price"], "original_price" :row["original_price"],"is_best_seller" :row["is_best_seller"], "is_sponsored": row["is_sponsored"],"has_coupon": row["has_coupon"],
                      "buy_box_availability" :row["buy_box_availability"],"delivery_date" : row["delivery_date"],"sustainability_tags" : row["sustainability_tags"],
                      "product_image_url" : row["product_image_url"],"product_page_url" : row["product_page_url"],"date":row["data_collected_at"], "product_category": row["product_category"], "discount_percentage": row["discount_percentage"]},
            id = str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="amazon_products_sales_data_cleaned",
    persist_directory = db_location,
    embedding_function =embeddings
)

if add_documents:
    vector_store.add_documents(documents =documents, ids =ids)

retriever = vector_store.as_retriever(
    search_kwargs ={"k" : 5}
)
