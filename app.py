# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'NHL'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/NHL'

mongo = PyMongo(app)

@app.route('/teams', methods=['GET'])
def get_all_teams():
  teams = mongo.db.NHLdata
  output = []
  for s in teams.find():
    output.append({'SEASON' : s['SEASON'], 'RANK' : s['RANK'], 'TEAM' : s['TEAM'], 'HOME GAMES' : s['HOME GAMES'], 'HOME ATTENDANCE' : s['HOME ATTENDANCE'], 'ROAD GAMES' : s['ROAD GAMES'], 'ROAD ATTENDANCE' : s['ROAD ATTENDANCE'], 'TOTAL GAMES' : s['TOTAL GAMES'], 'TOTAL ATTENDANCE' : s['TOTAL ATTENDANCE']})
  return jsonify({'result' : output})

@app.route('/teams/<TEAM>/', methods=['GET'])
def get_one_team(TEAM):
  teams = mongo.db.NHLdata
  s = teams.find_one({'TEAM' : TEAM})
  if s:
    output = {'TEAM' : s['TEAM'], 'SEASON' : s['SEASON'], 'RANK' : s['RANK'], 'HOME GAMES' : s['HOME GAMES'], 'HOME ATTENDANCE' : s['HOME ATTENDANCE'], 'ROAD GAMES' : s['ROAD GAMES'], 'ROAD ATTENDANCE' : s['ROAD ATTENDANCE'], 'TOTAL GAMES' : s['TOTAL GAMES'], 'TOTAL ATTENDANCE' : s['TOTAL ATTENDANCE']}
  else:
    output = "No such team"
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)