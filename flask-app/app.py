from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from datetime import datetime
from machine_learning import sentiment_analysis
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# MongoDB setup (adjust the URI as needed)
client = MongoClient('localhost', 27017) 
db = client["customer_feedback_db"]
positive_feedback_collection = db["positive_feedback"]
negative_feedback_collection = db["negative_feedback"]

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d %H:%M'):
    return value.strftime(format)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feedback', methods=['GET', 'POST'])
def submit_feedback():
    if request.method == 'POST':
        feedback_text = request.form['feedback']
        sentiment=sentiment_analysis.analyze_feedback(feedback_text)
        feedback_data = {
            "feedback_text": feedback_text,
            "timestamp": datetime.now(),
        }
        # Insert into appropriate collection based on sentiment 
        if sentiment>= 0: 
            positive_feedback_collection.insert_one(feedback_data)
        else:
            negative_feedback_collection.insert_one(feedback_data)

        flash('Feedback submitted successfully!')  # Flash a confirmation message
        return redirect(url_for('view_feedback'))
    return render_template('feedback.html')

@app.route('/view-feedback')
def view_feedback():
    positive_feedbacks = list(positive_feedback_collection.find())
    negative_feedbacks = list(negative_feedback_collection.find())
    return render_template('view_feedback.html', positive_feedbacks=positive_feedbacks, negative_feedbacks=negative_feedbacks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

