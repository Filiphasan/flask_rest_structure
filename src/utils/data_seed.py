from db import db

from src.models.users import UsersModel

def seed_data():
    user = UsersModel.query.filter_by(email="test@test.com").first()
    if not user:
        user1 = UsersModel(id="e6af78d6-3bed-4a8b-8498-d7bcedf3bfb0",first_name="Hasan", last_name="Erdal",username="deneme",email="test@test.com",password_hash="e10adc3949ba59abbe56e057f20f883e")
        user1.email_confirmed = True
        #password=123456
        db.session.add(user1)
        db.session.commit()