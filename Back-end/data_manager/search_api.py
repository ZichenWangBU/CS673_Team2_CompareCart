from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

# 初始化 Flask 应用
app = Flask(__name__)

# 初始化 Firebase Admin SDK
cred = credentials.Certificate("cs673comparecart-firebase-adminsdk-8la2o-8e6643de9f.json")  # 替换为你的服务账号 JSON 文件路径
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/search', methods=['GET'])
def search_items():
    try:
        collection_name = request.args.get('collection', default='items', type=str)
        keyword = request.args.get('keyword', default=None, type=str)  # 搜索关键字
        min_star = request.args.get('min_star', default=None, type=float)  # 最小星级
        min_price = request.args.get('min_price', default=None, type=float)  # 最低价格
        max_price = request.args.get('max_price', default=None, type=float)  # 最高价格
        sort_by = request.args.get('sort_by', default='price', type=str)  # 排序字段
        sort_order = request.args.get('sort_order', default='asc', type=str)  # 排序方式

        collection_ref = db.collection(collection_name)
        query = collection_ref

        if keyword:
            query = query.filter(
                field='name', op_string='>=', value=keyword
            ).filter(
                field='name', op_string='<=', value=keyword + '\uf8ff'
            )
        if min_star is not None:
            query = query.where('star', '>=', min_star)

        if min_price is not None:
            query = query.where('price', '>=', min_price)
        if max_price is not None:
            query = query.where('price', '<=', max_price)

        if sort_order.lower() == 'asc':
            query = query.order_by(sort_by, direction=firestore.Query.ASCENDING)
        elif sort_order.lower() == 'desc':
            query = query.order_by(sort_by, direction=firestore.Query.DESCENDING)

        results = query.stream()
        data = [{doc.id: doc.to_dict()} for doc in results]

        return jsonify({'status': 'success', 'data': data}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    with app.test_client() as client:
        response = client.get('/search?collection=items&min_star=4&min_price=0&max_price=15000&sort_by=price&sort_order=asc')
        print("Test 1: Search with keyword, star, and price range")
        print(response.json)

        response = client.get('/search?collection=items&keyword=iphone')
        print("\nTest 2: Search by keyword only")
        print(response.json)

        response = client.get('/search?collection=items&min_star=0&sort_by=star&sort_order=desc')
        print("\nTest 3: Filter by star and sort descending")
        print(response.json)

    app.run(debug=True)
