def store_personal_data(person: tuple):
    with open("people.csv", "a") as new_file: 
        new_file.write(f"{person[0]};{person[1]};{person[2]}\n")  

if __name__ == "__main__":
    a_person = ("Denis Django", 28, 1.83)
    store_personal_data(a_person)
