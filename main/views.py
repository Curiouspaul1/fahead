from Fahead.models import user_schema,users_schema,User,db
from . import api
from flask import request,jsonify,make_response

@api.route('/register',methods=['POST'])
def register():
    payload = request.get_json()
    user = User(name=payload['name'],email=payload['email'])

    db.session.add(user)
    db.session.commit()

    return make_response(user_schema.jsonify(user),200)

@api.route('/users',methods=['GET'])
def users():
    all_users = User.query.all()
    return jsonify(users_schema.dump(all_users))