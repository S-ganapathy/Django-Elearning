import requests

username='student3'
password='member@123'
base_url ='http://127.0.0.1:8000/api/'

# retrieve all courses

r=requests.get(f'{base_url}courses/')
courses=r.json()

avail_courses=','.join([course['title'] for course in courses])

print(avail_courses)


for course in courses:
    course_id=course['id']
    course_title=course['title']
    r=requests.post(f'{base_url}courses/{course_id}/enroll/',auth=(username,password))

    if r.status_code==200:
        print(f'Successfully enrolled in {course_title}')