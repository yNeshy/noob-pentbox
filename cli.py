import os

class CLIMenus:
    def __init__(self):
        self.previous = None
        self.menu = "{}\n\n{}\n\n"
        self.inputClient = CLInputs()

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
        return self.inputClient.input(message="Choice", options=[str(i) for i in range(1,7)])

    # 1
    def codage_decodage_menu(self):
        title = "Codage - decodage"
        items = {
            'a': "Codage d'un message: ",
            'b': "Décodage d'un message codé:",   
        }
        self.__print__(items, title=title)
        return self.inputClient.input(message="Symetrique", options=['a', 'b'])

    # 2
    def hachage_message(self):
        return 0

    # 3
    def craquage_message_hache(self):
        return 0

    # 4
    def chiffrement_Symetrique_menu(self):
        title = "Chiffrement Symétrique"
        items = {
            'a': "Chiffrer: ",
            'b': "Déchiffrer:",   
        }
        self.__print__(items, title=title)
        return self.inputClient.input(message="Symetrique", options=['a', 'b'])

    # 5
    def chiffrement_Asymetrique_menu(self):
        title = "Chiffrement Asymétrique"
        items = {
            'a': "Chiffrer: ",
            'b': "Déchiffrer:",
        }
        self.__print__(items, title=title)
        return self.inputClient.input(message="Asymetrique", options=['a', 'b'])

    # 6 
    def quitter(self):
        return -1        


class CLInputs:
    def __init__(self):
        pass

    def input(self, message="", options=None, formatting_dict=None):
        bad = True
        while(bad):
            if(len(options) > 0):
                print("Options are: "+str(options))
            if( len(message) > 0):
                print(message, end=": ")
            input_x = input()
            if(options):
                if( str(input_x) in [str(_) for _ in options] ):
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
        else :
            return str(input_x)


if __name__ == "__main__":
    menu = CLIMenus()
    cli = CLInputs()

    menu.main_menu()
    x=cli.input(message="Choose:", options=[i for i in range(1,7)])
    print(x)
