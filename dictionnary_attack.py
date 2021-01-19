import hashlib
import json
import glob



## look I'm sorry, don't cringe. I didn't want a whole file for this, it's an academic project ok!
def hash_message(message, alg):
    """
    Will hash message with alg (algorithm)
    """
    if not (alg in hashlib.algorithms_available) :
        print("{} is not supported.".format(alg))
        return 
    
    hasher = hashlib.new(alg)
    hashed = ""
    try:
        hasher.update((bytes(message, encoding='utf-8')))
        hashed = hasher.hexdigest()
    except TypeError :
        hasher.update((bytes(message, encoding='utf-8')))
        hashed = hasher.hexdigest(0)
    
    return hashed

class dictionnary_attack():

    def __init__(self, hashing_algorithm):
        self.PATH = "./dictionnaries/serialized_dictionnaries"
        if (hashing_algorithm == None):
            self.issetup = False
            return

        try:
            self.hash = hashlib.new(str(hashing_algorithm))
            try:
                file_path = self.PATH+"/{}.json".format(hashing_algorithm)
            except:
                print("dictionnaries not found.")
            self.hash_dict = json.loads(open(file_path, 'r').read())

            self.issetup = True
        except ValueError :
            print(hashing_algorithm+""" is not a supported hashing algorithm. See supported hashing algorithm
                through the info function, or refere to help.""")
        except FileNotFoundError:
            print("hashing algorithm not yet saved.")
    
    def unhash(self, hashed):
        if not self.issetup :
            print("No hashing algorithm selected.")
            return ""

        try: 
            result = self.hash_dict[hashed]
        except KeyError:
            result = None

        if (result):
            print("FOUND:  {}".format(result))

        else:
            print("{} not found. It is pretty secure.".format(hashed))
            
        
        return result

    def supported_algorithms(self):
        available_dictionnaries = glob.glob(self.PATH+"/*")
        return [ algo_name.split('/')[3].split('.')[0] for algo_name in available_dictionnaries ]


    def info(self):
        print("Available algorithms: {}".format(hashlib.algorithms_available) )
