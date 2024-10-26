import pytest
from fastapi.testclient import TestClient
from api.main import app
from database.models import User, APIRequest
from database.engine import get_db
from sqlalchemy.orm import Session
import datetime

client = TestClient(app)

# Sample data for testing
@pytest.fixture
def sample_user():
    return User(username="testuser", password_hash="testpasswordhash")

@pytest.fixture
def sample_api_request(sample_user):
    return APIRequest(
        user_id=sample_user.id,
        model="text-davinci-003",
        prompt="Test prompt",
        temperature=7,  # Store as percentage
        max_tokens=100,
        response="Test response",
        success=True,
    )

# Test database interactions (CRUD operations)
def test_create_user(sample_user, get_db):
    db: Session = get_db()
    db.add(sample_user)
    db.commit()
    db.refresh(sample_user)
    assert sample_user.id is not None

def test_get_user(sample_user, get_db):
    db: Session = get_db()
    db.add(sample_user)
    db.commit()
    db.refresh(sample_user)
    user = db.query(User).filter(User.username == "testuser").first()
    assert user.username == "testuser"

def test_update_user(sample_user, get_db):
    db: Session = get_db()
    db.add(sample_user)
    db.commit()
    db.refresh(sample_user)
    user = db.query(User).filter(User.username == "testuser").first()
    user.username = "updateduser"
    db.commit()
    db.refresh(user)
    assert user.username == "updateduser"

def test_delete_user(sample_user, get_db):
    db: Session = get_db()
    db.add(sample_user)
    db.commit()
    db.refresh(sample_user)
    user = db.query(User).filter(User.username == "testuser").first()
    db.delete(user)
    db.commit()
    assert db.query(User).filter(User.username == "testuser").first() is None

def test_create_api_request(sample_api_request, get_db):
    db: Session = get_db()
    db.add(sample_api_request)
    db.commit()
    db.refresh(sample_api_request)
    assert sample_api_request.id is not None

def test_get_api_request(sample_api_request, get_db):
    db: Session = get_db()
    db.add(sample_api_request)
    db.commit()
    db.refresh(sample_api_request)
    api_request = db.query(APIRequest).filter(APIRequest.id == sample_api_request.id).first()
    assert api_request.prompt == "Test prompt"

def test_update_api_request(sample_api_request, get_db):
    db: Session = get_db()
    db.add(sample_api_request)
    db.commit()
    db.refresh(sample_api_request)
    api_request = db.query(APIRequest).filter(APIRequest.id == sample_api_request.id).first()
    api_request.prompt = "Updated test prompt"
    db.commit()
    db.refresh(api_request)
    assert api_request.prompt == "Updated test prompt"

def test_delete_api_request(sample_api_request, get_db):
    db: Session = get_db()
    db.add(sample_api_request)
    db.commit()
    db.refresh(sample_api_request)
    api_request = db.query(APIRequest).filter(APIRequest.id == sample_api_request.id).first()
    db.delete(api_request)
    db.commit()
    assert db.query(APIRequest).filter(APIRequest.id == sample_api_request.id).first() is None

# Test query relationships and data retrieval
def test_get_api_requests_for_user(sample_user, sample_api_request, get_db):
    db: Session = get_db()
    db.add(sample_user)
    db.add(sample_api_request)
    db.commit()
    db.refresh(sample_user)
    user = db.query(User).filter(User.id == sample_user.id).first()
    api_requests = user.api_requests
    assert len(api_requests) == 1
    assert api_requests[0].prompt == "Test prompt"

def test_get_last_activity_for_user(sample_user, sample_api_request, get_db):
    db: Session = get_db()
    db.add(sample_user)
    db.add(sample_api_request)
    db.commit()
    db.refresh(sample_user)
    user = db.query(User).filter(User.id == sample_user.id).first()
    assert user.last_activity == sample_api_request.timestamp

# Test data formatting and calculations
def test_api_request_normalized_temperature(sample_api_request):
    assert sample_api_request.normalized_temperature == 0.7

def test_api_request_formatted_timestamp(sample_api_request):
    assert sample_api_request.formatted_timestamp == sample_api_request.timestamp.strftime('%Y-%m-%d %H:%M:%S')