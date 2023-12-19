from pymongo import MongoClient
from datetime import datetime

def test_insert():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["customer_feedback_db"]
    positive_feedback_collection = db["positive_feedback"]
    negative_feedback_collection = db["negative_feedback"]

    new_pos_feedback = {
        "feedback_text": "Test positive feedback",
        "timestamp": datetime.now()
    }
    new_neg_feedback = {
        "feedback_text": "Test negative feedback",
        "timestamp": datetime.now()
    }

    pos_result = positive_feedback_collection.insert_one(new_pos_feedback)
    neg_result = negative_feedback_collection.insert_one(new_neg_feedback)
    print(f"Inserted Feedback ID: {pos_result.inserted_id}")
    print(f"Inserted Feedback ID: {neg_result.inserted_id}")

if __name__ == "__main__":
    test_insert()
