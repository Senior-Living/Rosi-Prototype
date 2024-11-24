from collections import defaultdict
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




@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/addUser')
def page1():
    return render_template('addUser.html')

@app.route('/addPrescriptionDemographic')
def addPrescriptionDemographic():
    return render_template('addPrescriptionDemographic.html')

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

    print(f"1a. Eat with Others: {socClas1aEatWOthers or 'Not provided'}")
    print(f"2a. Hobbies Inside: {socClas2aHobbiesInside or 'Not provided'}")
    print(f"3a. Hobbies Outside: {socClas3aHobbiesOutside or 'Not provided'}")
    print(f"4a. TV: {socClas4aTV or 'Not provided'}")
    print(f"5a. Browsing: {socClas5aBrowsing or 'Not provided'}")
    print(f"6a. Talk Phone: {socClas6aTalkPhone or 'Not provided'}")
    print(f"7a. Meet FFA: {socClas7aMoreMeetFFA or 'Not provided'}")
    print(f"8a. Group Conversation: {socClas8aGroupConvo or 'Not provided'}")
    print(f"9a. Text: {socClas9aText or 'Not provided'}")
    print(f"10a. Volunteer: {socClas10aVolunteer or 'Not provided'}")
    print(f"11a. Essential: {socClas11aEssential or 'Not provided'}")

    allSocClasDesires = [
        socClas1aEatWOthers,
        socClas2aHobbiesInside,
        socClas3aHobbiesOutside,
        socClas4aTV,
        socClas5aBrowsing,
        socClas6aTalkPhone,
        socClas7aMoreMeetFFA,
        socClas8aGroupConvo,
        socClas9aText,
        socClas10aVolunteer,
        socClas11aEssential
    ]


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
    print("freqPerDomain" + str(freqPerDomain))

    #Step 3
    primaryDomain, primaryDomainFreq = findPrimaryDomain(freqPerDomain)

    print("Step 3: Primary Domain")
    print("Primary Domain "+ str(primaryDomain))
    print("Primary Domain Freq: " + str(primaryDomainFreq))

    print("Step 3.5 Determine Current Engagement Range")
    engagementScore, engagementRange, subCategories = determineCurrentEngagementRange(freqPerDomain, allSocClasDesires)

    print("Engagement score: " + str(engagementScore))
    print("Engagement range: " + str(engagementRange))
    print("Sub Categories: " + str(subCategories))

    #Step 4

    subCategoriesWActivities = getSubCategoriesActivities(subCategories)

    print("subCategoriesWActivities" + str(subCategoriesWActivities))


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

    return render_template('askActivities.html', firstname=firstname, subCategories = subCategories, engagementRange = engagementRange, subCategoriesWActivities = subCategoriesWActivities)

@app.route('/submitActivities', methods=['POST'])
def submitActivities():
    firstname = request.form.get('firstname')  # Retrieve firstname

    selected_activities = {}
    
    # Iterate through the submitted form data
    for subcategory in request.form:
        if subcategory != "firstname":
            # Get the selected activity and its frequency
            activity = request.form[subcategory]
            frequency = request.form.get(subcategory + "_frequency")  # Assuming frequency is passed with the activity
            selected_activities[subcategory] = {"activity": activity, "frequency": frequency}
    
    # Print the selected activities for debugging purposes
    print("Selected Activities:")
    for subcategory, data in selected_activities.items():
        print(f"{subcategory}: {data['activity']} ({data['frequency']})")

    # Pass both the firstname and the selected activities (with frequency) to the next page
    return render_template('endPrescriptionPage.html', firstname=firstname, selected_activities=selected_activities)

#Step 3.5 Determine Current Engagement Range
def determineCurrentEngagementRange(freqPerDomain, allSocClasDesires):
    print("Current Engagement Range")
    print(freqPerDomain)
    engagementScore = 0
    engagementRange = ""
    subcategoriesRecommendations = []

    socClas1aEatWOthers = allSocClasDesires[0]
    socClas2aHobbiesInside = allSocClasDesires[1]
    socClas3aHobbiesOutside =  allSocClasDesires[2]
    socClas4aTV = allSocClasDesires[3]
    socClas5aBrowsing =  allSocClasDesires[4]
    socClas6aTalkPhone = allSocClasDesires[5]
    socClas7aMoreMeetFFA =  allSocClasDesires[6]
    socClas8aGroupConvo =  allSocClasDesires[7]
    socClas9aText =  allSocClasDesires[8]
    socClas10aVolunteer =  allSocClasDesires[9]
    socClas11aEssential = allSocClasDesires[10]

    activityToFreqMapping = {}
    setOfSubCategories = list()

    for elem in freqPerDomain:
        engagementScore = engagementScore + elem[1]

    if engagementScore < 0.121:
        engagementRange = "Not Engaged"

        conditions = [
            socClas7aMoreMeetFFA,
            socClas3aHobbiesOutside,
            socClas1aEatWOthers,
            socClas2aHobbiesInside,
            socClas6aTalkPhone,
            socClas9aText,
        ]

        true_count = 0

        for elem in conditions:
            if elem == "Yes":
                true_count = true_count + 1


        # Keep adding conditions until true_count == 3
        i = 0  # Start from the first condition
        while true_count < 3 and i < len(conditions):
            if conditions[i] == "No":  # If the condition is False
                conditions[i] = "Yes"  # Set it to True
                true_count += 1  # Increment true_count
            i += 1

        
        if conditions[0] == "Yes":
            activityToFreqMapping["Meeting People"] = "Once a Month"
            setOfSubCategories.append("Meeting People")

        if conditions[1]  == "Yes":
            activityToFreqMapping["Outdoor Hobbies"] = "Twice a Month"
            setOfSubCategories.append("Outdoor Hobbies")

        if conditions[2]  == "Yes":
            activityToFreqMapping["Social Dining"] = "Once a Month"
            setOfSubCategories.append("Social Dining")

        if conditions[3]  == "Yes":
            activityToFreqMapping["Indoor Hobbies"] = "Once a Week"
            setOfSubCategories.append("Indoor Hobbies")

        if conditions[4]  == "Yes":
            activityToFreqMapping["Phone Calls"] = "Twice a Week"
            setOfSubCategories.append("Phone Calls")
        
        if conditions[5]  == "Yes":
            activityToFreqMapping["Texting People"] = "Twice a Week"
            setOfSubCategories.append("Texting People")

    elif engagementScore < 0.500:
        engagementRange = "Mildy Engaged"
        subcategoriesRecommendations.append(["Indoor Hobbies","Once a Week"])
        subcategoriesRecommendations.append(["Social Dining","Twice a Month"])
        subcategoriesRecommendations.append(["Meeting People","Twice a Month"])
        subcategoriesRecommendations.append(["Texting PeopleTexting People","Once a Week"])
        subcategoriesRecommendations.append(["Phone Calls","Once a Week"])
        subcategoriesRecommendations.append(["Outdoor Hobbies","Once a Week"])
        subcategoriesRecommendations.append(["Group Conversations ","Once a Month"])

    elif engagementScore < 1.500:
        engagementRange = "Moderately Engaged"
        subcategoriesRecommendations.append(["Volunteering","Once a Month"])
        subcategoriesRecommendations.append(["Group Conversations","Once a Week"])
        subcategoriesRecommendations.append(["Outdoor Hobbies","Once a Week"])
        subcategoriesRecommendations.append(["Social Dining","Once a Week"])
        subcategoriesRecommendations.append(["Meeting People","Once a Week"])

    elif engagementScore < 3.500:
        engagementRange = "Highly Engaged"
        subcategoriesRecommendations.append(["Volunteering","Once a Week"])
        subcategoriesRecommendations.append(["Group Conversations","Once a Week"])
        subcategoriesRecommendations.append(["Outdoor Hobbies","Twice a Week"])
        subcategoriesRecommendations.append(["Social Dining","Once a Week"])
        subcategoriesRecommendations.append(["Meeting People","Once a Week"])
    else:
        engagementRange = "Very Highly Engaged"


    indexFreqPerDomain = 0

    while len(subcategoriesRecommendations) < 3 and indexFreqPerDomain < len(freqPerDomain):

        currentSubCat = freqPerDomain[indexFreqPerDomain]
        nameOfSubCat = currentSubCat[0]

        if nameOfSubCat in setOfSubCategories and nameOfSubCat not in subcategoriesRecommendations:
            frequency = activityToFreqMapping.get(nameOfSubCat, "Frequency Not Available")  # Default if no mapping found
            subcategoriesRecommendations.append((nameOfSubCat, frequency))  # Append a tuple with activity name and frequency

        indexFreqPerDomain+=1


    while len(subcategoriesRecommendations) < 3:
        for elem in setOfSubCategories:
            if elem not in subcategoriesRecommendations:
                frequency = activityToFreqMapping.get(elem, "Frequency Not Available")  # Default if no mapping found
                subcategoriesRecommendations.append((elem, frequency))  # Append a tuple with activity name and frequency

            if len(subcategoriesRecommendations) == 3:
                break

    return engagementScore, engagementRange, subcategoriesRecommendations

#Step 3 
def findPrimaryDomain(freqPerDomain):
    return freqPerDomain[0][0],freqPerDomain[0][1]




#Step 2 Finished
def countActivitiesPerDomain(allActivitiesInActiveDomains,activeDomains):
    domainMap = [
        "Social Dining",
        "Indoor Hobbies",
        "Outdoor Hobbies",
        "Watching TV",
        "Browsing Online",
        "Phone Calls",
        "Meeting People",
        "Group Conversations",
        "Texting People",
        "Volunteering",
        "Essential Activities",
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
        "Social Dining": 0.6,
        "Indoor Hobbies": 0.5,
        "Outdoor Hobbies": 0.7,
        "Watching TV": 0,
        "Browsing Online": 0.1,
        "Phone Calls": 0.4,
        "Meeting People": 0.8,
        "Group Conversations": 0.9,
        "Texting People": 0.2,
        "Volunteering": 1,
        "Essential Activities": 0.3,
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

    res.sort(key=lambda x: x[1], reverse=True)

    return res
        
            

#Finished
#Step 1
def determineActiveDomain(allActivitiesInDomains):

    domainMap = [
        "Social Dining",
        "Indoor Hobbies",
        "Outdoor Hobbies",
        "Watching TV",
        "Browsing Online",
        "Phone Calls",
        "Meeting People",
        "Group Conversations",
        "Texting People",
        "Volunteering",
        "Essential Activities",
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

#Step 4
def getSubCategoriesActivities(subcategories):
    with open("activities.json", 'r') as file:
        activities_data = json.load(file)

    activities_by_subcategory = defaultdict(list)

    freqList = []

    for subcategory in subcategories:
        activities_by_subcategory[subcategory[0]] = []
        freqList.append(subcategory[1])

    for entry in activities_data:
        subcategory = entry.get("Sub-category ")

        if subcategory in activities_by_subcategory:
            activities_by_subcategory[subcategory].append(entry.get("Activity"))

    result = {}
    freqListIndex = 0
    for subcategory, activities in activities_by_subcategory.items():
        # Use the first character of the subcategory as part of the key
        result[(subcategory,freqList[freqListIndex])] = activities
        freqListIndex+= 1

    return result


    return dict(activities_by_subcategory)



if __name__ == '__main__':
    app.run(debug=True)
