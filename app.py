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

    socialActivities1 = [
        socialActivity1communityDining,
        socialActivity1teaAndCoffeeSocials,
        socialActivity1birthdayAnniversaryMeals,
        socialActivity1buffetOrBrunchGatherings,
        socialActivity1holidayFeastEvents,
        socialActivity1outdoorBBQs,
        socialActivity1picnicLunches,
        socialActivity1familyBBQDay,
        socialActivity1iceCreamSocials,
        socialActivity1happyhour
    ]

    socialActivity2readingBooks = request.form.get('2readingBooks')
    socialActivity2knittingAndCrochet = request.form.get('2knittingAndCrochet')
    socialActivity2gardening = request.form.get('2gardening')
    socialActivity2listeningToMusic = request.form.get('2listeningToMusic')
    socialActivity2watchingMoviesTvShows = request.form.get('2watchingMoviesTvShows')
    socialActivity2playingPuzzleOrGames = request.form.get('2playingPuzzleOrGames')
    socialActivity2craftingOrPainting = request.form.get('2craftingOrPainting')
    socialActivity2cookingBaking = request.form.get('2cookingBaking')
    socialActivity2photography = request.form.get('2photography')
    socialActivity2writing = request.form.get('2writing')
    socialActivity2brainGamesMemoryExercises = request.form.get('2brainGamesMemoryExercises')
    socialActivity2meditationRelaxation = request.form.get('2meditationRelaxation')
    socialActivity2indoorBowlingGolfPutting = request.form.get('2indoorBowlingGolfPutting')
    socialActivity2learningNewSkills = request.form.get('2learningNewSkills')
    socialActivity2exercising = request.form.get('2exercising')

    socialActivities2 = [
        socialActivity2readingBooks,
        socialActivity2knittingAndCrochet,
        socialActivity2gardening,
        socialActivity2listeningToMusic,
        socialActivity2watchingMoviesTvShows,
        socialActivity2playingPuzzleOrGames,
        socialActivity2craftingOrPainting,
        socialActivity2cookingBaking,
        socialActivity2photography,
        socialActivity2writing,
        socialActivity2brainGamesMemoryExercises,
        socialActivity2meditationRelaxation,
        socialActivity2indoorBowlingGolfPutting,
        socialActivity2learningNewSkills,
        socialActivity2exercising
    ]

    socialActivity3bookClubs = request.form.get('bookClubs')
    socialActivity3knittingClubs = request.form.get('knittingClubs')
    socialActivity3gardeningClubs = request.form.get('gardeningClubs')
    socialActivity3attendingExerciseOrFitnessClasses = request.form.get('attendingExerciseOrFitnessClasses')
    socialActivity3gentleExerciseClasses = request.form.get('gentleExerciseClasses')
    socialActivity3walkingGroups = request.form.get('walkingGroups')
    socialActivity3walkingAloneOrWithAPet = request.form.get('walkingAloneOrWithAPet')
    socialActivity3chairExercisesForLimitedMobility = request.form.get('chairExercisesForLimitedMobility')
    socialActivity3dancingSessionsWithMusicFromTheirEra = request.form.get('dancingSessionsWithMusicFromTheirEra')
    socialActivity3attendingMusicConcertsOrPerformances = request.form.get('attendingMusicConcertsOrPerformances')
    socialActivity3theaterOrMovieOutings = request.form.get('theaterOrMovieOutings')
    socialActivity3attendingCommunityCenterClasses = request.form.get('attendingCommunityCenterClasses')
    socialActivity3tripsToMuseumsOrArtGalleries = request.form.get('tripsToMuseumsOrArtGalleries')
    socialActivity3outdoorPhotographyExcursions = request.form.get('outdoorPhotographyExcursions')
    socialActivity3participatingInGroupTravelOrDayTrips = request.form.get('participatingInGroupTravelOrDayTrips')
    socialActivity3shortBikeRide = request.form.get('shortBikeRide')
    socialActivity3artAndCraftWorkshops = request.form.get('artAndCraftWorkshops')
    socialActivity3educationalTalksAndLectures = request.form.get('educationalTalksAndLectures')

    socialActivities3 = [
        socialActivity3bookClubs,
        socialActivity3knittingClubs,
        socialActivity3gardeningClubs,
        socialActivity3attendingExerciseOrFitnessClasses,
        socialActivity3gentleExerciseClasses,
        socialActivity3walkingGroups,
        socialActivity3walkingAloneOrWithAPet,
        socialActivity3chairExercisesForLimitedMobility,
        socialActivity3dancingSessionsWithMusicFromTheirEra,
        socialActivity3attendingMusicConcertsOrPerformances,
        socialActivity3theaterOrMovieOutings,
        socialActivity3attendingCommunityCenterClasses,
        socialActivity3tripsToMuseumsOrArtGalleries,
        socialActivity3outdoorPhotographyExcursions,
        socialActivity3participatingInGroupTravelOrDayTrips,
        socialActivity3shortBikeRide,
        socialActivity3artAndCraftWorkshops,
        socialActivity3educationalTalksAndLectures
    ]

    socialActivity4news = request.form.get('news')
    socialActivity4tvShows = request.form.get('tvShows')
    socialActivity4documentaries = request.form.get('documentaries')
    socialActivity4movies = request.form.get('movies')
    socialActivity4sports = request.form.get('sports')
    socialActivity4youTubeVideos = request.form.get('youTubeVideos')

    socialActivities4 = [
        socialActivity4news,
        socialActivity4tvShows,
        socialActivity4documentaries,
        socialActivity4movies,
        socialActivity4sports,
        socialActivity4youTubeVideos
    ]

    socialActivity5newsWebsites = request.form.get('newsWebsites')
    socialActivity5socialMedia = request.form.get('socialMedia')
    socialActivity5blogsOrArticles = request.form.get('blogsOrArticles')
    socialActivity5onlineForumsOrDiscussionGroups = request.form.get('onlineForumsOrDiscussionGroups')
    socialActivity5shoppingSites = request.form.get('shoppingSites')

    socialActivities5 = [
        socialActivity5newsWebsites,
        socialActivity5socialMedia,
        socialActivity5blogsOrArticles,
        socialActivity5onlineForumsOrDiscussionGroups,
        socialActivity5shoppingSites
    ]

    socialActivity6spouseOrPartner = request.form.get('spouseOrPartner')
    socialActivity6family = request.form.get('family')
    socialActivity6friends = request.form.get('friends')
    socialActivity6acquaintances = request.form.get('acquaintances')
    socialActivity6healthOrServiceProviders = request.form.get('healthOrServiceProviders')

    socialActivities6 = [
        socialActivity6spouseOrPartner,
        socialActivity6family,
        socialActivity6friends,
        socialActivity6acquaintances,
        socialActivity6healthOrServiceProviders
    ]

    socialActivity7atHome = request.form.get('atHome')
    socialActivity7atFriendFamilyHome = request.form.get('atFriendFamilyHome')
    socialActivity7atOutdoorLocation = request.form.get('atOutdoorLocation')
    socialActivity7atRestaurantCafe = request.form.get('atRestaurantCafe')

    socialActivities7 = [
        socialActivity7atHome,
        socialActivity7atFriendFamilyHome,
        socialActivity7atOutdoorLocation,
        socialActivity7atRestaurantCafe
    ]
    
    socialActivity8InPersonFamilyOrFriendsGatherings = request.form.get('InPersonFamilyOrFriendsGatherings')
    socialActivity8InPersonHobbyOrCommunityGroups = request.form.get('InPersonHobbyOrCommunityGroups')
    socialActivity8OnlineVideoCallsDiscussionForums = request.form.get('OnlineVideoCallsDiscussionForums')

    socialActivities8 = [
        socialActivity8InPersonFamilyOrFriendsGatherings,
        socialActivity8InPersonHobbyOrCommunityGroups,
        socialActivity8OnlineVideoCallsDiscussionForums
    ]
    
    socialActivity9sms = request.form.get('sms')
    socialActivity9whatsApp = request.form.get('whatsApp')
    socialActivity9facebookMessenger = request.form.get('facebookMessenger')
    socialActivity9iMessage = request.form.get('iMessage')

    socialActivities9 = [
        socialActivity9sms,
        socialActivity9whatsApp,
        socialActivity9facebookMessenger,
        socialActivity9iMessage
    ]

    socialActivity10supportingFamilyFriendsOrCommunityMembers = request.form.get('supportingFamilyFriendsOrCommunityMembers')
    socialActivity10communityAndEnvironmentalProjects = request.form.get('communityAndEnvironmentalProjects')
    socialActivity10mentoringTutoringAndEducationSupport = request.form.get('mentoringTutoringAndEducationSupport')
    socialActivity10charityAndFundraisingActivities = request.form.get('charityAndFundraisingActivities')
    socialActivity10directAssistanceToVulnerablePopulations = request.form.get('directAssistanceToVulnerablePopulations')
    socialActivity10foodAndEssentialsDistribution = request.form.get('foodAndEssentialsDistribution')
    socialActivity10artsAndCulturalEventSupport = request.form.get('artsAndCulturalEventSupport')
    socialActivity10animalWelfareVolunteering = request.form.get('animalWelfareVolunteering')
    socialActivity10advocacyAndCampaigningForSocialCauses = request.form.get('advocacyAndCampaigningForSocialCauses')
    socialActivity10virtualVolunteering = request.form.get('virtualVolunteering')

    socialActivities10 = [
        socialActivity10supportingFamilyFriendsOrCommunityMembers,
        socialActivity10communityAndEnvironmentalProjects,
        socialActivity10mentoringTutoringAndEducationSupport,
        socialActivity10charityAndFundraisingActivities,
        socialActivity10directAssistanceToVulnerablePopulations,
        socialActivity10foodAndEssentialsDistribution,
        socialActivity10artsAndCulturalEventSupport,
        socialActivity10animalWelfareVolunteering,
        socialActivity10advocacyAndCampaigningForSocialCauses,
    ]

    socialActivity11groceryShopping = request.form.get('groceryShopping')
    socialActivity11medicalAppointments = request.form.get('medicalAppointments')
    socialActivity11pharmacyVisits = request.form.get('pharmacyVisits')
    socialActivity11bankingOrPostOffice = request.form.get('bankingOrPostOffice')

    socialActivities11 = [
        socialActivity11groceryShopping,
        socialActivity11medicalAppointments,
        socialActivity11pharmacyVisits,
        socialActivity11bankingOrPostOffice
    ]

    print("Social Classifier Information")

    print("Question 1")

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


    print("Question 2")

    print(f"  Reading Books: {socialActivity2readingBooks}")
    print(f"  Knitting and Crochet: {socialActivity2knittingAndCrochet}")
    print(f"  Gardening: {socialActivity2gardening}")
    print(f"  Listening to Music: {socialActivity2listeningToMusic}")
    print(f"  Watching Movies/TV Shows: {socialActivity2watchingMoviesTvShows}")
    print(f"  Playing Puzzle or Games: {socialActivity2playingPuzzleOrGames}")
    print(f"  Crafting or Painting: {socialActivity2craftingOrPainting}")
    print(f"  Cooking/Baking: {socialActivity2cookingBaking}")
    print(f"  Photography: {socialActivity2photography}")
    print(f"  Writing: {socialActivity2writing}")
    print(f"  Brain Games/Memory Exercises: {socialActivity2brainGamesMemoryExercises}")
    print(f"  Meditation/Relaxation: {socialActivity2meditationRelaxation}")
    print(f"  Indoor Bowling/Golf Putting: {socialActivity2indoorBowlingGolfPutting}")
    print(f"  Learning New Skills: {socialActivity2learningNewSkills}")
    print(f"  Exercising: {socialActivity2exercising}")

    print("Question 3")

    print(f"  Book Clubs: {socialActivity3bookClubs}")
    print(f"  Knitting Clubs: {socialActivity3knittingClubs}")
    print(f"  Gardening Clubs: {socialActivity3gardeningClubs}")
    print(f"  Attending Exercise or Fitness Classes: {socialActivity3attendingExerciseOrFitnessClasses}")
    print(f"  Gentle Exercise Classes: {socialActivity3gentleExerciseClasses}")
    print(f"  Walking Groups: {socialActivity3walkingGroups}")
    print(f"  Walking Alone or With a Pet: {socialActivity3walkingAloneOrWithAPet}")
    print(f"  Chair Exercises for Limited Mobility: {socialActivity3chairExercisesForLimitedMobility}")
    print(f"  Dancing Sessions with Music from Their Era: {socialActivity3dancingSessionsWithMusicFromTheirEra}")
    print(f"  Attending Music Concerts or Performances: {socialActivity3attendingMusicConcertsOrPerformances}")
    print(f"  Theater or Movie Outings: {socialActivity3theaterOrMovieOutings}")
    print(f"  Attending Community Center Classes: {socialActivity3attendingCommunityCenterClasses}")
    print(f"  Trips to Museums or Art Galleries: {socialActivity3tripsToMuseumsOrArtGalleries}")
    print(f"  Outdoor Photography Excursions: {socialActivity3outdoorPhotographyExcursions}")
    print(f"  Participating in Group Travel or Day Trips: {socialActivity3participatingInGroupTravelOrDayTrips}")
    print(f"  Short Bike Ride: {socialActivity3shortBikeRide}")
    print(f"  Art and Craft Workshops: {socialActivity3artAndCraftWorkshops}")
    print(f"  Educational Talks and Lectures: {socialActivity3educationalTalksAndLectures}")

    print("Question 4")

    print(f"  News: {socialActivity4news}")
    print(f"  TV Shows: {socialActivity4tvShows}")
    print(f"  Documentaries: {socialActivity4documentaries}")
    print(f"  Movies: {socialActivity4movies}")
    print(f"  Sports: {socialActivity4sports}")
    print(f"  YouTube Videos: {socialActivity4youTubeVideos}")

    print("Question 5")

    print(f"  News Websites: {socialActivity5newsWebsites}")
    print(f"  Social Media: {socialActivity5socialMedia}")
    print(f"  Blogs or Articles: {socialActivity5blogsOrArticles}")
    print(f"  Online Forums or Discussion Groups: {socialActivity5onlineForumsOrDiscussionGroups}")
    print(f"  Shopping Sites: {socialActivity5shoppingSites}")

    print("Question 6")

    print(f"  Spouse or Partner: {socialActivity6spouseOrPartner}")
    print(f"  Family: {socialActivity6family}")
    print(f"  Friends: {socialActivity6friends}")
    print(f"  Acquaintances: {socialActivity6acquaintances}")
    print(f"  Health or Service Providers: {socialActivity6healthOrServiceProviders}")

    print("Question 7")

    print(f"  At Home: {socialActivity7atHome}")
    print(f"  At Friend or Family Home: {socialActivity7atFriendFamilyHome}")
    print(f"  At Outdoor Location: {socialActivity7atOutdoorLocation}")
    print(f"  At Restaurant or Cafe: {socialActivity7atRestaurantCafe}")


    print("Question 8")

    print(f"  In-Person Family or Friends Gatherings: {socialActivity8InPersonFamilyOrFriendsGatherings}")
    print(f"  In-Person Hobby or Community Groups: {socialActivity8InPersonHobbyOrCommunityGroups}")
    print(f"  Online Video Calls or Discussion Forums: {socialActivity8OnlineVideoCallsDiscussionForums}")

    print("Question 9")

    print(f"  SMS: {socialActivity9sms}")
    print(f"  WhatsApp: {socialActivity9whatsApp}")
    print(f"  Facebook Messenger: {socialActivity9facebookMessenger}")
    print(f"  iMessage: {socialActivity9iMessage}")

    print("Question 10")

    print(f"  Supporting Family, Friends, or Community Members: {socialActivity10supportingFamilyFriendsOrCommunityMembers}")
    print(f"  Community and Environmental Projects: {socialActivity10communityAndEnvironmentalProjects}")
    print(f"  Mentoring, Tutoring, and Education Support: {socialActivity10mentoringTutoringAndEducationSupport}")
    print(f"  Charity and Fundraising Activities: {socialActivity10charityAndFundraisingActivities}")
    print(f"  Direct Assistance to Vulnerable Populations: {socialActivity10directAssistanceToVulnerablePopulations}")
    print(f"  Food and Essentials Distribution: {socialActivity10foodAndEssentialsDistribution}")
    print(f"  Arts and Cultural Event Support: {socialActivity10artsAndCulturalEventSupport}")
    print(f"  Animal Welfare Volunteering: {socialActivity10animalWelfareVolunteering}")
    print(f"  Advocacy and Campaigning for Social Causes: {socialActivity10advocacyAndCampaigningForSocialCauses}")
    print(f"  Virtual Volunteering: {socialActivity10virtualVolunteering}")

    print("Question 11")

    print(f"  Grocery Shopping: {socialActivity11groceryShopping}")
    print(f"  Medical Appointments: {socialActivity11medicalAppointments}")
    print(f"  Pharmacy Visits: {socialActivity11pharmacyVisits}")
    print(f"  Banking or Post Office: {socialActivity11bankingOrPostOffice}")


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

    allActivitiesInDomains = [
        socialActivities1, 
        socialActivities2, 
        socialActivities3, 
        socialActivities4, 
        socialActivities5, 
        socialActivities6, 
        socialActivities7, 
        socialActivities8, 
        socialActivities9, 
        socialActivities10, 
        socialActivities11
    ]

    #Step 1 Done
    activeDomains,allActivitiesInActiveDomains  = determineActiveDomain(allActivitiesInDomains)

    print("Step 1: Active Domains")
    print(activeDomains)
    print(allActivitiesInActiveDomains)

    #Step 2
    freqPerDomain = countActivitiesPerDomain(allActivitiesInActiveDomains, activeDomains)

    print("Step 2: Frequency Per Domain")
    print(freqPerDomain)

    #Step 3
    primaryDomain, primaryDomainFreq = findPrimaryDomain(freqPerDomain)

    print("Step 3: Primary Domain")
    print(primaryDomain)
    print(primaryDomainFreq)



    
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

#Step 3 
def findPrimaryDomain(freqPerDomain):

    kingDomain = ""
    kingValue = 0

    for elem in freqPerDomain:
        if elem[1] > kingValue:
            kingDomain = elem[0]
            kingValue = elem[1]

    return kingDomain,kingValue



#Step 2 Finished
def countActivitiesPerDomain(allActivitiesInActiveDomains,activeDomains):
    domainMap = [
        "1. eatingMealsWithOthers",
        "2. spendingTimeOnHobbiesOrRecreationAtHome",
        "3. attendingHobbiesOrRecreationalActivitiesOutsideHome",
        "4. watchingTV",
        "5. browsingOnline",
        "6. talkingOnThePhoneOrVideoCall",
        "7. meetingFamilyFriendsOrAcquaintancesInPerson",
        "8. engagingInGroupConversations",
        "9. texting",
        "10. volunteeringOrHelpingOthers",
        "11. goingOutForEssentialActivities",
    ]

    freqMap = {
        "never" : 0,
        "1-3TimesAYear": 2/365,
        "onceInThreeMonths": 4/365,
        "twiceInThreeMonths": 8/365,
        "onceAMonth": 12/365,
        "twiceAMonth": 24/365,
        "threeTimesAMonth": 36/365,
        "1-3TimesAWeek": 104/365,
        "4-6TimesAWeek": 260/365,
        "everyDay": 1,
    }

    subCatNormalizedScore = {
        "1. eatingMealsWithOthers": 0.6,
        "2. spendingTimeOnHobbiesOrRecreationAtHome": 0.5,
        "3. attendingHobbiesOrRecreationalActivitiesOutsideHome": 0.7,
        "4. watchingTV": 0,
        "5. browsingOnline": 0.1,
        "6. talkingOnThePhoneOrVideoCall": 0.4,
        "7. meetingFamilyFriendsOrAcquaintancesInPerson": 0.8,
        "8. engagingInGroupConversations": 0.9,
        "9. texting": 0.2,
        "10. volunteeringOrHelpingOthers": 1,
        "11. goingOutForEssentialActivities": 0.3,
    }

    

    res = []


    

    for i in range(len(allActivitiesInActiveDomains)):
        currentDomain = allActivitiesInActiveDomains[i]
        sumOfActivities = 0

        for activity in currentDomain:
            value = freqMap[activity]
            sumOfActivities = sumOfActivities + value

        sumOfActivities = sumOfActivities * subCatNormalizedScore[activeDomains[i]]

        res.append([activeDomains[i],sumOfActivities])

    return res
        
            

#Finished
#Step 1
def determineActiveDomain(allActivitiesInDomains):

    domainMap = [
        "1. eatingMealsWithOthers",
        "2. spendingTimeOnHobbiesOrRecreationAtHome",
        "3. attendingHobbiesOrRecreationalActivitiesOutsideHome",
        "4. watchingTV",
        "5. browsingOnline",
        "6. talkingOnThePhoneOrVideoCall",
        "7. meetingFamilyFriendsOrAcquaintancesInPerson",
        "8. engagingInGroupConversations",
        "9. texting",
        "10. volunteeringOrHelpingOthers",
        "11. goingOutForEssentialActivities",
    ]

    activeDomains = []
    activitiesForActiveDomains = []
    

    for i in range(len(allActivitiesInDomains)):
        currentDomain = allActivitiesInDomains[i]
        added = False

        for activity in currentDomain:
            if activity != "never" and not added:
                activeDomains.append(domainMap[i])
                activitiesForActiveDomains.append(currentDomain)
                added = True


    return activeDomains,activitiesForActiveDomains




if __name__ == '__main__':
    app.run(debug=True)
