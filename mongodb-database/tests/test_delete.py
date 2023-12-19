from pymongo import MongoClient

def test_delete():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["customer_feedback_db"]
    positive_feedback_collection = db["positive_feedback"]
    negative_feedback_collection = db["negative_feedback"]

    pos_result = positive_feedback_collection.delete_one({"feedback_text": "Updated positive test feedback"})
    neg_result = negative_feedback_collection.delete_one({"feedback_text": "Updated negative test feedback"})
    print(f"Deleted {pos_result.deleted_count} document(s)")
    print(f"Deleted {neg_result.deleted_count} document(s)")

if __name__ == "__main__":
    test_delete()
