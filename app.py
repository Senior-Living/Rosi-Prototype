import json
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to local MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['local']  # Database name
collectionUser = db['ROSIUserConn']  # Collection name
collectionActivity = db['ROSIActivityConn']  # Collection name
collectionSocialClassifier = db['ROSISocialClassifierConn']  # Collection name

#℞OSI, not ROSI




# Route to insert data from JSON file into MongoDB
@app.route('/import_activities')
def import_activities():
    # Path to your JSON file
    json_file_path = 'activities.json'

    try:
        # Open and load the JSON file
        with open(json_file_path, 'r') as file:
            activities = json.load(file)  # This should be a list of dictionaries

        # Insert the activities into the collection
        if isinstance(activities, list):
            collectionActivity.insert_many(activities)
        else:
            collectionActivity.insert_one(activities)

        return "Activities imported successfully!"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
# Route to insert data from JSON file into MongoDB
@app.route('/import_users')
def import_users():
    # Path to your JSON file
    json_file_path = 'users.json'

    try:
        # Open and load the JSON file
        with open(json_file_path, 'r') as file:
            users = json.load(file)  # This should be a list of dictionaries

        # Insert the activities into the collection
        if isinstance(users, list):
            collectionUser.insert_many(users)
        else:
            collectionActivity.insert_one(users)

        return "Users imported successfully!"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

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
    #User Demographics 
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    dateOfBirth = request.form.get('dateOfBirth')
    gender = request.form.get('gender')
    interests = request.form.getlist('interests')
    personality = request.form.get('personality')
    social_goals = request.form.getlist('socialGoals')
    health_conditions = request.form.getlist('healthConditions')
    accessibility_needs = request.form.getlist('accessibilityNeeds')
    available_hours = request.form.get('availableHours')
    monthly_budget = request.form.get('monthlyBudget')
    independent_travel = request.form.get('independentTravel')
    zip_code = request.form.get('zipCode')
    activity_preferences = request.form.getlist('activityPreference')
    preferred_distance = request.form.get('distanceOptions')
    group_size_preference = request.form.getlist('groupSizePreference')
    time_preference = request.form.getlist('timePreference')
    language = request.form.get('language')

    socClas1EatWOthers = request.form.get('socClas1EatWOthers')    
    socClas2HobbiesInside = request.form.get('socClas2HobbiesInside')    
    socClas3HobbiesOutside = request.form.get('socClas3HobbiesOutside')    
    socClas4TV = request.form.get('socClas4TV')    
    socClas5Browsing = request.form.get('socClas5Browsing')    
    socClas6TalkPhone = request.form.get('socClas6TalkPhone')    
    socClas7MeetFamFriend = request.form.get('socClas7MeetFamFriend')    
    socClas8GroupConvo = request.form.get('socClas8GroupConvo')    
    socClas9Text = request.form.get('socClas9Text')    
    socClas10Volunteer = request.form.get('socClas10Volunteer')    
    socClas11Essential = request.form.get('socClas11Essential')    

    socClas1aWishPart = request.form.get('socClas1aWishPart')
    socClas1bTypesOfMealsInterested = request.form.getlist('socClas1bTypesOfMealsInterested')
    socClas1cTypesOfMealsParticipated = request.form.getlist('socClas1cTypesOfMealsParticipated')
    socClas1dWishPartMoreActivity = request.form.get('socClas1dWishPartMoreActivity')

    socClas2aWishTimeInsideHobbies = request.form.get('socClas2aWishTimeInsideHobbies')
    socClas2bTypesOfInsideHobbies = request.form.getlist('socClas2bTypesOfInsideHobbies')
    socClas2cTypesOfIndoorActivitiesParticipated = request.form.getlist('socClas2cTypesOfIndoorActivitiesParticipated')
    socClas2dWishPartMoreIndoorActivities = request.form.get('socClas2dWishPartMoreIndoorActivities')


    # Print statements for all retrieved data
    print("First Name:", firstname)
    print("Last Name:", lastname)
    print("Date of Birth:", dateOfBirth)
    print("Gender:", gender)
    print("Interests:", interests)
    print("Personality:", personality)
    print("Social Goals:", social_goals)
    print("Health Conditions:", health_conditions)
    print("Accessibility Needs:", accessibility_needs)
    print("Available Hours:", available_hours)
    print("Monthly Budget:", monthly_budget)
    print("Can Travel Independently:", independent_travel)
    print("ZIP Code:", zip_code)
    print("Activity Preferences:", activity_preferences)
    print("Preferred Distance:", preferred_distance)
    print("Group Size Preference:", group_size_preference)
    print("Time Preference:", time_preference)
    print("Language:", language)

    print("Social Classifiers")

    print("Eating with Others:", socClas1EatWOthers)
    print("Hobbies Inside:", socClas2HobbiesInside)
    print("Hobbies Outside:", socClas3HobbiesOutside)
    print("Watching TV:", socClas4TV)
    print("Browsing the Internet:", socClas5Browsing)
    print("Talking on the phone", socClas6TalkPhone)
    print("Meeting Family and Friends:", socClas7MeetFamFriend)
    print("Group Conversations:", socClas8GroupConvo)
    print("Text Messaging:", socClas9Text)
    print("Volunteering:", socClas10Volunteer)
    print("Essential Activities:", socClas11Essential)

    print(f"1a. Wish to participate in meals or social dining events: {socClas1aWishPart}")
    print(f"1b. Types of meals the user is interested in: {', '.join(socClas1bTypesOfMealsInterested) if socClas1bTypesOfMealsInterested else 'None'}")
    print(f"1c. Types of meals the user has participated in: {', '.join(socClas1cTypesOfMealsParticipated) if socClas1cTypesOfMealsParticipated else 'None'}")
    print(f"1d. Wish to participate in more social activities around meals: {socClas1dWishPartMoreActivity}")

    print(f"2a. Wish to spend time on hobbies or recreational activities inside the home: {socClas2aWishTimeInsideHobbies}")
    print(f"2b. Types of indoor hobbies the user is interested in: {', '.join(socClas2bTypesOfInsideHobbies) if socClas2bTypesOfInsideHobbies else 'None'}")
    print(f"2c. Types of indoor activities the user has participated in: {', '.join(socClas2cTypesOfIndoorActivitiesParticipated) if socClas2cTypesOfIndoorActivitiesParticipated else 'None'}")
    print(f"2d. Wish to participate in more indoor activities: {socClas2dWishPartMoreIndoorActivities}")



    socialClassifierStats = [
        socClas1EatWOthers,
        socClas2HobbiesInside,
        socClas3HobbiesOutside,
        socClas4TV,
        socClas5Browsing,
        socClas6TalkPhone,
        socClas7MeetFamFriend,
        socClas8GroupConvo,
        socClas9Text,
        socClas10Volunteer,
        socClas11Essential
    ]

    # extraClassifierStats1 = [
    #     socClas1aWishPart,
    #     socClas1bTypesOfMealsInterested,
    #     socClas1cTypesOfMealsParticipated,
    #     socClas1dWishPartMoreActivity,
    #     socClas2aWishTimeInsideHobbies,
    #     socClas2bTypesOfInsideHobbies,
    #     socClas2cTypesOfIndoorActivitiesParticipated,
    #     socClas2dWishPartMoreIndoorActivities
    # ]

    extraClassifierStatsFreq = [
        socClas1cTypesOfMealsParticipated,
        socClas2cTypesOfIndoorActivitiesParticipated
    ]

    #Step 1
    activeDomains = determineActiveDomain(socialClassifierStats)

    #Step 2
    freqPerDomain = countActivitiesPerDomain(extraClassifierStatsFreq)

    #Step 3
    pointsPerDomain = determineScorePerDomain(freqPerDomain,extraClassifierStatsFreq)


    #Step 4
    primaryDomain, primaryDomainFreq = findPrimaryDomain(socialClassifierStats)



    
    print(primaryDomain)
    print(primaryDomainFreq)
    print(freqPerDomain)

    socialScore = calcSocialScore(socialClassifierStats)


    user_submission_data = {
        "firstname": firstname,
        "lastname": lastname,
        "dateOfBirth": dateOfBirth,
        "gender": gender,
        "interests": interests,
        "personality": personality,
        "social_goals": social_goals,
        "health_conditions": health_conditions,
        "accessibility_needs": accessibility_needs,
        "available_hours": available_hours,
        "monthly_budget": monthly_budget,
        "independent_travel": independent_travel,
        "zip_code": zip_code,
        "activity_preferences": activity_preferences,
        "preferred_distance": preferred_distance,
        "group_size_preference": group_size_preference,
        "time_preference": time_preference,
        "language": language,
        "socialScore": socialScore
    }

    user_insert_result = collectionUser.insert_one(user_submission_data)
    user_id = user_insert_result.inserted_id  # Get the userId

    socialClassifier_submission_data = {
        "user_id": str(user_id),
        "social_score": socialScore,
        "socClas1EatWOthers" : socClas1EatWOthers,
        "socClas2HobbiesInside" : socClas2HobbiesInside,
        "socClas3HobbiesOutside": socClas3HobbiesOutside,
        "socClas4TV": socClas4TV,
        "socClas5Browsing": socClas5Browsing,
        "socClas6TalkPhone": socClas6TalkPhone,
        "socClas7MeetFamFriend": socClas7MeetFamFriend,
        "socClas8GroupConvo": socClas8GroupConvo,
        "socClas9Text": socClas9Text,
        "socClas10Volunteer": socClas10Volunteer,
        "socClas11Essential": socClas11Essential,
        "socClas1aWishPart": socClas1aWishPart,
        "socClas1bTypesOfMealsInterested": socClas1bTypesOfMealsInterested,
        "socClas1cTypesOfMealsParticipated": socClas1cTypesOfMealsParticipated,
        "socClas1dWishPartMoreActivity": socClas1dWishPartMoreActivity,
        "socClas2aWishTimeInsideHobbies": socClas2aWishTimeInsideHobbies,
        "socClas2bTypesOfInsideHobbies": socClas2bTypesOfInsideHobbies,
        "socClas2cTypesOfIndoorActivitiesParticipated": socClas2cTypesOfIndoorActivitiesParticipated,
        "socClas2dWishPartMoreIndoorActivities": socClas2dWishPartMoreIndoorActivities
    }
    
    print("socialScore: " + socialScore)

    collectionSocialClassifier.insert_one(socialClassifier_submission_data)


    return f"Form submitted successfully!"

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
@app.route('/introvertedActivities')
def introverted_activities():
    activities = collectionActivity.find({"activity_type": "Introverted"})  # Adjust the filter based on your data structure


    for activity in introverted_activities:
        print(activity.get("activity_type"))  # This will print each activity document

    return introverted_activities


def calcSocialScore(stats):

    scoring_map = {
        "never": 0,
        "1-3TimesAYear": 1,
        "quarterly": 2,
        "moreThanQuarterlyButLessThanMonthly": 3,
        "onceAMonth": 4,
        "twiceAMonth": 5,
        "moreThanTwiceAMonthButLessThanWeekly": 6,
        "1-3TimesAWeek": 7,
        "4-6TimesAWeek": 8,
        "everyDay": 9
    }


    totalScore = 0
    res = ""


    for elem in stats:
        print(elem)
        print(scoring_map.get(elem))
        totalScore = totalScore + scoring_map.get(elem)

    print(totalScore)

    if totalScore <30:
        res = "Low"
    elif totalScore <45:
        res = "Low-Medium"
    elif totalScore <60:
        res = "Medium"
    elif totalScore <70:
        res = "High"
    else:
        res = "Very High"

    return res
    

def findPrimaryDomain(socialClassifierStats):
    scoring_map = {
        "never": 0,
        "1-3TimesAYear": 1,
        "quarterly": 2,
        "moreThanQuarterlyButLessThanMonthly": 3,
        "onceAMonth": 4,
        "twiceAMonth": 5,
        "moreThanTwiceAMonthButLessThanWeekly": 6,
        "1-3TimesAWeek": 7,
        "4-6TimesAWeek": 8,
        "everyDay": 9
    }

    resActivity = ""
    resFreq = -1


    for elem in socialClassifierStats:
        print(elem)
        print(scoring_map.get(elem))
        if scoring_map.get(elem) > resFreq:
            resActivity = elem
            resFreq = scoring_map.get(elem)

    return resActivity, resFreq

def countActivitiesPerDomain(extraClassifierStatsFreq):
    domainMap = {
        "eatingMealsWithOthers",
        "spendingTimeOnHobbiesOrRecreationAtHome",
        "attendingHobbiesOrRecreationalActivitiesOutsideHome",
        "watchingTV",
        "browsingOnline",
        "talkingOnThePhoneOrVideoCall",
        "meetingFamilyFriendsOrAcquaintancesInPerson",
        "engagingInGroupConversations",
        "texting",
        "volunteeringOrHelpingOthers",
        "goingOutForEssentialActivities",
    }


    for elem in extraClassifierStatsFreq:
        pass


#Finished
def determineActiveDomain(socialClassifierStats):

    domainMap = {
        "eatingMealsWithOthers",
        "spendingTimeOnHobbiesOrRecreationAtHome",
        "attendingHobbiesOrRecreationalActivitiesOutsideHome",
        "watchingTV",
        "browsingOnline",
        "talkingOnThePhoneOrVideoCall",
        "meetingFamilyFriendsOrAcquaintancesInPerson",
        "engagingInGroupConversations",
        "texting",
        "volunteeringOrHelpingOthers",
        "goingOutForEssentialActivities",
    }

    activeDomains = []
    

    for i in range(len(socialClassifierStats)):
        if socialClassifierStats[i] != "never":
            activeDomains.append(domainMap[i])

    return activeDomains




if __name__ == '__main__':
    app.run(debug=True)
