import paramiko
from flask import Flask, render_template, url_for, redirect, request, jsonify, flash, json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sys
import re

# Create a Form Class

app = Flask(__name__)
# Creating a Cross-Site Request Forgery secret key
# https://portswigger.net/web-security/csrf
app.config['SECRET_KEY'] = "AJsanner%3oAAa0000sAjjf9e22AAal"

current_input = ""


class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


CLIENT = '192.168.0.11'
MAC = '38:8C:50:26:DD:51'


def do_command(command):
    print(f'doing command {command}')
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('192.168.0.101', username='pi',
                   password='underappleoverchair')
    print('starting command execution')

    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(command)
    # ssh_stdin_test, ssh_stdout_test, ssh_stderr_test = client.exec_command(
    #     f'webostv app get-id {CLIENT} {MAC}')

    ssh_stdout.channel.set_combine_stderr(True)
    output = ssh_stdout.read().decode()

    ssh_stdin.close()
    ssh_stdout.close()
    ssh_stderr.close()
    client.close()
    return output


def get_command_string(command_type, command):
    with open('device_capabilities.json', 'r') as read_file:
        device_capabilities = json.load(read_file)
        try:
            command_string = device_capabilities[command_type][command]
            return command_string
        except (KeyError) as e:
            return e


@app.route('/')
def index():
    startup_command = f"webostv pair {CLIENT} {MAC}"
    print(do_command(startup_command))
    # startup_command = f"webostv app get-id {CLIENT} {MAC}"
    # if curr_input == "":
    #     current_input = do_command(startup_command)
    #     print(current_input)
    return render_template('index_b.html')


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form submitted successfully.")

    return render_template("learning_wtf.html",
                           name=name,
                           form=form)


@app.route('/changeinput/', methods=['GET', 'POST'])
def set_input():
    if request.method == 'POST':
        if request.form.get('inputs') is not None:
            user_command = request.form.get('inputs').lower()
            command_string = get_command_string('inputs', user_command)
            input_string = f"webostv app launch {CLIENT} {MAC} {command_string}"
            do_command(input_string)

        elif request.form.get('volume') is not None:
            print('volume clicked')
        elif request.form.get('power') is not None:
            user_command = request.form.get('power').lower()
            command_string = get_command_string('power', user_command)
            input_string = f'webostv power {command_string} {CLIENT} {MAC}'
    elif request.method == 'GET':
        return render_template('index_b.html')
    else:
        return '2'  # render_template('index_b.html')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
