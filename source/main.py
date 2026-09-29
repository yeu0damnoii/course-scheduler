import json
import itertools
import scheduler as s

with open('data/course.json', 'r') as f:
    course_data = json.load(f)

danh_sach_8_mon = list(course_data.values())

# * (Unpacking Operator) pass 8 small list to make 8 tham số cho itertools.product
goc_to_hop = itertools.product(*danh_sach_8_mon) #list of every possible combination of all posisble schedule

# iterate each schedule
for schedule in goc_to_hop:
    if s.is_valid_schedule(schedule):
        print(schedule)
        print()
