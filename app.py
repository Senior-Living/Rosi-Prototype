from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to local MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['local']  # Database name
collection = db['ROSIUserConn']  # Collection name

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/1.0')
def page1():
    return render_template('version1-0.html')

@app.route('/1.1')
def page2():
    return "Rosie 1.1"

@app.route('/submit', methods=['POST'])
def submit():
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

    collection.insert_one(submission_data)  # Insert data into MongoDB collection


    return f"Form submitted successfully!<br>First Name: {firstname}<br>Last Name: {lastname}<br>Age: {age}<br>Gender: {gender}<br>Province: {province}<br>City: {city}<br>Language: {language}<br>Personality Type: {personality}"


if __name__ == '__main__':
    app.run(debug=True)
