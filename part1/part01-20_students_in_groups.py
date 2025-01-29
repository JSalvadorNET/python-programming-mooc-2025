students_number = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))
groups = students_number // group_size
if students_number % group_size != 0:
    groups += 1
print(f"Number of groups formed: {groups}")
 