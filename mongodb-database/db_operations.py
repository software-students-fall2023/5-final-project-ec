from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # Replace with your MongoDB URI
db = client.customer_feedback # Database name
#users = db.users # Users collection
positive_feedback = db.positive_feedback # Feedback collection
negative_feedback = db.negative_feedback # Feedback collection
# Example: Inserting data
#user_data = {"user_id": 1, "name": "John Doe", "email": "john@example.com"}
positive_feedback_data = {"feedback_text": "Great service!", "timestamp": "2021-01-01"}
negative_feedback_data = {"feedback_text": "Bad service!", "timestamp": "2021-01-01"}
#users.insert_one(user_data)
positive_feedback.insert_one(positive_feedback_data)
negative_feedback.insert_one(negative_feedback_data)
# Example: Fetching data
for f in positive_feedback.find():
    print(f)

for f in negative_feedback.find():
    print(f)
