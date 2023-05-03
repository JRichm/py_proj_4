from flask import Flask, render_template, redirect, url_for
from forms import TeamForm, ProjectForm
from model import connect_to_db, User, Teams, Projects, db

app = Flask(__name__)
app.secret_key = 'minecraft rocks'

user_id = 1

        ##        Flask Routes        ##
@app.route('/')
def home():
    team_form = TeamForm()
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams)
    return render_template('home.html', team_form=team_form, project_form=project_form)

@app.route('/add-team', methods=['POST'])
def add_team():
    team_form = TeamForm()
    
    if team_form.validate_on_submit():
        team_name = team_form.team_name.data
        new_team = Teams(team_name, user_id)
        db.session.add(new_team)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))
    
    
@app.route('/add-project', methods=['POST'])
def add_project():
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams)
    
    if project_form.validate_on_submit():
        project_name = project_form.project_name.data
        project_description = project_form.description.data
        project_completed = project_form.completed.data
        team_id = project_form.team_selection.data
        
        new_project = Projects(project_name, project_completed, team_id, description=project_description)
        db.session.add(new_project)
        db.session.commit()
        
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


        ##       Server Methods       ##
if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True)