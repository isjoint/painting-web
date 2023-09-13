"""
@date: 2023/9/11
@author: March
@desc: test

"""

from app import create_app
from config import settings
my_app = create_app()

from flask_migrate import Migrate
from models import db

migrate = Migrate(my_app, db)

if __name__ == "__main__":
    my_app.run(host=settings.HOST,
               port=settings.PORT,
               debug=settings.DEBUG)





