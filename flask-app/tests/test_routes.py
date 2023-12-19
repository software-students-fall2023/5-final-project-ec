import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from app import app  # Import your Flask app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Customer Feedback System" in response.data

def test_feedback_form_route(client):
    response = client.get('/feedback')
    assert response.status_code == 200
    assert b"Submit Your Feedback" in response.data

def test_feedback_submission(client):
    test_feedback = "This is a test feedback"
    response = client.post('/feedback', data={'feedback': test_feedback}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Feedback submitted successfully!" in response.data


def test_view_feedback_route(client):
    # Make a GET request to the view-feedback route
    response = client.get('/view-feedback')
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # If you know specific feedback text that should be present, check for it
    # For example, if you've submitted "Test Feedback" previously and it's stored in the database:
    assert b"Test Feedback" in response.data

    # Alternatively, if you're not sure of specific feedback, but want to ensure that
    # the structure for feedback is present (e.g., there are <p> tags in the response), 
    # you could check for that:
    assert b"<p>" in response.data

    # You can also check for the presence of other elements like headers or footers
    assert b"Customer Feedback" in response.data  # Example: Checking for a section header
