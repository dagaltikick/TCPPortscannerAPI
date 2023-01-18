from flask import Flask, jsonify, request, render_template
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/scan', methods=['POST'])
def scan_ports():
    host = request.form['host']
    ports = request.form.getlist('ports')
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, int(port)))
        
        if result != 0:
            open_ports.append(port)
            return render_template('out1.html')
        sock.close()
        
        
    
    return render_template('out.html',host=host,port=port)
    
 

if __name__ == '__main__':
    app.run(debug=True,port=443)