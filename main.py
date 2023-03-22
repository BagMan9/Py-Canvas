import canvasapi
import re
import datetime
try:
    import config
    # Canvas URl
    API_URL = config.api_url
    # Canvas API Key
    API_KEY = config.api_key
except ImportError:
    pass
    user_vars = open("config.py", "w")
    print("Config.py doesn't exist!")
    user_vars.write("api_url = 'https://" + input("Enter the first part of your Canvas URL\n"
                                                  "(I.E. if it is wabash.instructure.com, enter 'wabash': ")
                    + ".instructure.com'\n")
    user_vars.write("api_key = '" + input("Enter your API Key: ") + "'")
    user_vars.close()
    import config
    API_URL = config.api_url
    API_KEY = config.api_key
except AttributeError:
    print("Looks like your config.py file is missing some variables!\n"
          "Delete config and re-run the program to recreate it.")
    exit(1)


Current_Courses = {}
# General vars

# Canvas API object
canvas = canvasapi.Canvas(API_URL, API_KEY)

# User ID acquisition
me = canvas.get_current_user()

# Get list of courses
courses = me.get_courses()

# Get current year and month
year = datetime.date.today().year
current_month = datetime.date.today().month

# Find list of all courses
for course in courses:
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
            Current_Courses[nick] = course_number
        elif semester[-2:] == "FA" and current_month > 6:
            Current_Courses[nick] = course_number
print(Current_Courses)
