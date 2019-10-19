from flask import Flask, render_template
app = Flask(__name__)
@app.route('/tools')
def home():
    return render_template('resources.html')
if __name__ == '__main__':
    app.run(debug=True)