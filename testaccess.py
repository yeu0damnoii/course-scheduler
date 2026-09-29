courseoption = {
    "comp1002Tut":[
        {"classNumber":12345, "session":[ {"day":1, "start":9.1, "end":11}, {"day":2, "start":13.1, "end":15}]},
        {"classNumber":12346, "session":[ {"day":3, "start":8.1, "end":10}, {"day":4, "start":12.1, "end":14}]}
        ],
    "comp1003Tut":[
            {"classNumber":12347, "session":[ {"day":5, "start":9.1, "end":11}, {"day":2, "start":13.1, "end":15}]},
            {"classNumber":12348, "session":[ {"day":3, "start":8.1, "end":10}, {"day":4, "start":12.1, "end":14}]}
        ]
}
'''
print(courseoption["comp1002Tut"][0]["session"][0]["start"])

for classNumber in courseoption["comp1002Tut"]:
    for session in classNumber["session"]:
        print(session["start"])
'''


classesStart=list(range(8,17))
for i in range(len(classesStart)):
    classesStart[i] +=0.1
print(classesStart)