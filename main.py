import canvasapi
import re
import datetime

# Wabash URl
API_URL = "https://wabash.instructure.com"
# Wabash API Key
API_KEY = "1~IWdzaYdi6jEXFdYuN46j9UdXYzYuJy0SdnIP0Fh6ZjtAFdqA3go3hOHFlxht6yEI"

# Relevant Canvas Vars
canvas = canvasapi.Canvas(API_URL, API_KEY)
user_id = 12552904
me = canvas.get_user(user_id)
courses = me.get_courses()

# Find list of all courses
for course in courses:
    course = str(course)
    course = re.sub("[,].+[SP|FA]", "", course)
    print(course)
    semester = re.findall("[.]\d{2}\S\w{2}", course)
    if semester:
        semester = semester[0]
        semester = semester[1:]
        print(semester)

