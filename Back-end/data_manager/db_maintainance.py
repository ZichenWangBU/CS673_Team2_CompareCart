import firebase_admin
from firebase_admin import credentials, firestore
import random
import string
import re

cred = credentials.Certificate("cs673comparecart-firebase-adminsdk-8la2o-c86686395c.json")

def add_word_to_documents(collection_ref,field_name,value):
    docs = collection_ref.stream()
    for doc in docs:
        collection_ref.document(doc.id).update({
            field_name:value
        })

def rename_field(collection_ref,old_name,new_name):
    docs=collection_ref.stream()
    for doc in docs:
        doc_data=doc.to_dict()
        if old_name in doc_data:
            field_value=doc_data[old_name]
            collection_ref.document(doc.id).update({old_name:field_value})
            print(f"creating {new_name} in document {doc.id}")
            collection_ref.document(doc.id).update({new_name:firestore.DELETE_FIELD})
            print(f"deleted {old_name} in document {doc.id}")

def generate_keywords(title):
    if not title:
        return []
    words = re.split(r'[,\.\s]+', str(title).lower())
    return list(set(filter(None, words)))

def update_documents_with_keywords(collection_ref):
    documents = collection_ref.stream()

    for doc in documents:
        doc_data = doc.to_dict()
        title = doc_data.get("title", "")
        keywords = generate_keywords(title)  # Generate keywords

        # Update the document with the new 'keywords' field
        collection_ref.document(doc.id).update({"keywords": keywords})
        print(f"Updated document {doc.id} with keywords: {keywords}")



def generate_random_str(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_random_doc(collection_ref, num_docs):
    for i in range(num_docs):
        doc_data = {
            "field1": generate_random_str(8),
            "field2": generate_random_str(12),
            "field3": generate_random_str(16)
        }
        doc_ref = collection_ref.document()  # Auto-generate document ID
        doc_ref.set(doc_data)
        print(f"Added document {i + 1}: {doc_data}")

if __name__ == "__main__":
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    coll_ref=db.collection("Items")
    update_documents_with_keywords(coll_ref)