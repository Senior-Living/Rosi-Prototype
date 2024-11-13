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

@app.route('/addPrescriptionDemographic')
def addPrescriptionDemographic():
    return render_template('addPrescriptionDemographic.html')

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

    socClas1aEatWOthers = request.form.get('socClas1aEatWOthers')    
    socClas2aHobbiesInside = request.form.get('socClas2aHobbiesInside')    
    socClas3aHobbiesOutside = request.form.get('socClas3aHobbiesOutside')    
    socClas4aTV = request.form.get('socClas4aTV')    
    socClas5aBrowsing = request.form.get('socClas5aBrowsing')    
    socClas6aTalkPhone = request.form.get('socClas6aTalkPhone')    
    socClas7aMoreMeetFFA = request.form.get('socClas7aMoreMeetFFA')    
    socClas8aGroupConvo = request.form.get('socClas8aGroupConvo')    
    socClas9aText = request.form.get('socClas9aText')    
    socClas10aVolunteer = request.form.get('socClas10aVolunteer')    
    socClas11aEssential = request.form.get('socClas11aEssential')  

    socialActivity1communityDining = request.form.get('1communityDining')
    socialActivity1teaAndCoffeeSocials = request.form.get('1teaAndCoffeeSocials')
    socialActivity1birthdayAnniversaryMeals = request.form.get('1birthdayAnniversaryMeals')
    socialActivity1buffetOrBrunchGatherings = request.form.get('1buffetOrBrunchGatherings')
    socialActivity1holidayFeastEvents = request.form.get('1holidayFeastEvents')
    socialActivity1outdoorBBQs = request.form.get('1outdoorBBQs')
    socialActivity1picnicLunches = request.form.get('1picnicLunches')
    socialActivity1familyBBQDay = request.form.get('1familyBBQDay')
    socialActivity1iceCreamSocials = request.form.get('1iceCreamSocials')
    socialActivity1happyhour = request.form.get('1happyhour')


    print(f"  Community Dining: {socialActivity1communityDining}")
    print(f"  Tea and Coffee Socials: {socialActivity1teaAndCoffeeSocials}")
    print(f"  Birthday/Anniversary Meals: {socialActivity1birthdayAnniversaryMeals}")
    print(f"  Buffet or Brunch Gatherings: {socialActivity1buffetOrBrunchGatherings}")
    print(f"  Holiday Feast Events: {socialActivity1holidayFeastEvents}")
    print(f"  Outdoor BBQs: {socialActivity1outdoorBBQs}")
    print(f"  Picnic Lunches: {socialActivity1picnicLunches}")
    print(f"  Family BBQ Day: {socialActivity1familyBBQDay}")
    print(f"  Ice Cream Socials: {socialActivity1iceCreamSocials}")
    print(f"  Happy Hour: {socialActivity1happyhour}")





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


    print(f"1a. Wish to participate in meals or social dining events: {socClas1aEatWOthers}")

    print(f"2a. Wish to spend time on hobbies or recreational activities inside the home: {socClas2aHobbiesInside}")

    print("Hobbies Outside 3a:", socClas3aHobbiesOutside or "Not provided")


    print("TV 4a:", socClas4aTV)


    print("Browsing 5a:", socClas5aBrowsing or "Not provided")


    print("Talk Phone 6a:", socClas6aTalkPhone or "Not provided")


    print("Meet FFA 7a:", socClas7aMoreMeetFFA or "Not provided")


    print("Group Conversation 8a:", socClas8aGroupConvo or "Not provided")


    print("Text 9a:", socClas9aText or "Not provided")


    print("Volunteer 10a:", socClas10aVolunteer or "Not provided")


    print("Essential 11a:", socClas11aEssential or "Not provided")




    # socialClassifierStats = [
    #     socClas1EatWOthers,
    #     socClas2HobbiesInside,
    #     socClas3HobbiesOutside,
    #     socClas4TV,
    #     socClas5Browsing,
    #     socClas6TalkPhone,
    #     socClas7MeetFamFriend,
    #     socClas8GroupConvo,
    #     socClas9Text,
    #     socClas10Volunteer,
    #     socClas11Essential
    # ]


    #Step 1
    #activeDomains = determineActiveDomain(socialClassifierStats)

    #Step 2
    #freqPerDomain = countActivitiesPerDomain(extraClassifierStatsFreq)

    #Step 3
    #pointsPerDomain = determineScorePerDomain(freqPerDomain,extraClassifierStatsFreq)


    #Step 4
    #primaryDomain, primaryDomainFreq = findPrimaryDomain(socialClassifierStats)



    
    # print(primaryDomain)
    # print(primaryDomainFreq)
    # #print(freqPerDomain)

    # socialScore = calcSocialScore(socialClassifierStats)


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
        #"socialScore": socialScore
    }

    user_insert_result = collectionUser.insert_one(user_submission_data)
    user_id = user_insert_result.inserted_id  # Get the userId


    

    #collectionSocialClassifier.insert_one(socialClassifier_submission_data)


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
        "twiceInThreeMonths": 3,
        "onceAMonth": 4,
        "twiceAMonth": 5,
        "threeTimesAMonth": 6,
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
    
#Finished
#Step 3
def findPrimaryDomain(socialClassifierStats):
    scoring_map = {
        "never": 0,
        "1-3TimesAYear": 1,
        "quarterly": 2,
        "twiceInThreeMonths": 3,
        "onceAMonth": 4,
        "twiceAMonth": 5,
        "threeTimesAMonth": 6,
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

#Step 2
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
#Step 1
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
