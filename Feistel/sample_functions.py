""" Some sample functions for the Feistel program. """

import hashlib

def _test_func1(input:int, key:float) -> int:
    """ A test function to use in a Feistel network. """
    return input + key

def _test_func2(input:int, key:float) -> int:
    """ A test function to use in a Feistel network. """
    return hash(key*input + ((10**key) % 1000000 + key + 1))

# Sample hash functions for use.

def sha256(input:int, key:float) -> int:
    """ An implementation of SHA256 for use in a Feistel network. """
    sha = hashlib.sha256()
    sha.update(str(input + key).encode())
    return int(sha2.hexdigest(), 16)

def sha384(input:int, key:float) -> int:
    sha = hashlib.sha384()
    sha.update(str(input + key).encode())
    return int(sha2.hexdigest(), 16)

def sha512(input:int, key:float) -> int:
    sha = hashlib.sha512()
    sha.update(str(input + key).encode())
    return int(sha2.hexdigest(), 16)

def sha224(input:int, key:float) -> int:
    sha = hashlib.sha224()
    sha.update(str(input + key).encode())
    return int(sha2.hexdigest(), 16)
