from flask import Flask
app = Flask(__name__)
@app.route('/api/', methods=['GET', 'POST'])
def welcome():
    return "pong"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
