from pymongo import MongoClient

def test_update():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["customer_feedback_db"]
    positive_feedback_collection = db["positive_feedback"]
    negative_feedback_collection = db["negative_feedback"]

    pos_result = positive_feedback_collection.update_one(
        {"feedback_text": "Test positive feedback"}, 
        {"$set": {"feedback_text": "Updated positive test feedback"}}
    )

    neg_result = negative_feedback_collection.update_one(
        {"feedback_text": "Test negative feedback"}, 
        {"$set": {"feedback_text": "Updated negative test feedback"}}
    )
    print(f"Modified {pos_result.modified_count} document(s)")
    print(f"Modified {neg_result.modified_count} document(s)")
if __name__ == "__main__":
    test_update()
