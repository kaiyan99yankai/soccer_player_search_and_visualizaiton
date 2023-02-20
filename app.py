from flask import Flask, request, render_template, redirect, url_for
import json
from celery import Celery

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Soccer Search Engine</h1>
    """
@app.route('/search', methods=['GET', 'POST'])
def search():
    #search page of the players
    if request.method == 'POST':
        area = request.form.get('area')
        position = request.form.get('position')
        age = request.form.get('age')
        #pass the result to the backend worker

        #should be down with celery

        #after the backend workder return the value, show that on the new template
        playerlist = {'players':[{'name': 'Kaiyan', 'x': 0, 'y': 0}]}
        return render_template('map.html', **playerlist)
    return render_template('search.html')

@app.route('/player?name=<name>')
def player(name):
    #fetch player data from the user database and render the template
    playerdata = {'name': 'Kaiyan', 'position': 'RW', 'age': 23}
    return render_template('player.html', **playerdata)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')