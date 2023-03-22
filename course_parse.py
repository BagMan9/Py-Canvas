import re
import datetime

UniDict = {"wabash": 1}

year = datetime.date.today().year
current_month = datetime.date.today().month


def parse_course(course, uni):
    try:
        uni_code = UniDict[uni]
    except KeyError:
        try:
            open("CUSTOM", "x")
        except FileExistsError:
            uni_code = 0
            pass
        else:
            choice = input("University not in database. Would you like to use the nickname method? (y/n): ")
            if choice.lower() == "y":
                print("Go to your Canvas dashboard page and select 'Card View'.\n"
                      "Click the three dots in the upper right corner of the course you want to add.\n"
                      "Name your course whatever you want, but make sure it ends in '.FA' or '.SP' for Fall/Spring.\n "
                      "a '/' followed by the last two digits of the year.\n"
                      "Example: 'CS 101.19/FA' for Fall 2019.\n"
                      "Come back here when you are done.")
                input("Press enter to continue...")
                print("Great, now we will attempt to parse your courses.")
                uni_code = 0
                open("CUSTOM", "w")
                open("CUSTOM", "w").close()
            else:
                print("Sorry, we can't help you with that. Try again later.")
                exit(2)
    if uni_code == 0:
        course_nick = str(course.name)
        course = str(course)
        semester = re.findall("[.]\d{2}\S\w{2}", course_nick)
        course_number = re.findall("[(]\d{7}[)]", course)[0]
        course_number = course_number[1:-1]
        if semester:
            semester = semester[0]
            semester = semester[1:]
            if semester[-2:] == "SP" and current_month < 6:
                return course_nick, course_number
            elif semester[-2:] == "FA" and current_month > 6:
                return course_nick, course_number

    if uni_code == 1:
        nick = str(course.name)
        course = str(course)
        course = re.sub(",.+[SP|FA]", "", course)
        print(course)
        semester = re.findall("[.]\d{2}\S\w{2}", course)
        course_number = re.findall("[(]\d{7}[)]", course)[0]
        course_number = course_number[1:-1]
        print(course_number)
        if semester:
            semester = semester[0]
            semester = semester[1:]
            if semester[-2:] == "SP" and current_month < 6:
                return nick, course_number
            elif semester[-2:] == "FA" and current_month > 6:
                return nick, course_number
