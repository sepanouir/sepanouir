# import os

# import os
# from os.path import join, dirname
# from dotenv import load_dotenv
# is_prod = os.environ.get('IS_SERVER', None)
# if not is_prod:
# 	dotenv_path = join(dirname(__file__), '.env')
# 	load_dotenv(dotenv_path, verbose=True)
# 	env=True
# else:
# 	env=False
# #     /**these settings will load up only when we are in a server environment*/
# #     APP_ENV = os.environ.get('APP_ENV')
# #     DEBUG = os.environ.get('DEBUG')

# db_uri='postgresql://eupffnwpticpxv:2aa1bf09f1debcac5da02c780c7267567440530ff2013999320cca10caeb9768@ec2-52-30-159-47.eu-west-1.compute.amazonaws.com:5432/d20nrtd7i24t0c'

# youtube api key AIzaSyArD4OxXRWI_LUu6oZBaQp-udrgWISfwAU

# db_uri = "sqlite:///test.db"
# db_uri = 'postgresql://hjzwqdyjsxpthd:a813015534804b1006718d69bfe179d1c1129b0fada39a5ab56f7eec399a8455@ec2-63-34-180-86.eu-west-1.compute.amazonaws.com:5432/dejf3cqd8mhfeh'
db_uri = 'postgresql://dlqmpeecuezmmv:3f56fb7a8abf98b6bf509f39a835e2ca95eaf741225224e8c0d858a0b3897e1f@ec2-34-252-35-249.eu-west-1.compute.amazonaws.com:5432/dcofgr35drvp5o'
class Config(object):
	DEBUG = True
	TESTING = False
	CSRF_ENABLED = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = db_uri
	SESSION_COOKIE_SECURE = True
	SESSION_COOKIE_HTTPONLY = True
	SESSION_COOKIE_SAMESITE = 'None'
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 465 
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True 
	

# abderafiechairi02@gmail.com

# class ProductionConfig(Config):
# 	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
# 	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
# 	SECRET_KEY = os.environ.get("SECRET_KEY")	
# 	SQLALCHEMY_DATABASE_URI = os.environ.get("NEW_DATABASE_URL")

# class DeveloppementConfig(Config):
# 	MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
# 	MAIL_USERNAME = os.getenv("MAIL_USERNAME")
# 	SECRET_KEY = os.getenv("SECRET_KEY")	
# 	SQLALCHEMY_DATABASE_URI = os.getenv("NEW_DATABASE_URL")	


class ProductionConfig(Config):
	MAIL_PASSWORD = 'gexxrmihlbqnhxfn'
	MAIL_USERNAME = 'sepanouir.maroc@gmail.com'
	SECRET_KEY = 'kjsgjgfdskhgfdskhgfksgkfqgkfq'
	MAIL_CHECK_API_KEY='57a4d05d-7095-4a6c-8a35-35fd9c4b4d8f'	

# sepanouir.amdin@gmail.com


# sepanouir.maroc@gmail.com
# gexxrmihlbqnhxfn





# imtecbihlorfxqbb