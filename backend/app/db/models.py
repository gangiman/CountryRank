from sqlalchemy import Boolean, Column, Integer, String, Date, JSON, Text
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from .session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)


class Ranking(Base):
    __tablename__ = "Ranking"

    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(Date)
    ranking = Column(JSON)
    number_of_countries = Column(Integer)
    source = Column(Text)
    user_id = Column(
        Integer,
        ForeignKey('user.id', ondelete='CASCADE'),
        nullable=False,
        # no need to add index=True, all FKs have indexes
    )
    user = relationship('User', backref='Ranking')
