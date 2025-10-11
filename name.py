from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about', methods=['GET', 'POST'])
def uname():
    # return "This is About"
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('about.html', name=name)
    return render_template('about.html', name=None)


if __name__ == "__main__":
    app.run(debug=True)
