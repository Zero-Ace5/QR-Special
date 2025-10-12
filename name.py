from flask import Flask, request, render_template, session, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = "secre"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about', methods=['GET', 'POST'])
def uname():
    # name = request.form.get('name') if request.method == 'POST'else None
    # return render_template('about.html', name=name)
    name = None

    if request.method == 'POST':
        name = request.form.get('name')

    if name:
        session['username'] = name

    return render_template('about.html', name=session.get('username'))


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    if not name.strip():
        flash("Name cannot be empty!", "error")
        return redirect(url_for('home'))
    session['username'] = name
    return redirect(url_for('uname'))


if __name__ == "__main__":
    app.run(debug=True)
