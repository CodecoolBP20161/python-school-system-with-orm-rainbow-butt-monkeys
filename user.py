from peewee import *
import config

db = PostgresqlDatabase(config.dbname, user=config.name)

class BaseModel(Model):  # Main Class with the database connection.
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db

class User(BaseModel):
    id = PrimaryKeyField()
    username = CharField(unique=True)
    password = CharField()
    email = CharField(unique=True)
    registered_on = DateTimeField()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymus(self):
        return False

    def get_id(self):
        return (self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)