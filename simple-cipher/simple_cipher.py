import math
import secrets
from string import ascii_lowercase


class Cipher(object):
    def __init__(self, key=None):
        if not key:
            key = self._random_key()
        if not key.isalpha() or not key.islower():
            raise ValueError("Key must consist only of lowercase letters")
        self.key = key
        self._key = [ord(k)-97 for k in key]

    def encode(self, s, dirn=1):
        key = self._key * math.ceil(len(s)/len(self._key))
        chars = [c for c in s.lower() if c in ascii_lowercase]
        return "".join(self._shift(c, dirn*k) for c, k in zip(chars, key))

    def decode(self, s):
        return self.encode(s, dirn=-1)

    @staticmethod
    def _shift(char, key):
        return chr(97 + ((ord(char) - 97 + key) % 26))

    @staticmethod
    def _random_key(length=256):
        return "".join(secrets.choice(ascii_lowercase) for _ in range(length))


class Caesar(Cipher):
    def __init__(self):
        super().__init__("d")
