#!/usr/bin/python3
"""A simple Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
"""The Flask application instanc"""
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """The states_list page"""
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', states=all_states)


@app.teardown_appcontext
def close_db(exc):
    """The Flask app/request context end event listener"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
