import logging
from flask import Flask, request, render_template, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint
from functions import *

logging.basicConfig(filename="basic.log", level=logging.INFO)

app = Flask(__name__)

app.register_blueprint(main_blueprint, url_prefix="/")
app.register_blueprint(loader_blueprint, url_prefix="/post")

post_data = get_posts_from_json()


@app.route('/search')
def search_page():
    search_string = request.args.get('s')
    found_posts = search_posts(search_string)

    logging.info(f"Поиск по значению {search_string}")

    return render_template('post_list.html', found_posts=found_posts, search_string=search_string)


@app.route('/uploads', methods=["POST"])
def uploads_page():
    pic = request.files.get('picture')
    text = request.values.get('content')

    try:
        result_post = save_form_result(pic, text)
    except FileExistsError:
        logging.error(f"Ошибка загрузки")
        return "Ошибка загрузки"
    else:
        return render_template('post_uploaded.html', post=result_post)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)
