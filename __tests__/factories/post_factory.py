import factory
from faker import Faker

from app import db
from app.models import Post

faker = Faker()

class PostFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Post
        sqlalchemy_session = db.session
        sqlalchemy_session_persistece = 'commit'

    title = faker.text()
    text = faker.paragraph()
    published = True