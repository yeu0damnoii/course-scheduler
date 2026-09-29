import random
import json

classes = ["comp1002Tut","comp1002Prac",
           "comp1015Tut",
           "comp1003Forum","comp1003Prac",
           "info1012Tut","info1012Prac","info1012Stu"]

courseClasses={}
classesNumber= list(range(50000,50999))
classesStart=list(range(8,17))
for i in range(len(classesStart)):
    classesStart[i] +=0.1
#classesStart = [8.1, 9.1, 10.1, 11.1, 12.1, 13.1, 14.1, 15.1, 16.1]
for Class in classes: #pick a class to gen data
    availableSchedules = random.randint(2,6) #number of availble time for a class
    classSessions=[] #dict obj that hold all the possible schedule of a class
    numberOfSession = random.randint(1,2) #random the number of session for a class
    for _ in range(availableSchedules):
        SpecificClassesDayList= [1,2,3,4,5] #monday, tuesday, wednesday, thursday, friday
        classData={} #create a dict to store the data of each class (classnumber,session (day/start/end)*snumberOfsession)
        classNumber = random.choice(classesNumber)  #gen a classnumber, make sure it is unique
        classesNumber.remove(classNumber)           #
        classData["classNumber"] = classNumber      #
        listOfSession = [] #create a list to store each session data of all the sessions a class has 
        for _ in range(numberOfSession):                    #consider each session
            classtime={}                                    #add day,time for that session
            classtime["day"]=random.choice(SpecificClassesDayList)
            SpecificClassesDayList.remove(classtime["day"]) #make sure all the session of a class wont be on the same day and clash
            classtime["start"]=random.choice(classesStart)
            classtime["end"] = classtime["start"] + 1.9
            listOfSession.append(classtime)                 #saved that session to the list created beyond
        classData["session"] = listOfSession                #add the key-value pair "session" to the class
        classSessions.append(classData)
    courseClasses[Class] = classSessions
with open("data/course.json", 'w') as f:
    json.dump(courseClasses, f, indent=2)



    
