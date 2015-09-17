from flask import Flask, request
from flask_sockets import Sockets
#accessible from remote: gunicorn -k flask_sockets.worker hello:app -b :8888
#install: pip install Flask-Sockets gunicorn
app = Flask(__name__, static_url_path='/static')
@app.route('/')
def root():
        return app.send_static_file('index.html') 
sockets = Sockets(app)
@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
