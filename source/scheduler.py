
def check_session_class(session1,session2):
    if session1["day"] == session2["day"]:
        if max(session1["start"], session2["start"]) < min(session1["end"], session2["end"]):
            return True
    return False

def is_valid_schedule(schedule):
    listOfSession = list()
    for i in schedule:
        for session in i["session"]:
            listOfSession.append(session)
            #put the all sessions into 1 list
    for i in range(len(listOfSession)):
            for j in range(i + 1, len(listOfSession)):
                session1 = listOfSession[i]
                session2 = listOfSession[j]

                if check_session_class(session1, session2):
                    return False
            #pick every combination of 2 and validate them
    return True

