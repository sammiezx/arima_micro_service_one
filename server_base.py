# from flask import Flask, request, jsonify
# import controller

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return jsonify({"status": "success", "code": 200, "message": "success", "data": "HELLO!!!"}), 200

# @app.route('/submit', methods=['POST'])
# def submit():
#     try:
#         data = request.json
#         user = data['user']
#         image = data['image']
#         text = data['text']
#         response = controller.submit(user, image, text)
#         return jsonify({"status": "success", "code": 200, "message": "success", "data": response}), 200
#     except KeyError as e:
#         return jsonify({"status": "error", "code": 400, "message": f"Missing required field: {e}", "data": None}), 400
#     except Exception as e:
#         return jsonify({"status": "error", "code": 500, "message": str(e), "data": None}), 500
    

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


