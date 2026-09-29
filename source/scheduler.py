'''
{"day":5, "start":9.1, "end":11}
'''

def check_session_class(session1,session2):
    if session1["day"] == session2["day"]:
        if max(session1["start"], session2["start"]) < min(session1["end"], session2["end"]):
            return True
    return False


session1= {"day":5, "start":9.1, "end":11}
session2= {"day":5, "start":10.1, "end":12}

def is_valid_schedule(schedule):
    listOfSession = list()
    for i in schedule:
        for session in i["session"]:
            listOfSession.append(session)
    for i in range(len(listOfSession)):
            for j in range(i + 1, len(listOfSession)):
                session1 = listOfSession[i]
                session2 = listOfSession[j]

                if check_session_class(session1, session2):
                    return False
    return True

schedule = ({'classNumber': 50468, 'session': [{'day': 2, 'start': 12.1, 'end': 14.0}]}, {'classNumber': 50641, 'session': [{'day': 2, 'start': 10.1, 'end': 12.0}]}, {'classNumber': 50617, 'session': [{'day': 1, 'start': 8.1, 'end': 10.0}, {'day': 3, 'start': 12.1, 'end': 14.0}]}, {'classNumber': 50165, 'session': [{'day': 5, 'start': 10.1, 'end': 12.0}]}, {'classNumber': 50150, 'session': [{'day': 5, 'start': 16.1, 'end': 18.0}, {'day': 2, 'start': 16.1, 'end': 18.0}]}, {'classNumber': 50459, 'session': [{'day': 5, 'start': 12.1, 'end': 14.0}]}, {'classNumber': 50061, 'session': [{'day': 4, 'start': 13.1, 'end': 15.0}, {'day': 1, 'start': 11.1, 'end': 13.0}]}, {'classNumber': 50079, 'session': [{'day': 4, 'start': 11.1, 'end': 13.0}]})


print(is_valid_schedule(schedule))