from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


# with app.app_context():
#     db.create_all()


@app.route('/add/<name>')
def add_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return {"message": f"Added {name}"}, 201


@app.route('/users')
def get_users():
    users = User.query.all()
    data = [{"id": user.id, "name": user.name} for user in users]
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)
