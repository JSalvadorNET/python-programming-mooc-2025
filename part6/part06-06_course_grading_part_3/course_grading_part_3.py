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

def calculate_exercise_points(exercises_completed):
    total_exercises = 40 
    percentage = (exercises_completed / total_exercises) * 100

    if percentage >= 100:
        return 10
    elif percentage >= 90:
        return 9
    elif percentage >= 80:
        return 8
    elif percentage >= 70:
        return 7
    elif percentage >= 60:
        return 6
    elif percentage >= 50:
        return 5
    elif percentage >= 40:
        return 4
    elif percentage >= 30:
        return 3
    elif percentage >= 20:
        return 2
    elif percentage >= 10:
        return 1
    else:
        return 0

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

def print_student_statistics(students_file, exercises_file, exam_file):
    students = search_students(students_file)
    exercises = search_exercises(exercises_file)
    exams = search_exam_points(exam_file)

    # Print the header
    print(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}")

    for student_id, (first_name, last_name) in students.items():
        # Get the number of exercises completed
        completed_exercises = exercises.get(student_id, 0)
        
        # Calculate exercise points
        exercise_points = calculate_exercise_points(completed_exercises)
        
        # Get the exam points
        exam_points = exams.get(student_id, 0)
        
        # Calculate the total points
        total_points = exam_points + exercise_points
        
        # Calculate the grade
        grade = calculate_grade(exam_points, exercise_points)
        
        # Print the student info in formatted columns
        print(f"{first_name + ' ' + last_name:<30}{completed_exercises:<10}{exercise_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}")

students_file = input("Student information: ")
exercises_file = input("Exercises completed: ")
exam_file = input("Exam points: ")

print_student_statistics(students_file, exercises_file, exam_file)
