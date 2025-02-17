def add_student(students, name):
    """Adds a new student to the dictionary with an empty 'courses' dictionary."""
    students[name] = {"courses": {}} 
 
def add_course(students, name, course):
    """Adds a course and its grade to the student's record, ensuring:
       - The student exists in the database.
       - Courses with grade 0 are ignored.
       - If a course is repeated, only higher grades replace existing ones.
    """
    if name not in students:
        print(f"{name}: no such person in the database")
        return
 
    course_name, grade = course
 
    if grade == 0:
        return  # Ignore courses with grade 0
 
    # If the course exists, update the grade only if the new grade is higher
    if course_name in students[name]["courses"]:
        if grade > students[name]["courses"][course_name]:
            students[name]["courses"][course_name] = grade
    else:
        students[name]["courses"][course_name] = grade  # Add new course
 
def print_student(students, name):
    """Prints the student's information, including completed courses and average grade."""
    if name not in students:
        print(f"{name}: no such person in the database")
        return
 
    courses = students[name]["courses"]
    num_courses = len(courses)
 
    if num_courses == 0:
        print(f"{name}:\n no completed courses")
        return
 
    print(f"{name}:")
    print(f" {num_courses} completed courses:")
 
    total_grade = sum(courses.values())
 
    # Print each course and its grade
    for course_name, grade in courses.items():
        print(f"  {course_name} {grade}")
 
    average_grade = total_grade / num_courses  # Calculate average grade
    print(f" average grade {average_grade:.1f}")
 
def summary(students):    
    """Prints a summary of all students, including:
       - Total number of students
       - The student with the most completed courses
       - The student with the highest average grade
    """
    num_students = len(students)
    if num_students == 0:
        print("No students in the database.")
        return
 
    max_courses = 0
    top_student_courses = None
    best_avg_grade = 0
    top_student_avg = None
 
    # Loop through all students to calculate required statistics
    for name, data in students.items():
        num_courses = len(data["courses"])
        total_grade = sum(data["courses"].values())
        avg_grade = total_grade / num_courses if num_courses > 0 else 0
 
        # Check for most completed courses
        if num_courses > max_courses:
            max_courses = num_courses
            top_student_courses = name
 
        # Check for best average grade
        if avg_grade > best_avg_grade:
            best_avg_grade = avg_grade
            top_student_avg = name
 
    # Print the summary results
    print(f"students {num_students}")
    print(f"most courses completed {max_courses} {top_student_courses}")
    print(f"best average grade {best_avg_grade:.1f} {top_student_avg}")
 
# Main execution block (only runs when the script is executed directly)
if __name__ == "__main__":
    students = {}
 
    # Adding students
    add_student(students, "Peter")
    add_student(students, "Eliza")
 
    # Printing students before adding courses
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")  # Student not in database
    print()
 
    # Adding courses
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Introduction to Programming", 0))  # Should be ignored
    add_course(students, "Peter", ("Advanced Course in Programming", 4))  # Updates grade 2 → 4
    add_course(students, "Peter", ("Introduction to Programming", 2))  # Should be ignored (3 > 2)
 
    # Printing student information after adding courses
    print_student(students, "Peter")
    print()
 
    # Adding more courses and generating summary
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
 