from flask_mail import Message
from flask import request,jsonify,make_response,render_template,current_app
from sqlalchemy.exc import IntegrityError
from Fahead.models import user_schema,users_schema,User,db
from Fahead.main.extensions import isNameValid,emailcheck
from Fahead import mail
from . import api
import smtplib

@api.route('/register',methods=['POST'])
def register():
    payload = request.get_json(force=True)
    if not isNameValid(payload['name']):
        return make_response(jsonify({"code":"error","fields":{"name":"invalid name sequence","email":"invalid email sequence"}}),400)
    elif not emailcheck(payload['email']):
        return make_response(jsonify({"code":"error","fields":{"name":"invalid name sequence","email":"invalid email sequence"}}),400)
    try:
        user = User(name=payload['name'],email=payload['email'])
        db.session.add(user)
        db.session.commit() # if error unique constraint fails upon commiting - the Integrity error is raised
    except IntegrityError as e:
        return make_response(jsonify({"code":"error","msg":"User with email already exists"}),400)
        raise e

    return make_response(jsonify({'code':'ok'}),200)

@api.route('/users',methods=['GET'])
def users():
    all_users = User.query.all()
    return jsonify(users_schema.dump(all_users))


@api.route('/send_newsletter',methods=['GET','POST'])
def send_newsletter():
    users = User.query.all()
    subscribers = [user.email for user in users]
    payload = request.get_json()
    mail_subject = payload['subject']
    news_body = payload['body']
    #msg.body = render_template('newsletter.txt',news_body=news_body,subject=subject)
    with mail.connect() as conn:
        for user in users:
            msg = Message(sender=("Oladayo",current_app.config['MAIL_DEFAULT_SENDER']),recipients=[user.email])
            msg.subject = mail_subject.replace("[[firstname]]", "{}".format(user.name.split(' ')[0]))
            msg.html = render_template('newsletter.html',name=user.name,news_body=news_body,subject=mail_subject.replace("[[firstname]]","{}".format(user.name.split(' ')[0])))
            try:
                conn.send(msg)
                #with app.open_resource("image.png") as fp:
                #    msg.attach("image.png", "image/png", fp.read())
            except smtplib.SMTPException:
                return make_response(jsonify({'error':'An error occurred while trying to send message'}),500)
        return jsonify({'msg':'Mail sent successfully'}),200