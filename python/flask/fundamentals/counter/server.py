from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="I am a secret key."

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template("counter.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)