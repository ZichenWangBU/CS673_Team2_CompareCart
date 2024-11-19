from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import FieldFilter

# 初始化 Flask 应用
app = Flask(__name__)

# 初始化 Firebase Admin SDK
cred = credentials.Certificate("cs673comparecart-firebase-adminsdk-8la2o-8e6643de9f.json")  # 替换为你的服务账号 JSON 文件路径
firebase_admin.initialize_app(cred)
db = firestore.client()

# API Endpoint to query Firestore dynamically
@app.route('/search_items', methods=['GET'])
def search_items():
    try:
        # Get parameters from the request
        keyword = request.args.get('keyword', default='', type=str)
        min_price = request.args.get('min_price', default=0, type=float)
        max_price = request.args.get('max_price', default=float('inf'), type=float)
        min_stars = request.args.get('min_stars', default=0, type=int)
        max_stars = request.args.get('max_stars', default=100, type=int)
        order_by = request.args.get('order_by', default='price', type=str)
        direction = request.args.get('direction', default='desc', type=str)
        lim=request.args.get('limit', default=10, type=int)
        # Query Firestore
        items_ref = db.collection('Items')
        query = (
            items_ref
            #.where("title", ">=", keyword)
            #.where("title", "<", keyword+"\uF8FF")
            .where('price', '>=', min_price)
            .where('price', '<=', max_price)
            .where('star', '>=', min_stars)
            .where('star', '<=', max_stars)
            .limit(lim)
            .select(('title','store','price','star','img_reference'))
        )
        # Apply order by
        if direction.lower() == 'desc':
            query = query.order_by(order_by, direction=firestore.Query.DESCENDING)
        else:
            query = query.order_by(order_by, direction=firestore.Query.ASCENDING)
        docs = query.stream()
        results = [{'id': doc.id, **doc.to_dict()} for doc in docs]
        return jsonify(results), 200
    except:
        return jsonify({'error': 'No result found'})

@app.route('/search_items', methods=['GET'])
def item_details():
    try:
        # Get parameters from the request
        keyword = request.args.get('keyword', default='', type=str)
        items_ref = db.collection('Items')
        query = (
            items_ref
            .where("title", "==", keyword)
            .select(('title','store','price','star','img_reference','commentNum','detail_url'))
        )
        # Apply order by
        docs = query.stream()
        results = [{'id': doc.id, **doc.to_dict()} for doc in docs]
        return jsonify(results), 200
    except:
        return jsonify({'error': 'No result found'})

def item_comparison():
    try:
        # Get parameters from the request
        keywords = request.args.get('keywords', default='', type=str)
        items_ref = db.collection('Items')
        results=[]
        for keyword in keywords:
            query = (
            items_ref
            .where("title", "==", keyword)
            .select(('title','store','price','star','img_reference','commentNum',))
            )
            doc=query.stream().to_dict()
            results.append(doc)

        return jsonify(results), 200
    except:
        return jsonify({'error': 'No result found'})


# Main function to test the API
if __name__ == '__main__':
    with app.test_request_context(query_string={
        'keyword': 'iPhone',
        'min_price': 0,
        'max_price': 100000,
        'min_stars': 0,
        'max_stars': 5,
        'order_by': 'price',
        'direction': 'desc'
    }):
        # Simulate a request to the API
        response = search_items()

        # Extract JSON from the response tuple
        json_response = response[0].get_json() if isinstance(response, tuple) else response.get_json()

        print(json_response)  # Print the results to the console

    # Run the Flask server
    app.run(debug=True)