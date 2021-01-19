from Crypto.Cipher import DES
from Crypto.Cipher import AES
import hashlib

from Cli import CLInputs
inputs = CLInputs()

class Process():
    choices = {}
    
    def Vigenère(self):
        pass
    
    def DES(self):
        pass
    
    def AES(self):
        pass

    def main(self):
        self.getChoice()
        self.getMessage()
        self.process()

    def process(self):
        if(self.choice=="1"):
            self.Vigenère()
        elif(self.choice=="2"):
            self.DES()
        elif(self.choice=="3"):
            self.AES()

    def getMessage(self):
        print("enter the message : \n")
        self.message=input()

    def getChoice(self):
        print("choose an encryption methode: \n")
        for choice in list(self.choices.keys()):
            line="\t"+choice+")"+self.choices[choice]+"\n"
            print(line)
        while(True):
            self.choice=input()
            if( (self.choice in list(self.choices.keys())) ):
                break
            else:
                print("not a valid choice try again")

#call to decrypt  
#decoder = Decoder() 
#decoder.main()     
class Decoder(Process):
    def __init__(self):
        self.choices={
            "1" : "Vigenère",
            "2" : "DES",
            "3" : "AES"   
        }
        self.choice="3"
    def Vigenère(self):
        while(True):
            try:
                print("enter the key (must be a number): \n ")
                key = input()
                val = int(key)
                break
            except ValueError:
                print("key must be a number")
        encrypted_text=""
        mult=(int)(len(self.message)/len(key))
        newKey=key * (mult+1)
        for i in range(0,len(self.message)):
            encrypted_text=encrypted_text+chr( ord(self.message[i]) - int(newKey[i])  )
        print(encrypted_text)
        return encrypted_text

    def DES(self):
        while(True):
            print("enter the key (key must be of length 8): \n ")
            key=input()
            if(len(key)==8):
                break
            else:
                print("key must be of length 8 try again")
        
        self.message = bytes(self.message)
        n = len(self.message) % 8
        message=self.message + (' ' * (8-n))
        des = DES.new(bytes(key), DES.MODE_ECB)
        encrypted_text = des.decrypt(bytes(message))
        print(encrypted_text)
        return encrypted_text
        
    def AES(self):
        while(True):
            print("enter the key (key must be of length 16, 24, or 32 ): \n ")
            key=input()
            if((len(key)==32) or (len(key)==16) or (len(key)==24) ):
                break
            else:
                print("key must be of length 16, 24, or 32 try again")
        n = len(self.message) % len(key)
        message=self.message + (' ' * (len(key)-n))
        aes = AES.new(key, DES.MODE_ECB)
        encrypted_text = aes.decrypt(bytes(message))
        print(encrypted_text)
        return encrypted_text




#call to encrypt  
#coder = Coder() 
#coder.main()   
class Coder(Process):
    def __init__(self):
        self.choices={
            "1" : "Vigenère",
            "2" : "DES",
            "3" : "AES"   
        }
        self.choice="3"
    def Vigenère(self):
        while(True):
            try:
                print("enter the key (must be a number): \n ")
                key = input()
                val = int(key)
                break
            except ValueError:
                print("key must be a number")
        encrypted_text=""
        mult=(int)(len(self.message)/len(key))
        newKey=key * (mult+1)
        for i in range(0,len(self.message)):
            encrypted_text=encrypted_text+chr( ord(self.message[i]) + int(newKey[i])  )
        print(encrypted_text)
        return encrypted_text

    def DES(self):
        while(True):
            print("enter the key (key must be of length 8): \n ")
            key=input()
            if(len(key)==8):
                break
            else:
                print("key must be of length 8 try again")
        n = len(self.message) % 8
        message=self.message + (' ' * (8-n))
        des = DES.new(key, DES.MODE_ECB)
        encrypted_text = des.encrypt(message)
        print(type(encrypted_text))
        print(encrypted_text)
        return encrypted_text
        
    def AES(self):
        while(True):
            print("enter the key (key must be of length 16, 24, or 32 ): \n ")
            key=input()
            if((len(key)==32) or (len(key)==16) or (len(key)==24) ):
                break
            else:
                print("key must be of length 16, 24, or 32 try again")
        n = len(self.message) % 8
        message=self.message + (' ' * (8-n))
        aes = AES.new(key, DES.MODE_ECB)
        encrypted_text = aes.encrypt(message)
        print(encrypted_text)
        return encrypted_text
        
        


class Hash(Process):


    def __init__(self, alg):
        self.alg = alg

    def getChoice(self):
        pass

    def process(self):
        hashed = Hash.write(self.alg, self.message)
        print(hashed)
        return hashed

    def getMessage(self):
        print("enter the message to be hashed : \n")
        self.message=input()


    @staticmethod
    def write(alg, message):
        if not (alg in hashlib.algorithms_available) :
            print("{} does is not supported.".format(alg))
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
        
    

Decoder().main()

