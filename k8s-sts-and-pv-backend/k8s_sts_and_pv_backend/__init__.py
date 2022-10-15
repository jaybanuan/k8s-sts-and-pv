import flask
import json
import pathlib


def create_app() -> flask.Flask:
    app = flask.Flask(__name__)
    app.config['DATA_FILE_DIR'] = app.instance_path
    app.config.from_prefixed_env()

    data_file_dir = pathlib.Path(app.config['DATA_FILE_DIR'])
    data_file_dir.mkdir(parents=True, exist_ok=True)

    data_file = pathlib.Path(data_file_dir, 'data.json')
    if not data_file.exists():
        with open(data_file, 'w') as output_file:
            json.dump(dict(), output_file)

    app.config['DATA_FILE'] = data_file

    return app


app = create_app()
data_file = app.config['DATA_FILE']


@app.route('/')
def handle_root():
    with open(data_file, 'r') as input_file:
        json_data = json.load(input_file)
    
    if flask.request.args:
        for key, value in flask.request.args.items():
            json_data[key] = value

        with open(data_file, 'w') as output_file:
            json.dump(json_data, output_file)

    return flask.jsonify(json_data)
