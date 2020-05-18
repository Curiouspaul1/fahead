from Fahead import db,ma

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100),unique=True)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)