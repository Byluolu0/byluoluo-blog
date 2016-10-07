from flask import render_template
from flask import current_app

from . import main
from .. import articles

@main.route('/')
def index():
	return render_template('index.html', articles=articles.get_art_list())