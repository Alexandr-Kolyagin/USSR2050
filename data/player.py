import sqlalchemy
from .db_session import SqlAlchemyBase


class Player(SqlAlchemyBase):
    __tablename__ = 'players'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    lvl = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    x = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    y = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    # registration_date = sqlalchemy.Column(sqlalchemy.DateTime,
    #                                       default=datetime.datetime.now)
    # date_birth = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    # admin = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # friends = orm.relation("Friend", back_populates='user')


