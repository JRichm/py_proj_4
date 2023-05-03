from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    teams = db.relationship("Teams", backref = "user", lazy = True)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    
class Teams(db.Model):
    __tablename__ = 'teams'
    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_name = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    
    def __init__(self, team_name, user_id):
        self.team_name = team_name
        self.user_id = user_id
    
    
class Projects(db.Model):
    __tablename__ = 'projects'
    project = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    completed = db.Column(db.Boolean, default=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=False)
    
    def __init__(self, project_name, completed, team_id, description=None):
        self.project_name = project_name
        self.completed = completed
        self.team_id = team_id
        if description is not None:
            self.description = description
        else:
            self.description = 'No description'
            
    
def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
        
        
if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    with app.app_context():
        connect_to_db(app)
        print('Connected to db...')