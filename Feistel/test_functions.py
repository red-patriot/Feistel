""" Some sample functions for the Feistel program. """

import hashlib

def test_func1(input:int, key:float) -> int:
    """ A test function to use in a Feistel network. """
    return input + key

def test_func2(input:int, key:float) -> int:
    """ A test function to use in a Feistel network. """
    return hash(key*input + ((10**key) % 1000000 + key + 1))

def test_func3(input:int, key:float) -> int:
    """ A test function to use in a Feistel network. """
    sha2 = hashlib.sha256()
    sha2.update(str(input + key).encode())
    return int(sha2.hexdigest(), 16)
