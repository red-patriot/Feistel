""" A file containing the implementation of a Feistel cipher"""


class Feistel():
    """ A balanced Feistel network.
    
    The network uses any cryptographic function to encrypt or decrypt a
    message using a balanced Feistel network. 

    Cryptographic functions:
        Any function which accepts as parameters an int and a float and 
        which returns an int can be used as the cryptographic function.
    """
    def __init__(self, func):
        """Initialize Feistel attributes"""
        self.cryptographic_function = func
        return 

    def encrypt(self, input: str, keys: list) -> str:
        """ Perform the encryption algorithm on the given message.

    message: A string to be encrypted
    keys: A list of keys used in the encryption, which are
        passed to the cryptographic function. The network will 
        perform 1 round of encryption for each key. 
        
    returns: the encrypted message. 
        """
        # Split the input into parts
        left, right = self.split(input)

        for key in keys:
            # pass the right side into the cryptographic function and XOR
            #   the halfs together
            new_right = left ^ self.cryptographic_function(right, key)
            new_left = right
                        
            # swap the halfs
            left, right = new_left, new_right
            
        # Flip the halfs, and return the result as a string
        output_left = self.rejoin(left)
        output_right = self.rejoin(right)

        return output_right + output_left

    def split(self, input: str) -> int:
        """ A function to split the input of self.encrypt in halfs.
        
    input: the original input to be split in half. If the string has 
        an odd number of characters, one side will be 1 character
        longer than the other.
    returns: an int encoding the characters in input. 
        """
        # Divide the input in half.
        left = input[:len(input)//2]
        right = input[len(input)//2:]

        # Get the character code for each character in the input
        l =  [ord(c) for c in left]
        r = [ord(c) for c in right]

        left = 0
        right = 0

        # Combine the list of ints into 1 unique number coding the input.
        for i in range(len(l) - 1, -1, -1):
            left += l[i] * (10**(i*3))
        for i in range(len(r) - 1, -1, -1):
            right += r[i] * (10**(i*3))
        
        return left, right


    def rejoin(self, input: int) -> str:
        """Recreate a string from an int. """
        # Divide the int into groups of 3, representing 1 character each.
        chars = []
        while input > 0:
            chars.append(input % 1000)
            input //= 1000

        # Get the character coded by each group
        chars = [chr(i) for i in chars]

        # Combine the string.
        return ''.join(chars)
