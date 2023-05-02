from flask import Flask, render_template, redirect, url_for
from forms import TeamForm
from model import connect_to_db

app = Flask(__name__)
app.secret_key = 'minecraft rocks'


        ##        Flask Routes        ##
@app.route('/')
def home():
    team_form = TeamForm()
    return render_template('home.html', team_form=team_form)

@app.route('/add_team', methods=['POST'])
def add_team():
    team_form = TeamForm()
    
    if team_form.validate_on_submit():
        print(team_form.team_name.data)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

        ##       Server Methods       ##
if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True)