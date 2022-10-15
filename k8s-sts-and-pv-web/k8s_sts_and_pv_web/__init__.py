import flask
import requests
import urllib.parse


def create_app() -> flask.Flask:
    app = flask.Flask(__name__)

    return app


app = create_app()


@app.route('/<service>/<port>')
def handle_service(service:str, port:str):
    response = requests.get(
        urllib.parse.urlunsplit(('http', service + ':' + port, '/', flask.request.query_string.decode('utf-8'), ''))
    )

    return flask.jsonify({
        'status_code': response.status_code,
        'body': response.json()
    })
