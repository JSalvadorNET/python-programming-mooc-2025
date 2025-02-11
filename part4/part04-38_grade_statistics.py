'''
!! GOAL !!
 
The program collects exam points and completed exercises from students.
It calculates grades based on a grading system.
It prints statistics:
- Average points
- Pass percentage
- Grade distribution
 
!! FUNCTIONS !!
 
exam_and_exercise_completed(inpt)  ->	Splits input into exam points and exercise completed.
exercise_points(amount)	           ->   Converts completed exercises into exercise points (divided by 10).
grade(points)	                   ->   Returns grade (0-5) based on total points.
mean(points)	                   ->   Calculates the average of total points.
main()	                           ->   Manages the input, processing, storing, and printing statistics.
 
'''
 
 
def exam_and_exercise_completed(inpt): 
    exam, exercise = inpt.split()  # splits the input string by space
    return [int(exam), int(exercise)]  # converts both parts to integers
 
 
def exercise_points(amount):
    return amount // 10 # converts completed exercises into exercise points 
 
def grade(points):
    if points >= 28:
        return 5
    elif points >= 24:
        return 4
    elif points >= 21:
        return 3
    elif points >= 18:
        return 2
    elif points >= 15:
        return 1
    else:
        return 0
 
 
def mean(points):
    return sum(points) / len(points) # average of the total points.
 
def main():
    points = []
    grades = [0] * 6 # list to ount how many students got each grade (0 to 5)
    while True:
        inpt = input("Exam points and exercises completed: ")
        if len(inpt) == 0:
            break
 
        exam_and_exercises = exam_and_exercise_completed(inpt)
        exercise_pnts = exercise_points(exam_and_exercises[1])
        total_points = exam_and_exercises[0] + exercise_pnts
 
        points.append(total_points)
        grd = grade(total_points)
        if exam_and_exercises[0] < 10:
            grd = 0
        grades[grd] += 1
 
    pass_pros = 100 * (len(points) - grades[0]) / len(points)
 
    print("Statistics:")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {pass_pros:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars = "*" * grades[i]
        print(f"  {i}: {stars}")
 
main()