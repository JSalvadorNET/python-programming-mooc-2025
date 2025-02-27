def search_students(students_file):
    students = {}
    try:
        with open(students_file) as new_file:  
            for line in new_file:
                parts = line.strip().split(";")
                if parts[0] == "id": 
                    continue
                student_id = parts[0]
                first_name = parts[1] 
                last_name = parts[2]  
                students[student_id] = (first_name, last_name) 
    except FileNotFoundError:
        print(f"Erro: '{students_file}' not found")
    return students

def search_exercises(exercises_file):
    exercises = {}
    try:
        with open(exercises_file) as new_file:  
            for line in new_file:
                parts = line.strip().split(";")
                if parts[0] == "id":  
                    continue
                student_id = parts[0]
                total_exercises = 0
                for num in parts[1:]:  
                    total_exercises += int(num)
                exercises[student_id] = total_exercises  
    except FileNotFoundError:
        print(f"Erro: '{exercises_file}' not found")
    return exercises

def search_exam_points(exam_file):
    exams = {}
    try:
        with open(exam_file) as new_file:
            for line in new_file:
                parts = line.strip().split(";")
                if parts[0] == "id":  
                    continue
                student_id = parts[0]  
                exam_points = 0  
                for num in parts[1:]:
                    exam_points += int(num)  
                exams[student_id] = exam_points  
    except FileNotFoundError:
        print(f"Error: '{exam_file}' not found")
    return exams

def calculate_exercise_points(total_exercises):
    max_exercises = 40
    percentage = (total_exercises / max_exercises) * 100
    exercise_points = min(int(percentage // 10), 10)
    return exercise_points

def calculate_grade(exam_points, exercise_points):
    total_points = exam_points + exercise_points
    if total_points <= 14:
        return 0
    elif total_points <= 17:
        return 1
    elif total_points <= 20:
        return 2
    elif total_points <= 23:
        return 3
    elif total_points <= 27:
        return 4
    else:
        return 5

students_file = input("Student information: ")
exercises_file = input("Exercises completed: ")
exam_file = input("Exam points: ")

students = search_students(students_file)
exercises = search_exercises(exercises_file)
exam_points = search_exam_points(exam_file)

for student_id in students:
    first_name, last_name = students[student_id]
    total_exercises = exercises.get(student_id, 0)
    exercise_points = calculate_exercise_points(total_exercises)
    total_exam_points = exam_points.get(student_id, 0)
    grade = calculate_grade(total_exam_points, exercise_points)
    
    print(f"{first_name} {last_name} {grade}")
