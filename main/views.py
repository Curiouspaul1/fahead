from Fahead.models import user_schema,users_schema,User,db
from . import api
from flask import request,jsonify,make_response,render_template

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
    recipients = [user.email for user in users]
    payload = request.get_json()
    subject = payload['subject']
    news_body = payload['body']
    with mail.connect() as conn:
        for user in users:
            msg = Message(subject=subject,sender=("Oladayo",current_app.config['MAIL_DEFAULT_SENDER']),recipients=recipients)
            #msg.body = render_template('newsletter.txt',news_body=news_body,subject=subject)
            msg.html = render_template('newsletter.html',name=user.name,news_body=news_body,subject=subject)

            try:
                conn.send(msg)
                #with app.open_resource("image.png") as fp:
                #    msg.attach("image.png", "image/png", fp.read())
            except smtplib.SMTPException:
                return make_response(jsonify({'error':'An error occurred while trying to send message'}),500)