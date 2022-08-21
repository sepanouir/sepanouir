from Sep import *
from config import ProductionConfig


app=create_app(ProductionConfig)

with app.app_context():
	user = Admin.query.first()
	print(user.email)
	print(user.password)

