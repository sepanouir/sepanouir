from Sep import *
from config import ProductionConfig


app=create_app(ProductionConfig)

with app.app_context():
	user = User.query.first()
	print(user)
	print(user.password)

