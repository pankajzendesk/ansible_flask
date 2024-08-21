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
    if username and password:
        # Call the Ansible Playbook using the subprocess module
        subprocess.run(
            ['ansible-playbook', '/app/create_user.yml', '-e', f'username={username} password={password}'],
            check=True
        )
        return redirect(url_for('index'))
    return 'Failed to create user', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
