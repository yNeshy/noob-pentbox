import hashlib
import json

class dictionnary_attack():
    def __init__(self, hashing_algorithm):
        try:
            self.hash = hashlib.new(hashing_algorithm)
            try:
                file_path = "dictionnaries/serialized_dictionnaries/{}.json".format(hashing_algorithm)
            except:
                print("dictionnaries not found.")
            self.hash_dict = json.loads(open(file_path, 'r').read())

            self.__issetup__ = True
        except ValueError :
            print(hashing_algorithm+"""is not a supported hashing algorithm. See supported hashing algorithm
                through the info function, or refere to help.""")
        except FileNotFoundError:
            print("hashing algorithm not yet saved.")
    
    def unhash(self, hashed):
        if not self.__issetup__ :
            print("Select hashing algorithm first.")
            return ""

        try: 
            result = self.hash_dict[hashed]
        except KeyError:
            print(str(hashed)+ " is not supported.")
            result = ""

        if (result == ""):
            print("{} not found. It is pretty secure.")
        
        else:
            print("{} = {}".format(hashed, result))
        
        return result

