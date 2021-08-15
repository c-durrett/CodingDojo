from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

app.secret_key = "lol secret key"

@app.route('/')
def index():
    return render_template("dojo_survey.html")

@app.route('/get_results', methods = ['POST'])
def get_results():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__=="__main__":
    app.run(debug=True)