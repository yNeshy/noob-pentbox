import os

class CLIMenus:
    def __init__(self):
        self.previous = None
        self.menu = "{}\n\n{}\n\n"
    def __clear__(self):
        # for mac and linux
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            # for windows
            _ = os.system('cls')
        

    def __print__(self, items, clear=True, title=""):
        if(clear):
            self.__clear__()
        menu_items = """"""
        for key in items:
            menu_items = menu_items+"\t"+str(key)+"-  "+str(items[key])+"\n"
        print(self.menu.format(title,menu_items))


    def main_menu(self):
        title = "OUTIL DE CRYPTOGRAPHIE by AZIZ NECHI"
        items = {
            1: "Codage et Décodage d'un message: ",
            2: "Hachage d'un message:",
            3: "Craquage d'un message haché:",
            4: "Chiffrement et déchiffrement Symétrique",
            5: "Chiffrement et déchiffrement Asymétrique",
            6: "Quitter"
        }
        self.__print__(items, title=title)

    def codage_decodage_menu(self):
        title = "Chiffrement Symétrique"
        items = {
            'a': "Codage: ",
            'b': "Décodage:",   
        }
        self.__print__(items, title=title)

    def chiffrement_Symetrique_menu(self):
        title = "Chiffrement Symétrique"
        items = {
            1: "Chiffrer: ",
            2: "Déchiffrer:",   
        }
        self.__print__(items, title=title)

    def chiffrement_Asymetrique_menu(self):
        title = "Chiffrement Asymétrique"
        items = {
            1: "Chiffrer: ",
            2: "Déchiffrer:",
        }
        self.__print__(items, title=title)


class CLInput:
    def __init__(self):
        pass

    def input(self, message="", options=None, formatting_dict=None):
        bad = True
        while(bad):
            if(options):
                print("Options are: "+str(options))
            input_x = input(message)
            if(options):
                if(input_x in options):
                    bad = False
                else :
                    print("Wrong input.")
        
        if(formatting_dict):
            try:
                return formatting_dict[input_x]
            except :
                print("Chosen option unavailable in provided dictionnary.\n{} not in {}").format(
                    input_x, formatting_dict
                )
                return None 