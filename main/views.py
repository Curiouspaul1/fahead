from flask_mail import Message
from flask import request,jsonify,make_response,render_template,current_app
import smtplib
from Fahead.models import user_schema,users_schema,User,db
from Fahead import mail
from . import api

@api.route('/register',methods=['POST'])
def register():
    payload = request.get_json(force=True)
    user = User(name=payload['name'],email=payload['email'])

    db.session.add(user)
    db.session.commit()

    return make_response(jsonify({'msg':'registered user successfully'}),200)

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