import os
from flask import Flask, render_template, redirect, url_for, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.form['username']
    password = request.form['password']
    host_ip = os.getenv('HOST_IP')
    private_key_path = os.getenv('PRIVATE_KEY_PATH')

    if username and password and host_ip and private_key_path:
        subprocess.run([
            'ansible-playbook', 
            '/app/create_user.yml', 
            '-i', f'{host_ip},',  
            '--private-key', private_key_path,
            '-e', f'username={username} password={password}'
        ], check=True)
        return redirect(url_for('index'))
    return 'Failed to create user', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
