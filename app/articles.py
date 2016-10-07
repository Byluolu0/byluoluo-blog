from os import listdir
from markdown2 import markdown

class Articles:
	art_list = []

	def init_app(self, app):
		article_dir = app.config['ARTICLE_DIR']
		file_list = listdir(article_dir)
		for f in file_list:
			art_file = open(article_dir + '/' + f)
			art = art_file.read()
			art_file.close()
			art = markdown(art)
			self.art_list.append(art)

	def get_art_list(self):
		return self.art_list