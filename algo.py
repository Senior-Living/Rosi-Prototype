

#Step 1
#Determines which subcategory are active (meaning a at least 1 activity has a value which is not "Never")
from collections import defaultdict
import json


def determineActiveSubcategories(allActivitiesInSubcategories):

    SubCategoriesMap = [
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

    activeSubCategories = []
    activitiesForActiveSubCategories = []
    

    for i in range(len(allActivitiesInSubcategories)):
        currentSubCategories = allActivitiesInSubcategories[i]
        added = False

        for activity in currentSubCategories:
            if activity != "never" and not added:
                activeSubCategories.append(SubCategoriesMap[i])
                activitiesForActiveSubCategories.append(currentSubCategories)
                added = True


    return activeSubCategories,activitiesForActiveSubCategories

#Step 2

def countActivitiesPerSubCategories(allActivitiesInActiveSubCategories,activeSubCategories):
    subCategoriesMap = [
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

    for i in range(len(allActivitiesInActiveSubCategories)):
        currentSubCategory = allActivitiesInActiveSubCategories[i]
        sumOfActivities = 0

        for activity in currentSubCategory:
            value = freqMap[activity]
            sumOfActivities = sumOfActivities + value

        sumOfActivities = sumOfActivities * subCatNormalizedScore[activeSubCategories[i]]

        res.append([activeSubCategories[i],sumOfActivities])

    res.sort(key=lambda x: x[1], reverse=True)

    return res
        
#Step 3 Find Primary Sub Cat (Unused)
def findPrimarySubCategories(freqPerSubCategories):

    #Error handling
    if freqPerSubCategories and len(freqPerSubCategories) > 0 and len(freqPerSubCategories[0]) >= 2:
        #Return #1 subcat 
        return freqPerSubCategories[0][0], freqPerSubCategories[0][1]
    else:
        return None, None
    
#Step 4 Determine Current Engagement Range
def determineCurrentEngagementRange(freqPerSubCategories, allSocClasDesires):
    engagementScore = 0
    engagementRange = ""
    subcategoriesRecommendations = []

    #Get our variables for readability
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

    #Sume the freqs 
    for elem in freqPerSubCategories:
        engagementScore = engagementScore + elem[1]

    #If the score is in a range 
    if engagementScore < 0.121:
        #Assign a range string
        engagementRange = "Not Engaged"

        #Conditions which are needed ordered by priority 
        conditions = [
            socClas7aMoreMeetFFA,
            socClas3aHobbiesOutside,
            socClas1aEatWOthers,
            socClas2aHobbiesInside,
            socClas6aTalkPhone,
            socClas9aText,
        ]

        #Num of subcats selected (Max 3)
        true_count = 0

        #Sum up the natural true counts
        for elem in conditions:
            if elem == "Yes":
                true_count = true_count + 1


        # Keep adding conditions until true_count == 3
        i = 0  # Start from the first condition
        while true_count < 3 and i < len(conditions):
            if conditions[i] == "No":  # If the condition is No
                conditions[i] = "Yes"  # Set it to Yes
                true_count += 1  # Increment true_count
            i += 1

        #If Yes, add to a potential output
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

        conditions = [
            socClas2aHobbiesInside,
            socClas1aEatWOthers,
            socClas7aMoreMeetFFA,
            socClas9aText,
            socClas6aTalkPhone,
            socClas3aHobbiesOutside,
            socClas8aGroupConvo,
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
            activityToFreqMapping["Indoor Hobbies"] = "Once a Week"
            setOfSubCategories.append("Indoor Hobbies")

        if conditions[1]  == "Yes":
            activityToFreqMapping["Social Dining"] = "Twice a Month"
            setOfSubCategories.append("Social Dining")

        if conditions[2]  == "Yes":
            activityToFreqMapping["Meeting People"] = "Twice a Month"
            setOfSubCategories.append("Meeting People")

        if conditions[3]  == "Yes":
            activityToFreqMapping["Texting People"] = "Once a Week"
            setOfSubCategories.append("Texting People")

        if conditions[4]  == "Yes":
            activityToFreqMapping["Phone Calls"] = "Once a Week"
            setOfSubCategories.append("Phone Calls")
        
        if conditions[5]  == "Yes":
            activityToFreqMapping["Outdoor Hobbies"] = "Once a Week"
            setOfSubCategories.append("Outdoor Hobbies")

        if conditions[6]  == "Yes":
            activityToFreqMapping["Group Conversations"] = "Once a Month"
            setOfSubCategories.append("Group Conversations")

    elif engagementScore < 1.500:
        engagementRange = "Moderately Engaged"

        conditions = [
            socClas10aVolunteer,
            socClas8aGroupConvo,
            socClas3aHobbiesOutside,
            socClas1aEatWOthers,
            socClas7aMoreMeetFFA,
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
            activityToFreqMapping["Volunteering"] = "Once a Month"
            setOfSubCategories.append("Volunteering")

        if conditions[1]  == "Yes":
            activityToFreqMapping["Group Conversations"] = "Once a Week"
            setOfSubCategories.append("Group Conversations")

        if conditions[2]  == "Yes":
            activityToFreqMapping["Outdoor Hobbies"] = "Once a Week"
            setOfSubCategories.append("Outdoor Hobbies")

        if conditions[3]  == "Yes":
            activityToFreqMapping["Social Dining"] = "Once a Week"
            setOfSubCategories.append("Social Dining")

        if conditions[4]  == "Yes":
            activityToFreqMapping["Meeting People"] = "Once a Week"
            setOfSubCategories.append("Meeting People")

    elif engagementScore < 3.500:
        engagementRange = "Highly Engaged"

        conditions = [
            socClas10aVolunteer,
            socClas8aGroupConvo,
            socClas3aHobbiesOutside,
            socClas1aEatWOthers,
            socClas7aMoreMeetFFA,
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
            activityToFreqMapping["Volunteering"] = "Once a Week"
            setOfSubCategories.append("Volunteering")

        if conditions[1]  == "Yes":
            activityToFreqMapping["Group Conversations"] = "Once a Week"
            setOfSubCategories.append("Group Conversations")

        if conditions[2]  == "Yes":
            activityToFreqMapping["Outdoor Hobbies"] = "Twice a Week"
            setOfSubCategories.append("Outdoor Hobbies")

        if conditions[3]  == "Yes":
            activityToFreqMapping["Social Dining"] = "Once a Week"
            setOfSubCategories.append("Social Dining")

        if conditions[4]  == "Yes":
            activityToFreqMapping["Meeting People"] = "Once a Week"
            setOfSubCategories.append("Meeting People")

    else:
        engagementRange = "Very Highly Engaged"


    indexFreqPerSubCategories = 0

    while len(subcategoriesRecommendations) < 3 and indexFreqPerSubCategories < len(freqPerSubCategories):

        currentSubCat = freqPerSubCategories[indexFreqPerSubCategories]
        nameOfSubCat = currentSubCat[0]

        if nameOfSubCat in setOfSubCategories and nameOfSubCat not in subcategoriesRecommendations:
            frequency = activityToFreqMapping.get(nameOfSubCat, "Frequency Not Available")  # Default if no mapping found
            subcategoriesRecommendations.append((nameOfSubCat, frequency))  # Append a tuple with activity name and frequency

        indexFreqPerSubCategories+=1


    while len(subcategoriesRecommendations) < 3:
        for elem in setOfSubCategories:
            if elem not in subcategoriesRecommendations:
                frequency = activityToFreqMapping.get(elem, "Frequency Not Available")  # Default if no mapping found
                subcategoriesRecommendations.append((elem, frequency))  # Append a tuple with activity name and frequency

            if len(subcategoriesRecommendations) == 3:
                break

    return engagementScore, engagementRange, subcategoriesRecommendations

#Step 5
def getSubCategoriesActivities(subcategories):
    #Opens files and loads data
    with open("storagefiles/activities.json", 'r') as file:
        activities_data = json.load(file)


    activities_by_subcategory = defaultdict(list)
    freqList = []

    #Remove the Freq for now
    for subcategory in subcategories:
        activities_by_subcategory[subcategory[0]] = []
        freqList.append(subcategory[1])

    #For every entry
    for entry in activities_data:
        #get the subcat
        subcategory = entry.get("Sub-Category")

        #if the subcat matches with something we are looking for
        if subcategory in activities_by_subcategory:
            #Add to semi-final Array 
            activities_by_subcategory[subcategory].append(entry.get("Activity"))

    result = {}
    
    #Pointer for the freqs
    freqListIndex = 0

    #For every subcat
    #Adding back in the freq
    for subcategory, activities in activities_by_subcategory.items():
        result[(subcategory,freqList[freqListIndex])] = activities
        freqListIndex+= 1

    return result
