from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///name.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Defines a blueprint of the table


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(99), nullable=False)


# Done once, creates DB
with app.app_context():
    db.create_all()


@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": f"User '{new_user.name}' added"}), 201


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data['name']
    db.session.commit()
    return jsonify({"message": f"User {id} updated to '{user.name}'."})


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"User {id} deleted."})


if __name__ == '__main__':
    app.run(debug=True)


# curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Zero\"}" http://127.0.0.1:5000/users

# curl http://127.0.0.1:5000/users

# curl -X PUT -H "Content-Type: application/json" -d "{\"name\":\"Zer0x\"}" http://127.0.0.1:5000/users/1

# curl -X DELETE http://127.0.0.1:5000/users/1
