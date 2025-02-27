def filter_solutions():
    correct = []
    incorrect = []
    with open("solutions.csv") as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            name = parts[0]
            problem = parts[1]
            expected_result = int(parts[2])
            
            if "+" in problem:
                operands = problem.split("+")
                actual_result = int(operands[0]) + int(operands[1])
            elif "-" in problem:
                operands = problem.split("-")
                actual_result = int(operands[0]) - int(operands[1])
            else:
                continue
            
            if actual_result == expected_result:
                correct.append(line)
            else:
                incorrect.append(line)            
            
        with open("correct.csv", "w") as correct_file:
            for entry in correct:
                correct_file.write(entry + "\n")

        with open("incorrect.csv", "w") as incorrect_file:
            for entry in incorrect:
                incorrect_file.write(entry + "\n")

if __name__ == "__main__":
    filter_solutions()
