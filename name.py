from flask import Flask, request, render_template, session

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


if __name__ == "__main__":
    app.run(debug=True)
