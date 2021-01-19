# Python program to illustrate ElGamal encryption 
import random 
from math import pow
import os

SOURCE_FOLDER = "./al_gamal_keys/"

class PrivateKey():
    def __init__(self, key):
        self.key = int(key)


class PublicKey():
    def __init__(self, h, q, g):
        self.h = int(h)
        self.q = int(q)
        self.g = int(g)
    


def gcd(a, b): 
	if a < b: 
		return gcd(b, a) 
	elif a % b == 0: 
		return b
	else: 
		return gcd(b, a % b) 

# Generating large random numbers 
def gen_key(q): 
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1: 
        key = random.randint(pow(10, 20), q)

    return key 

# Modular exponentiation 
def power(a, b, c): 
	x = 1
	y = a 
	while b > 0: 
		if b % 2 == 0: 
			x = (x * y) % c
		y = (y * y) % c 
		b = int(b / 2) 

	return x % c 

# Asymmetric encryption 
def alice_encrypt(msg, q, h, g): 
    en_msg = [] 
    k = gen_key(q)  # Private key for sender 
    s = power(h, k, q) 
    p = power(g, k, q) 
    
    # copy basically
    for i in range(0, len(msg)): 
        en_msg.append(msg[i]) 
  
    for i in range(0, len(en_msg)): 
        en_msg[i] = s * ord(en_msg[i])
  
    return en_msg, p
  
def decrypt(en_msg, p, key, q): 
    dr_msg = [] 
    h = power(p, key, q) 
    for i in range(0, len(en_msg)): 
        dr_msg.append(chr(int(en_msg[i]/h))) 
          
    return dr_msg 
  
def bob_decrypt(en_msg, p, key, q): 
  
    dr_msg = [] 
    h = power(p, key, q) 
    for i in range(0, len(en_msg)): 
        dr_msg.append(chr(int(en_msg[i]/h))) 
          
    return dr_msg 

class Algamal():
    """
    Asymetric encryption, using Algamal's algorithm.
    """
    def __init__(self, name=None):
        if(not name):
            q = random.randint(pow(10, 20), pow(10, 50))
            g = random.randint(2, q) 
            
            # Set private key
            key = gen_key(q)
            self.__private_key__ = PrivateKey(key)
            
            
            h = power(g, key, q)
            self.__public_key__ = PublicKey(h, q, g)
        else :
            self.load(name)

    def load(self, name):
        try:
            with open(SOURCE_FOLDER+name+".key", 'r') as f :
                data = f.readline()
                self.__public_key__ = PublicKey(data[0], data[1], data[2])
                self.__private_key__ = PrivateKey(data[3])

        except FileNotFoundError:
            return -1
        return 1

    def save(self, name):
        try:
            with open(SOURCE_FOLDER+name+".key", 'wb') as f :
                line = '{}:{}:{}:{}'.format(self.__public_key__.h, self.__public_key__.h, self.__public_key__.g, self.__private_key__.key)
                f.write(line.encode())
                f.close
            
        except FileNotFoundError :
            return -1
        return 1

    def encrypt(self, message, public_key):
        return alice_encrypt(message ,public_key.q, public_key.h, public_key.g)

    def decrypt(self, message, p):
        return bob_decrypt(message, p, self.__private_key__.key, self.__public_key__.q )

    def get_public_key(self):
        return self.__public_key__

    @staticmethod
    def get_saved_users():
        arr = [user.split('.')[0] for user in os.listdir(SOURCE_FOLDER) ]
        return arr

    @staticmethod
    def find_public_key(name):
        if (name not in Algamal.get_saved_users() ):
            print(name+" not found.")
            return None
        with open(SOURCE_FOLDER+name+".key", 'r') as f :
            data = f.readline().split(':')
            return PublicKey(data[0], data[1], data[2])

        


if __name__ == "__main__":
    alice = Algamal()
    bob = Algamal()
    

    bob.save("bob")

    bob = Algamal("bob")
    alice_msg = "Pour etre franc, je ne comprend vraiment rien. chui tombé de la coline et j'ai de la colle sur lse main et des disques sur les doights, de gros disques sur mes doights je ne peux pas arreter."
    encrypted_message, pk = bob.encrypt(alice_msg, alice.get_public_key())
    decr = ''.join(alice.decrypt(encrypted_message, pk))
    
    print(decr)

