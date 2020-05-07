# Some sample test functions for the Feistel program

def test_func1(input: int, key:float) -> int:
    return hash(key*input + ((10**key) % 1000000 + key + 1))
