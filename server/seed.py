from app import app
from models import db #import other models here too!

if __name__ == '__main__':
    with app.app_context():

        print("Starting seed...")

        # you can add seeds here...

        print("Seeding complete...")