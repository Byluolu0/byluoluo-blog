import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	ARTICLE_DIR = basedir + '/articles'

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,

	'default': DevelopmentConfig
}