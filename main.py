from Cli import CLIMenus
from Cli import CLInputs
from dictionnary_attack import dictionnary_attack
from AlGamal import Algamal

import process

menus = CLIMenus()
inputs = CLInputs()

def save(line=""):
    with open('./tmp.txt', 'wb') as f:
        f.write(line.encode())
    f.close()

def load():
    content = []
    with open('./tmp.txt', 'r') as f:
        for line in f.readlines():
            content.append(line)
    return content


def codage():
    process.Coder().main()

def decodage():
    
    process.Decoder().main()

def hachage():
    for algo in dictionnary_attack(None).supported_algorithms(): # i pass none cause idk how to use static methods in python
        print("* "+algo)
    
    algo_choice = inputs.input(message="Select algorithm to use: ", options=None)
    process.Hash(algo_choice).main()

def craquage():
    print("Available algorithms: ")
    for algo in dictionnary_attack(None).supported_algorithms(): # i pass none cause idk how to use static methods in python
        print("* "+algo)
    
    algo_choice = inputs.input(message="Select algorithm to use: ", options=None)
    attacker = dictionnary_attack(algo_choice)
    
    if (attacker.issetup):
        hashed = inputs.input(message="Message to decrypt: ")
    print()
    result = attacker.unhash(hashed)
    
    return result


def chiffrement_symetrique():
    print("chiffrement symetrique")

def dechiffrement_symetrique():
    print("dechiffrement symetrique")


def chiffrement_Asymetrique():
    
    if(inputs.input(message="Charger personne? [y/n]", options=["y", "n"]) == 'y'):
        print("Choose user among: ")
        for user in Algamal.get_saved_users():
            print(user, end='\n')
        username = inputs.input(message="    ", options=Algamal.get_saved_users())
    else:
        username = None

    alice = Algamal(name=username)    
    message = inputs.input(message="Message à crypter: ")
    bob = inputs.input(message="Nom du destinataire: ")
    public_key = Algamal.find_public_key(bob)
    encrypted_message, message_key = alice.encrypt( message, public_key )
    output = ":".join([str(e) for e in encrypted_message])
    
    
    print("Message encrypté: " + output )
    print("Clé du message (p): " + str(message_key) )

    if(username==None):
        if(inputs.input("Voulez vous sauvegarder cet utilisateur? [y/n]", options=['y', 'n']) == 'y'):
            name=inputs.input(message="Nom du nouvel utilisateur: ")
            alice.save(name)
    save(line=output+"\n"+str(message_key))
    return (output, message_key)


def dechiffrement_Asymetrique():
    if(inputs.input(message="Charger personne? [y/n]", options=["y", "n"]) == 'y'):
        print("Options: ")
        for user in Algamal.get_saved_users():
            print(user, end='\n')
        username = inputs.input(message="   ", options=Algamal.get_saved_users())
    else:
        username = None

    bob = Algamal(name=username)
    message = None
    if(inputs.input(message="Decoder dernier message crypté? [y/n]: ", options=["y","n"]) == 'y'):
        saved = load()
        if(len(saved) < 2 ):
            print("Aucun message enregistré.")
            message = None
        else:
            message = [int(x) for x in saved[0].split(':')]
            key = int(saved[1])
            

    if(message==None):
        message = [int(x) for x in inputs.input(message="Message à décrypter: ").split(':')]
        key = int(inputs.input(message="Clé du message (p): "))

    message = bob.decrypt(message, key)
    print("Message clair: "+str(message))
    return message



def main():
    wrong = True
    while(wrong):
        _input = menus.main_menu()
        wrong = False

        if(_input=='1'):
            # codage decodage
            x = menus.codage_decodage_menu()
            if(x=='a'):
                codage()
            elif(x=='b'):
                decodage()
            else:
                print("Wrong input...")
                wrong = True
        elif(_input=='2'):
            hachage()
        elif(_input=='3'):
            craquage()

        elif(_input=='4'):
            x = menus.chiffrement_Symetrique_menu()
            if(x=='a'):
                chiffrement_symetrique()
            elif(x=='b'):
                dechiffrement_symetrique()
            else:
                print("Wrong input...")
                wrong = True
        elif(_input=='5'):
            x = menus.chiffrement_Asymetrique_menu()
            if(x=='a'):
                chiffrement_Asymetrique()
            elif(x=='b'):
                dechiffrement_Asymetrique()
            else:
                print("Wrong input...")
                wrong = True
        elif(_input=='6'):
            print("Quitting...")
            return False
        
        else:
            print("Wrong input...")
            wrong = True
        

    print("\n\n\t-----------Aziz Nechi & Ghaith Nabli-----------")
    return True
        

if __name__ == "__main__":    
    while(main()):
        input()
