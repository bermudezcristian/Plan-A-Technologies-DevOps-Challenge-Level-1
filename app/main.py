from flask import Flask, request, jsonify
import os
import datetime;
import socket
import platform


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Getting TimeStamp
    timestamp = str(datetime.datetime.now())
    # Getting HostName
    hostname = str(socket.gethostname())
    # Getting Engine Version
    system = platform.system()
    release = platform.release()
    version = platform.version()
    engine = system + " " + release + " " + version
    # Gettint Visitor IP
    visitor_ip = str(request.remote_addr)
    return jsonify({'timestamp': timestamp, 'hostname': hostname, 'engine': engine, 'visitor ip': visitor_ip}), 200

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=str(os.environ.get('DEBUG',True)),host='0.0.0.0', port=port) 