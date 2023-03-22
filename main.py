import canvasapi
import re
import course_parse as cpar
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


# Canvas API object
canvas = canvasapi.Canvas(API_URL, API_KEY)

# User ID acquisition
me = canvas.get_current_user()
print(me)

# Get list of courses
courses = me.get_courses()

# Get current year and month
year = datetime.date.today().year
current_month = datetime.date.today().month

# Dictionary of current courses
Current_Courses = {}

test = canvas.get_course(3664118)

# Find list of all courses
for course in courses:
    output = cpar.parse_course(course, "wabash")
    if output:
        Current_Courses[output[0]] = output[1]
print(Current_Courses)


