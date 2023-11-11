from flask import Flask, jsonify
from utils import get_animal_by_id

app = Flask(__name__)
app.config.from_pyfile('./config.py')


@app.route("/<animal_id>")
def animal_page(animal_id):
    return jsonify(get_animal_by_id(animal_id, app.config.get('DB_PATH')))


if __name__ == "__main__":
    app.run(debug=True)
