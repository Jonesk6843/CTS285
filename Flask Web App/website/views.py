from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/') # ('/', methods=['GET','POST']) but im paraphrasing
def home():
    return render_template("home.html")