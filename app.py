from flask import Flask, request
from flask_cors import CORS
from flask_mail import Mail, Message
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 15 * 1024 * 1024

api = Api(app)
CORS(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'#'smtp.gmail.com'#'127.0.0.1:4535''mail.visionstrategie.com'
app.config['MAIL_PORT'] = 465 # Use the appropriate port for SSL 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'visionstrategie@gmail.com'#'noreply@visionstrategie.com'
app.config['MAIL_PASSWORD'] = 'wgos zjtd gmfo uubj'#'ajvg phyd ufct haqc'#'Uz2M8rHMQ5Xyfyt'
app.config['MAIL_DEFAULT_SENDER'] = 'visionstrategie@gmail.com'#'noreply@visionstrategie.com'

mail = Mail(app)


class HelloWorld(Resource):
    def get(self):
        return {'version': '1.2.0'}

class SendMailResource(Resource):
    def post(self):
        try:
            # Get data from the request JSON
            data = request.get_json()
            subject = data["subject"]
            recipient = data["recipient"]
            html_content = data["message"]

            # Create a message object
            msg = Message(subject=subject, recipients=[recipient], html=html_content, sender='visionstrategie@gmail.com')

            # Send the email
            mail.send(msg)

            return {'message': 'Email sent successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 500

api.add_resource(HelloWorld, '/')
api.add_resource(SendMailResource, '/send-mail')

if __name__ == '__main__':
    app.run() #debug=True,port=4535,host="0.0.0.0"
