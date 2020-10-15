from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from package_tracker import app
from app.models import User, Package, db

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username="miah", password="password")
    package1 = Package(sender='miah', recipient='bob', origin='Houston', destination='Los Angeles', location='Houston', user=user1)
    db.session.add(package1)
    db.session.commit()