from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! Our awesome app is running! And the WebHook too.'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
