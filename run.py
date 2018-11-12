from flask import Flask, render_template


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def view_index():
    return render_template('pages/index.html')

@app.route('/about')
def view_about():
    return render_template('pages/form-components.html')

if __name__ == '__main__':
    app.run(debug=app.debug)