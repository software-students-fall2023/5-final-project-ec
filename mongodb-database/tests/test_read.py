from pymongo import MongoClient

def test_read():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["customer_feedback_db"]
    positive_feedback_collection = db["positive_feedback"]
    negative_feedback_collection = db["negative_feedback"]

    for feedback in positive_feedback_collection.find():
        print(feedback)
    for feedback in negative_feedback_collection.find():
        print(feedback)
if __name__ == "__main__":
    test_read()
