from pymongo import MongoClient
from datetime import datetime

def create_collections(db):
    # Creating collections
    db.create_collection("users")
    db.create_collection("negative_feedback")
    db.create_collection("positive_feedback")

    print("Collections 'users' and 'feedback' created.")

def insert_initial_data(db):
    # Inserting some initial user data
    # users_data = [
    #     {"user_id": 1, "name": "John Doe", "email": "john@example.com"},
    #     {"user_id": 2, "name": "Jane Doe", "email": "jane@example.com"}
    # ]
    # db.users.insert_many(users_data)

    # Inserting some initial feedback data
    positive_feedback_data = [
        {"feedback_text": "Great service!", "timestamp": datetime.now()},
        {"feedback_text": "Very satisfied.", "timestamp": datetime.now()}
    ]
    negative_feedback_data = [
        {"feedback_text": "Bad service!", "timestamp": datetime.now()},
        {"feedback_text": "Very bad.", "timestamp": datetime.now()}
    ]
    db.negative_feedback.insert_many(negative_feedback_data)
    db.positive_feedback.insert_many(positive_feedback_data)
    print("Initial data inserted into 'negative_feedback' and 'positive_feedback' collections.")

def main():
    # Connect to the MongoDB local client
    client = MongoClient('localhost', 27017) 

    # Connect to the database (will create if it doesn't exist)
    db = client["customer_feedback_db"]

    # Create collections and insert initial data
    create_collections(db)
    insert_initial_data(db)

if __name__ == "__main__":
    main()
