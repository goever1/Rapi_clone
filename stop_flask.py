#!/usr/bin/python3

from flask import Flask, request

app = Flask(__name__)

def shutdown_server():
    try:
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
    except Exception as e:
        print(f"Error shutting down server: {str(e)}")

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run()