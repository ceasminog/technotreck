from app import app
from flask import request, abort, session

# module where work with db is implemented
from module1 import db_search_users

def login_requered():
	#session.user_id

@app.route('/<string:name>/')
@app.route('/')
def index(name ="world"):
    return "Hello,{}".format(name)

@app.route('/form/', methods=['GET', 'POST'])
def form():
	if request.method == 'GET':
		return """"<html><head></head><body>
		<form method="POST" action='/form/'>
		<input name="first_name">
		<input name="last_name">
		<input type="submit">
		</form> </body></html>"""
	else:
		abort(404)

const my_id = '3413'

@jsonrpc.method('api.login')
def login():
	 db_search_users(my_id)
    return
@login_requered
@jsonrpc.method('api.search_users')
def search_users(query, limit):
    return

@jsonrpc.method('api.search_chats')
def search_chats(query, limit):
    return

@jsonrpc.method('api.list_chats')
def list_chats():
    return

@jsonrpc.method('api.create_pers_chat')
def create_pers_chat(user_id):
    return

@jsonrpc.method('api.create_group_chat')
def create_group_chat(topic):
    return

@jsonrpc.method('api.add_members_to_group_chat')
def add_members_to_group_chat(chat_id, users_id):
    return

@jsonrpc.method('api.leave_group_chat')
def leave_group_chat(chat_id):
    return

@jsonrpc.method('api.send_message')
def send_message(chat_id, content, attach_id):
    return 

@jsonrpc.method('api.read_message')
def read_message(message_id):
    return message

# new seminar //||\\ нужно придумать генерацию ключа
@jsonrpc.method('api.upload_file')
def upload_file(b64contest, filename):
content = base64.b64decode(b64content).decode('utf-8')
s3_client.put_object( )
    return b64content

@jsonrpc.method('api.downlod_file')
def downlod_file(filename):
	response = s3_client.get_object(Bucket = config.s3_BUCKET_NAME, Key=filename)
	print(response, dir(response))
	return response



