from flask import Flask, request, jsonify
app = Flask(__name__)

# In-memory "database"
users = {}

# Home route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the User REST API with Flask!"})

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET a single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user})
    return jsonify({"error": "User not found"}), 404

# POST - Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = {
        "name": data.get("name"),
        "email": data.get("email")
    }
    return jsonify({"message": "User created", "user": users[user_id]}), 201

# PUT - Update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])
    return jsonify({"message": "User updated", "user": users[user_id]})

# DELETE - Remove user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted_user})

if __name__ == "__main__":
    app.run(debug=True)
