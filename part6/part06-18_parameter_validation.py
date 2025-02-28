def new_person(name: str, age: int):
    if name == "":
        raise ValueError("Name cannot be an empty string.")
    
    if len(name.split()) < 2:
        raise ValueError("Name must contain at least two words.")
    
    if len(name) > 40:
        raise ValueError("Name cannot be longer than 40 characters.")
    
    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150.")
    
    return (name, age)

if __name__ == "__main__":
    new_person("", 23) # empty string error
    new_person("Mary", 12) # at least two words error
    new_person("That's a new person, say hello to the new person!", 30) # longer than 40 char error
    new_person("Richard Ruby", 240) # age range error
    new_person("Peter Python", 32) # ideal entry
