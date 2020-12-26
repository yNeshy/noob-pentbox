from cli import CLIMenus
from dictionnary_attack import dictionnary_attack

menus = CLIMenus()

def codage():
    print("codage")

def decodage():
    print("decodage")

def hachage():
    print("hachage")

def craquage():
    print("")
    #dictionnary_attack()

def chiffrement_symetrique():
    print("chiffrement symetrique")

def dechiffrement_symetrique():
    print("dechiffrement symetrique")


def chiffrement_Asymetrique():
    print("chiffrement asymetrique")

def dechiffrement_Asymetrique():
    print("dechiffrement asymetrique")




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
                chiffrement_symetrique
            elif(x=='b'):
                dechiffrement_symetrique
            else:
                print("Wrong input...")
                wrong = True
        elif(_input=='5'):
            x = menus.chiffrement_Asymetrique_menu()
            if(x=='a'):
                chiffrement_Asymetrique
            elif(x=='b'):
                dechiffrement_Asymetrique
            else:
                print("Wrong input...")
                wrong = True
        elif(_input=='6'):
            print("Quitting...")
        
        else:
            print("Wrong input...")
            wrong = True

    print("-----------Aziz Nechi & Ghaith Nabli-----------")
        

if __name__ == "__main__":
    main()