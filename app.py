from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to local MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['local']  # Database name
collectionUser = db['ROSIUserConn']  # Collection name
collectionActivity = db['ROSIActivityConn']  # Collection name

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/addUser')
def page1():
    return render_template('addUser.html')

@app.route('/addActivity')
def page2():
    return render_template('addActivity.html')

@app.route('/submitUser', methods=['POST'])
def submitUser():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    age = request.form.get('age')
    gender = request.form.get('gender')
    province = request.form.get('province')
    city = request.form.get('city')
    language = request.form.get('language')
    personality = request.form.get('personality')

    # You can process the form data here
    # For now, we'll just print it out to the console
    print(f"First Name: {firstname}")
    print(f"Last Name: {lastname}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Province: {province}")
    print(f"City: {city}")
    print(f"Language: {language}")
    print(f"Personality Type: {personality}")

    submission_data = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age,
        "gender": gender,
        "province": province,
        "city": city,
        "language": language,
        "personality": personality
    }

    collectionUser.insert_one(submission_data)  # Insert data into MongoDB collection


    return f"Form submitted successfully!<br>First Name: {firstname}<br>Last Name: {lastname}<br>Age: {age}<br>Gender: {gender}<br>Province: {province}<br>City: {city}<br>Language: {language}<br>Personality Type: {personality}"

@app.route('/submitActivity', methods=['POST'])
def submit_activity():
    activity_name = request.form.get('activityName')
    activity_type = request.form.get('activityType')
    frequency = request.form.get('frequency')
    duration = request.form.get('duration')
    activity_description = request.form.get('activityDescription')
    precautions = request.form.get('precautions')
    followup = request.form.get('followup')

    submission_data = {
        "activity_name": activity_name,
        "activity_type": activity_type,
        "frequency": frequency,
        "duration": duration,
        "activity_description": activity_description,
        "precautions": precautions,
        "followup": followup
    }

    collectionActivity.insert_one(submission_data)  # Insert data into MongoDB collection

    
    # You can process the data here (e.g., store in database, print, etc.)
    return f"""
        <h1>Activity Submitted</h1>
        <p><strong>Activity Name:</strong> {activity_name}</p>
        <p><strong>Activity Type:</strong> {activity_type}</p>
        <p><strong>Frequency:</strong> {frequency}</p>
        <p><strong>Duration:</strong> {duration}</p>
        <p><strong>Activity Description:</strong> {activity_description}</p>
        <p><strong>Precautions:</strong> {precautions}</p>
        <p><strong>Followup:</strong> {followup}</p>
    """


if __name__ == '__main__':
    app.run(debug=True)
