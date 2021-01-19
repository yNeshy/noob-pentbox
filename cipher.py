from Crypto.Cipher import DES
from Crypto.Cipher import AES
import hashlib
import base64
from Crypto import Random



class DES_e():
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, message):
        
        des = DES.new(self.key, DES.MODE_OFB)
        plaintext = bytes(message)
        encoded = des.IV + des.encrypt(plaintext)

        return encoded

    def decrypt(self, message):
        pass

class AES_e():
    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, message):
        raw = self._pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, message):
        enc = base64.b64decode(message)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

# class Process():
#     choices = {}
    
#     def Vigenère(self):
#         pass
    
#     def DES(self):
#         pass
    
#     def AES(self):
#         pass

#     def main(self):
#         self.getChoice()
#         self.getMessage()
#         self.process()

#     def process(self):
#         if(self.choice=="1"):
#             self.Vigenère()
#         elif(self.choice=="2"):
#             self.DES()
#         elif(self.choice=="3"):
#             self.AES()

#     def getMessage(self):
#         print("enter the message : \n")
#         self.message=input()

#     def getChoice(self):
#         print("choose an encryption methode: \n")
#         for choice in list(self.choices.keys()):
#             line="\t"+choice+")"+self.choices[choice]+"\n"
#             print(line)
#         while(True):
#             self.choice=input()
#             if( (self.choice in list(self.choices.keys())) ):
#                 break
#             else:
#                 print("not a valid choice try again")

# #call to decrypt  
# #decoder = Decoder() 
# #decoder.main()     
# class Decoder(Process):
#     def __init__(self):
#         self.choices={
#             "1" : "Vigenère",
#             "2" : "DES",
#             "3" : "AES"   
#         }
#         self.choice="3"
#     def Vigenère(self):
#         while(True):
#             try:
#                 print("enter the key (must be a number): \n ")
#                 key = input()
#                 val = int(key)
#                 break
#             except ValueError:
#                 print("key must be a number")
#         encrypted_text=""
#         mult=(int)(len(self.message)/len(key))
#         newKey=key * (mult+1)
#         for i in range(0,len(self.message)):
#             encrypted_text=encrypted_text+chr( ord(self.message[i]) - int(newKey[i])  )
#         print(encrypted_text)
#         return encrypted_text

#     def DES(self):
#         while(True):
#             print("enter the key (key must be of length 8): \n ")
#             key=input()
#             if(len(key)==8):
#                 break
#             else:
#                 print("key must be of length 8 try again")
        
#         self.message = bytes(self.message)
#         n = len(self.message) % 8
#         message=self.message + (' ' * (8-n))
#         des = DES.new(bytes(key), DES.MODE_ECB)
#         encrypted_text = des.decrypt(bytes(message))
#         print(encrypted_text)
#         return encrypted_text
        
#     def AES(self):
#         while(True):
#             print("enter the key (key must be of length 16, 24, or 32 ): \n ")
#             key=input()
#             if((len(key)==32) or (len(key)==16) or (len(key)==24) ):
#                 break
#             else:
#                 print("key must be of length 16, 24, or 32 try again")
#         n = len(self.message) % len(key)
#         message=self.message + (' ' * (len(key)-n))
#         aes = AES.new(key, DES.MODE_ECB)
#         encrypted_text = aes.decrypt(bytes(message))
#         print(encrypted_text)
#         return encrypted_text




# #call to encrypt  
# #coder = Coder() 
# #coder.main()   
# class Coder(Process):
#     def __init__(self):
#         self.choices={
#             "1" : "Vigenère",
#             "2" : "DES",
#             "3" : "AES"   
#         }
#         self.choice="3"
#     def Vigenère(self):
#         while(True):
#             try:
#                 print("enter the key (must be a number): \n ")
#                 key = input()
#                 val = int(key)
#                 break
#             except ValueError:
#                 print("key must be a number")
#         encrypted_text=""
#         mult=(int)(len(self.message)/len(key))
#         newKey=key * (mult+1)
#         for i in range(0,len(self.message)):
#             encrypted_text=encrypted_text+chr( ord(self.message[i]) + int(newKey[i])  )
#         print(encrypted_text)
#         return encrypted_text

#     def DES(self):
#         while(True):
#             print("enter the key (key must be of length 8): \n ")
#             key=input()
#             if(len(key)==8):
#                 break
#             else:
#                 print("key must be of length 8 try again")
#         n = len(self.message) % 8
#         message=self.message + (' ' * (8-n))
#         des = DES.new(key, DES.MODE_ECB)
#         encrypted_text = des.encrypt(message)
#         print(type(encrypted_text))
#         print(encrypted_text)
#         return encrypted_text
        
#     def AES(self):
#         while(True):
#             print("enter the key (key must be of length 16, 24, or 32 ): \n ")
#             key=input()
#             if((len(key)==32) or (len(key)==16) or (len(key)==24) ):
#                 break
#             else:
#                 print("key must be of length 16, 24, or 32 try again")
#         n = len(self.message) % 8
#         message=self.message + (' ' * (8-n))
#         aes = AES.new(key, DES.MODE_ECB)
#         encrypted_text = aes.encrypt(message)
#         print(encrypted_text)
#         return encrypted_text
        
if __name__ == "__main__":
    aes = AES_e("12345678123467812345678123468")
    x = aes.encrypt("aziz")
    print(x)

    aes = AES_e("12345678123467812345678123468")
    y = aes.decrypt(x)
    print(y)
     

