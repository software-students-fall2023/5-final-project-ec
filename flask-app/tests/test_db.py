import pytest
from pymongo import MongoClient
from datetime import datetime

@pytest.fixture(scope="module")
def mongo_client():
    # Set up a separate test database
    client = MongoClient("mongodb://localhost:27017/")
    yield client
    # Clean up: Drop the test database after tests are done
    client.drop_database("test_customer_feedback_db")

def test_insert_and_read_feedback(mongo_client):
    test_db = mongo_client["test_customer_feedback_db"]
    positive_feedback_collection = test_db["positive_feedback"]
    negative_feedback_collection = test_db["negative_feedback"]
    # Insert a test feedback
    pos_test_feedback = {
        "feedback_text": "Test positive feedback",
        "timestamp": datetime.now()
    }
    neg_test_feedback = {
        "feedback_text": "Test negative feedback",
        "timestamp": datetime.now()
    }
    pos_insert_result = positive_feedback_collection.insert_one(pos_test_feedback)
    assert pos_insert_result.inserted_id
    neg_insert_result = negative_feedback_collection.insert_one(neg_test_feedback)
    assert neg_insert_result.inserted_id

    # Read the inserted feedback
    read_pos_feedback = positive_feedback_collection.find_one({"_id": pos_insert_result.inserted_id})
    assert read_pos_feedback is not None
    assert read_pos_feedback['feedback_text'] == "Test positive feedback"

    read_neg_feedback = negative_feedback_collection.find_one({"_id": neg_insert_result.inserted_id})
    assert read_neg_feedback is not None
    assert read_neg_feedback['feedback_text'] == "Test negative feedback"

def test_update_feedback(mongo_client):
    test_db = mongo_client["test_customer_feedback_db"]
    positive_feedback_collection = test_db["positive_feedback"]
    negative_feedback_collection = test_db["negative_feedback"]

    # Insert a test feedback
    positive_feedback_collection.insert_one({"feedback_text": "Old positive feedback", "timestamp": datetime.now()})
    negative_feedback_collection.insert_one({"feedback_text": "Old negative feedback", "timestamp": datetime.now()})
    # Update the feedback
    updated_pos_feedback = "Updated positive feedback"
    positive_feedback_collection.update_one({"feedback_text": "Old positive feedback"}, {"$set": {"feedback_text": updated_pos_feedback}})
    updated_neg_feedback = "Updated negative feedback"
    negative_feedback_collection.update_one({"feedback_text": "Old negative feedback"}, {"$set": {"feedback_text": updated_neg_feedback}})

    # Verify update
    updated_pos_record = positive_feedback_collection.find_one({"feedback_text": updated_pos_feedback})
    assert updated_pos_record
    assert updated_pos_record['feedback_text'] == updated_pos_feedback
    updated_neg_record = negative_feedback_collection.find_one({"feedback_text": updated_neg_feedback})
    assert updated_neg_record
    assert updated_neg_record['feedback_text'] == updated_neg_feedback

def test_delete_feedback(mongo_client):
    test_db = mongo_client["test_customer_feedback_db"]
    positive_feedback_collection = test_db["positive_feedback"]
    negative_feedback_collection = test_db["negative_feedback"]

    # Insert a test feedback
    pos_feedback_id = positive_feedback_collection.insert_one({"feedback_text": "Test positive feedback", "timestamp": datetime.now()}).inserted_id
    neg_feedback_id = negative_feedback_collection.insert_one({"feedback_text": "Test negative feedback", "timestamp": datetime.now()}).inserted_id
    # Delete the feedback
    positive_feedback_collection.delete_one({"_id": pos_feedback_id})
    negative_feedback_collection.delete_one({"_id": neg_feedback_id})
    # Verify deletion
    pos_deleted_record = positive_feedback_collection.find_one({"_id": pos_feedback_id})
    assert pos_deleted_record is None
    neg_deleted_record =  negative_feedback_collection.find_one({"_id": neg_feedback_id})
    assert neg_deleted_record is None
