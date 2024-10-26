from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

    api_requests = relationship('APIRequest', backref='user', cascade='all, delete-orphan')

    @hybrid_property
    def last_activity(self):
        last_request = self.api_requests.order_by(APIRequest.timestamp.desc()).first()
        return last_request.timestamp if last_request else None

class APIRequest(Base):
    __tablename__ = 'api_requests'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    model = Column(String, nullable=False)
    prompt = Column(String, nullable=False)
    temperature = Column(Integer, default=7, nullable=False) # Store as percentage for easier retrieval and comparison
    max_tokens = Column(Integer, default=100, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    response = Column(String, nullable=True)
    success = Column(Boolean, default=False, nullable=False)
    error_message = Column(String, nullable=True)

    @property
    def normalized_temperature(self):
        return self.temperature / 10 # Convert from percentage to decimal

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%Y-%m-%d %H:%M:%S')