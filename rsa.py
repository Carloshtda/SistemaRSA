import secrets
import math_functions

class Rsa:
    def __init__(self):
        self.__q = 0 #chave privada
        self.__p = 0 #chave privada
        self.__n = 0 #chave pública
        self.__e = 3 #chave pública
        self.__d = 0 #chave privada
        self.__minPrime = 0
        self.__maxPrime = 1000

    def file_setup(self, file_control):
        self.__p = int(file_control.keys[0])
        self.__q = int(file_control.keys[1])
        self.__d = int(file_control.keys[2])
        self.__e = int(file_control.keys[3])
        self.__n = int(file_control.keys[4])
        public_keys = (self.__e, self.__n)
        return public_keys

    def setup(self):
        primes = [i for i in range(self.__minPrime, self.__maxPrime) if math_functions.is_prime(i)]

        self.__p = secrets.choice(primes)
        while (self.__p - 5)%6 != 0:
            self.__p = secrets.choice(primes)

        self.__q = secrets.choice(primes)
        while (self.__q - 5) % 6 != 0 or (self.__p ==  self.__q):
            self.__q = secrets.choice(primes)

        self.__n = self.__p * self.__q
        totiente = (self.__p - 1) * (self.__q - 1)

        self.__d = math_functions.mulinv(self.__e, totiente)
        public_keys = (self.__e, self.__n)
        return public_keys

    def encrypt(self, msg):
        encoded_msg = []
        for i in range(len(msg)):
            encoded_msg.append(ord(msg[i])**self.__e % self.__n)
        return ' '.join(map(str, encoded_msg))

    def decrypt(self, encrypted_msg):
        encrypted_list = encrypted_msg.split()
        decryted_list = []
        for i in range(len(encrypted_list)):
            decryted_list.append(chr((int(encrypted_list[i])**self.__d) % self.__n))
        return ''.join(map(str, decryted_list))

    def get_public_n(self):
        return self.__n

    def keys_toString(self):
        keys = [self.__p, self.__q, self.__d, self.__e, self.__n]
        return ' '.join(map(str, keys))