# Dữ liệu điểm của lớp 2A
students_scores = [
    {'name': 'Được', 'math': 10, 'literature': 10, 'english':10},
    {'name': 'Yến', 'math': 1, 'literature': 1, 'english': 1},
    {'name': 'Nguyên', 'math': 9, 'literature': 8, 'english': 7},
    {'name': 'Bằng', 'math': 6, 'literature': 5, 'english': 6},
    {'name': 'Hiếu', 'math': 7, 'literature': 7, 'english': 8}
]

# Tính điểm trung bình của từng học sinh
for student in students_scores:
    scores = [score for subject, score in student.items() if subject != 'name']
    student['average'] = sum(scores) / len(scores)

# In bảng điểm và điểm trung bình của từng học sinh
print(f"{'Tên Học Sinh':<15}{'Toán':<8}{'Văn':<8}{'Anh':<8}{'Điểm Trung Bình'}")
print("-" * 50)
for student in students_scores:
    print(f"{student['name']:<15}{student['math']:<8}{student['literature']:<8}{student['english']:<8}{student['average']:.2f}")


# Tìm học sinh có điểm trung bình cao nhất và thấp nhất
highest_avg_student = max(students_scores, key=lambda x: x['average'])
lowest_avg_student = min(students_scores, key=lambda x: x['average'])

# In kết quả
print("\nKết quả:")
print(f"Học sinh có điểm trung bình cao nhất: {highest_avg_student['name']} với điểm trung bình {highest_avg_student['average']:.2f}")
print(f"Học sinh có điểm trung bình thấp nhất: {lowest_avg_student['name']} với điểm trung bình {lowest_avg_student['average']:.2f}")


