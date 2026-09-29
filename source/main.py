import json
import itertools
import scheduler as s

with open('data/course.json', 'r') as f:
    course_data = json.load(f)

danh_sach_8_mon = list(course_data.values())

# 3. Dùng dấu * (Unpacking Operator) để truyền 8 list nhỏ làm 8 tham số cho itertools.product
goc_to_hop = itertools.product(*danh_sach_8_mon)


# 4. Duyệt qua từng bộ lịch
for schedule in goc_to_hop:
    # Biến 'schedule' ở đây là một Tuple chứa đúng 8 option (mỗi option từ 1 môn)
    # Bạn sẽ gọi hàm is_valid_schedule(schedule) tự viết ở đây!
    if s.is_valid_schedule(schedule):
        print(schedule)
        print()
