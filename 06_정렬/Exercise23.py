N = int(input())
students = []
for i in range(N):
    name, korean, english, math = input().split()
    korean = int(korean)
    english = int(english)
    math = int(math)
    students.append((name, korean, english, math))
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for student in students:
    print(student[0])