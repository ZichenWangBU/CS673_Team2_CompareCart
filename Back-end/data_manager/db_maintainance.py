import firebase_admin
from firebase_admin import credentials, firestore

# Initialize the Firestore client
cred = credentials.Certificate("C:/Users/wyf20/CS673_Team2_CompareCart/Back-end/Real-time search/cs673comparecart-firebase-adminsdk-8la2o-84029a7194.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Define the name of the collection
collection_name = "Items"

# Add new word to each document in the collection
def add_word_to_documents():
    docs = db.collection(collection_name).stream()

    for doc in docs:
        # Update each document to add the new field
        db.collection(collection_name).document(doc.id).update({
            'category': "Smartphone"
        })

if __name__ == "__main__":
    add_word_to_documents()