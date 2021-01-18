from Crypto.Cipher import DES
from Crypto.Cipher import AES
import hashlib
class Process():
    choices = {}
    @abs
    def Vigenère(self):
        pass
    @abs
    def DES(self):
        pass
    @abs
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
        print("enter the messege to be encrypted : \n")
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
        print("enter the key : \n ")
        key = input()
        encrypted_text=""
        mult=(int)(len(self.message)/len(key))
        newKey=key * (mult+1)
        newKey=newKey.upper()
        for i in range(0,len(self.message)):
            encrypted_text=encrypted_text+chr( ord(self.message[i]) - ord(newKey[i]) -64 )
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
        encrypted_text = des.decrypt(message)
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
        encrypted_text = aes.decrypt(message)
        print(encrypted_text)
        return encrypted_text
        print()



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
        print("enter the key : \n ")
        key = input()
        encrypted_text=""
        mult=(int)(len(self.message)/len(key))
        newKey=key * (mult+1)
        newKey=newKey.upper()
        for i in range(0,len(self.message)):
            encrypted_text=encrypted_text+chr( ord(self.message[i]) + ord(newKey[i]) -64 )
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
        print()
        


class Hash(Process):
    def __init__(self):
        self.choices={
            "1" : "md5",
            "2" : "sha256",
            "3" : "sha512",
        }
        self.choice="3"
    def process(self):
        if(self.choice=="1"):
            hashed=hashlib.md5(str(self.message).encode('utf-8')).hexdigest()
        elif(self.choice=="2"):
            hashed=hashlib.sha256(str(self.message).encode('utf-8')).hexdigest()
        elif(self.choice=="3"):
            hashed=hashlib.sha512(str(self.message).encode('utf-8')).hexdigest()
        print(hashed)

    def getMessage(self):
        print("enter the messege to be hashed : \n")
        self.message=input()

if __name__ == '__main__':
    Hash().main()