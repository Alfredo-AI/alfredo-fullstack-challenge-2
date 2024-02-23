from uuid import uuid4
from typing import Any

from datetime import datetime
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Float, Index


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    public_id = Column(
        String,
        unique=True,
        nullable=False,
        default=lambda: uuid4().hex
    )

    phone = Column(String)
    account_type = Column(String, default="regular", index=True)
    registration_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="active", index=True)
    origin = Column(String, index=True)
    lang = Column(String, index=True)

    def __repr__(self):
        return f"<User(email='{self.email}', name='{self.name}', account_type='{self.account_type}')>"


class Subscription(Base):
    id = Column(Integer, primary_key=True)
    date_init = Column(DateTime, default=datetime.utcnow)
    date_end = Column(DateTime, default=datetime.utcnow)
    status = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'), index=True)
    reason = Column(String)
    
    def __repr__(self):
        return f"<Subscription(id='{self.id}', reason='{self.reason}')>"
