import hashlib
import json


def write_md5():
    passwords = open("dictionnaries/samples/common1.txt",'r')
    md5 = open("dictionnaries/serialized_dictionnaries/md5.json", 'w')
    md5_dict = {}
    for line in passwords :
        password = line.replace("\n","")
        hashed = hashlib.md5(bytes(password, 'utf-8'))
        md5_dict[hashed.hexdigest()] = password

    md5.write(json.dumps(md5_dict) )

    passwords.close()
    md5.close()

def read():
    md5 = open("dictionnaries/serialized_dictionnaries/md5.json", 'r')
    md5_dict = json.loads(md5.read())
    md5.close()
    return md5_dict



def write(alg):
    if not (alg in hashlib.algorithms_available) :
        print("{} does is not supported.".format(alg))
        return 
    passwords = open("dictionnaries/samples/common1.txt",'r')
    file_name = "dictionnaries/serialized_dictionnaries/{}.json".format(alg)
    f = open(file_name, 'w')
    
    hasher = None
    algorithm_dict = {}
    for line in passwords :
        password = line.replace("\n","")
        hasher = hashlib.new(alg)
        hashed = ""
        try:
            hasher.update((bytes(password, encoding='utf-8')))
            hashed = hasher.hexdigest()
        except TypeError :
            hasher.update((bytes(password, encoding='utf-8')))
            hashed = hasher.hexdigest(0)
        del hasher

        algorithm_dict[hashed] = password

    f.write(json.dumps(algorithm_dict))
    passwords.close()



for alg in hashlib.algorithms_available :
    write(alg)