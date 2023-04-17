from flask import Flask, request, send_from_directory, jsonify, g
import sqlite3 as sql
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
import math, sys, os, json
import numpy as np
from flask_cors import CORS
from scipy.spatial.distance import euclidean
from scipy.spatial import cKDTree
from flask.json import JSONEncoder


DATABASE = './players_20.db'

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        return super().default(obj)

def connect_db():
    return sql.connect(DATABASE)

def get_connection():
    db = getattr(g, '_db', None)
    if db is None:
        db = g._db = connect_db()
    return db

goalkeeper_attributes = ['Aerial Reach', 'Command of Area', 'Communication', 'Eccentricity', 'First Touch', 'Handling', 'Kicking', 'One on Ones', 'Passing', 'Punching (Tendency)', 'Reflexes', 'Rushing Out (Tendency)', 'Throwing']
technical_attributes = ['Corners', 'Crossing', 'Dribbling', 'Finishing', 'First Touch', 'Free Kick Taking', 'Heading', 'Long Shots', 'Long Throws', 'Marking', 'Passing', 'Penalty Taking', 'Tackling', 'Technique']
physical_attributes = ['Acceleration', 'Agility', 'Balance', 'Jumping Reach', 'Natural Fitness', 'Pace', 'Stamina', 'Strength']
mental_attributes = ['Aggression', 'Anticipation', 'Bravery', 'Composure', 'Concentration', 'Decisions', 'Determination', 'Flair', 'Off the Ball', 'Positioning', 'Teamwork', 'Vision', 'Work Rate']
player_information_attributes = ['Name', 'Position', 'Club', 'Division', 'Based', 'Nation','Height', 'Weight', 'Age', 'Preferred Foot', 'Best Pos', 'Best Role','Value', 'Wage']
margin_ratio_for_name = 1.2

def create_visualization(value_down, value_up, position, font_size):
    conn = sql.connect(DATABASE)
    df = pd.read_sql_query("SELECT * FROM player WHERE Value BETWEEN {} AND {} AND is{} = 1".format(str(value_down), str(value_up), position), conn)
    conn.close()
    player_information = df[player_information_attributes]
    if position == "GK":
        player_attributes = df[goalkeeper_attributes + physical_attributes + mental_attributes]
    else:
        player_attributes = df[technical_attributes + physical_attributes + mental_attributes]
    pca = PCA()
    pipe = Pipeline(steps=[    
        ('scaling',StandardScaler()),
        ('pca',PCA(n_components=2))
    ])
    player_attributes_pca = pipe.fit_transform(player_attributes)
    pca1 = np.array([point[1] for point in player_attributes_pca])
    pca0 = np.array([point[0] for point in player_attributes_pca])
    print(pipe['pca'].explained_variance_ratio_)
    canvas_width = 2000
    canvas_height = 16000
    pca1 -= np.min(pca1)
    pca0 -= np.max(pca0)
    pca0 = -pca0
    points_0 = canvas_width/(np.max(pca1) - np.min(pca1)) * pca1
    points_1 = canvas_height/(np.max(pca0) - np.min(pca0)) * pca0
    player_information['point0'] = points_0
    player_information['point1'] = points_1
    players = player_information.to_dict()
    data = {
        "canvas_width": canvas_width,
        "canvas_height": canvas_height,
        "players": players,
    }
    return data

def graph_visualization(value_down, value_up, position, font_size):
    conn = sql.connect(DATABASE)
    df = pd.read_sql_query("SELECT * FROM player WHERE Value BETWEEN {} AND {} AND is{} = 1".format(str(value_down), str(value_up), position), conn)
    conn.close()
    player_information = df[player_information_attributes]
    if position == "GK":
        player_attributes = df[goalkeeper_attributes + physical_attributes + mental_attributes]
    else:
        player_attributes = df[technical_attributes + physical_attributes + mental_attributes]
    pca = PCA()
    pipe = Pipeline(steps=[    
        ('scaling',StandardScaler()),
        ('pca',PCA(n_components=2))
    ])
    player_attributes_pca = pipe.fit_transform(player_attributes)
    pca1 = np.array([point[1] for point in player_attributes_pca])
    pca0 = np.array([point[0] for point in player_attributes_pca])
    print(pipe['pca'].explained_variance_ratio_)
    canvas_width = 2000
    canvas_height = 16000
    pca1 -= np.min(pca1)
    pca0 -= np.max(pca0)
    pca0 = -pca0
    points_0 = canvas_width/(np.max(pca1) - np.min(pca1)) * pca1
    points_1 = canvas_height/(np.max(pca0) - np.min(pca0)) * pca0
    player_information['point0'] = points_0
    player_information['point1'] = points_1
    player_information['nei'] = None
    # 计算每个玩家与其他玩家之间的距离，并将最近的五个玩家的索引保存到 'nei' 列表中
    points = player_information[["point0", "point1"]].values
    tree = cKDTree(points)
    for index, player in player_information.iterrows():
        _, nearest_indices = tree.query(points[index], k=6)  # k=6 因为包含自己在内的最近6个点
        nearest_indices = nearest_indices[1:]  # 去掉自己（第一个元素）
        player_information.at[index, "nei"] = list(nearest_indices)

    players = player_information.to_dict()
    data = {
        "canvas_width": canvas_width,
        "canvas_height": canvas_height,
        "players": players,
    }
    return data

app = Flask(__name__, static_folder="dist/static", template_folder="dist")
app.json_encoder = CustomJSONEncoder

CORS(app, origins="http://localhost:8080")

class NumpyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NumpyJSONEncoder, self).default(obj)

@app.route("/node", methods=['GET', 'POST'])
def node():
    if request.method == 'POST':
        #search page of the players
        bot = int(request.json.get('bottom'))
        top = int(request.json.get('top'))
        position = request.json.get('position')
        data = create_visualization(bot, top, position, 12)
        return jsonify(data)
    
    return catch_all('')

@app.route("/similarity", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #search page of the players
        bot = int(request.json.get('bottom'))
        top = int(request.json.get('top'))
        position = request.json.get('position')
        data = graph_visualization(bot, top, position, 12)
        return jsonify(data)
    
    return catch_all('')

@app.route("/player", methods=["POST"])
def player():
    #fetch player data from the user database and render the template
    name = request.json.get('name')
    age = request.json.get('age')
    db = get_connection()
    cur = db.cursor()
    cur.execute('SELECT * FROM player WHERE name=(?) AND age=(?)', [name, age])
    res = cur.fetchone()
    col_name_list = [tuple[0] for tuple in cur.description]
    playerdata = {}
    for i in range(1, len(col_name_list)):
        playerdata[col_name_list[i]] = res[i]
        print(res[i])
    return jsonify(playerdata)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    if path.startswith("static/") and os.path.isfile("dist/" + path):
        return send_from_directory("dist", path)
    else:
        return send_from_directory("dist", "index.html")


if __name__ == "__main__":
    app.run()