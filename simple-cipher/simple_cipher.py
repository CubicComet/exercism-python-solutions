import math
import secrets
from string import ascii_lowercase


class Cipher(object):
    def __init__(self, key=None):
        if not key:
            key = Cipher._random_key()
        if not key.isalpha() or not key.islower():
            raise ValueError("Key must consist only of lowercase letters")
        self.key = key
        self._key = [ord(k)-97 for k in key]

    def encode(self, s):
        key = self._key * math.ceil(len(s)/len(self._key))
        chars = [c for c in s.lower() if c in ascii_lowercase]
        return "".join(Cipher._shift(c, k) for c, k in zip(chars, key))

    def decode(self, s):
        key = self._key * math.ceil(len(s)/len(self._key))
        chars = [c for c in s.lower() if c in ascii_lowercase]
        return "".join(Cipher._shift(c, -k) for c, k in zip(chars, key))

    @staticmethod
    def _shift(char, key):
        return chr(97 + ((ord(char) - 97 + key) % 26))

    @staticmethod
    def _random_key(length=256):
        return "".join(secrets.choice(ascii_lowercase) for _ in range(length))


class Caesar(Cipher):
    def __init__(self):
        Cipher.__init__(self, "d")
