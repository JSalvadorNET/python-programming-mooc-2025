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

def combine_data(students_file, exercises_file):
    students = search_students(students_file)
    exercises = search_exercises(exercises_file)
    
    result = []
    for student_id in students:
        first_name, last_name = students[student_id]  
        if student_id in exercises:
            total_exercises = exercises[student_id]  
        else:
            total_exercises = 0  
        result.append(f"{first_name} {last_name} {total_exercises}")
    
    return result


student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
students_exercises = combine_data(student_file, exercise_file)
for item in students_exercises:
    print(item)