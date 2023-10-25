import logging

from flask import render_template, request, Blueprint
from functions import save_form_result

logging.basicConfig(filename="basic.log", level=logging.INFO)

loader_blueprint = Blueprint('loader_blueprint', __name__, url_prefix="/post", template_folder='templates')


@loader_blueprint.route('/')
def main_page():
    return render_template('post_form.html')


@loader_blueprint.route('/uploads', methods=["POST"])
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
