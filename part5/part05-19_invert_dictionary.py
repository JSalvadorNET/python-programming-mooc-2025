def invert(dictionary: dict):
    for key in list(dictionary.keys()):
        dictionary[dictionary[key]] = key  
        del dictionary[key]  
        
if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
 