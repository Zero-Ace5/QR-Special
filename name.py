import logging
from flask import Flask, request, render_template, session, redirect, url_for, flash
from routes.main_routes import main_bp

app = Flask(__name__)

app.secret_key = "secre"

app.register_blueprint(main_bp)


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


@app.route('/jinja')
def jinja():
    return render_template('jinja.html')


@app.route('/health')
def health_check():
    app.logger.info("Health check requested.")
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(debug=True)
