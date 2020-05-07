# A file containing the implementation of a Feistel cipher


class Feistel():
    """ A balanced Feistel network.
    
    The network uses any cryptographic function to encrypt or decrypt a
    message using a balanced Feistel network. """
    def __init__(self, func):
        """Initialize Feistel attributes"""
        self.cryptographic_function = func
        return

    def encrypt(self, input: str, keys: list) -> str:
        """ Perform the encryption on the given message.

        message: A string to be encrypted
        rounds: The number of rounds of encryption to perform
        keys(optional): A list of keys used in the encryption, which are
            passed to the cryptographic function
        
        returns: the excrypted message. """
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
        """ A function to split the input to self.encrypt in halfs.
        
        input: the original input to be split. If the string has an odd 
            length, a space is appended to the end. 
        Returns a list of ascii values of each character in the input. """
        # If the input has an odd number of characters, append a space
        #   to the end.
        if len(input) % 2 != 0:
            input += ' '

        left = input[:len(input)//2]
        right = input[len(input)//2:]

        l =  [ord(c) for c in left]
        r = [ord(c) for c in right]

        left = 0
        right = 0

        for i in range(len(l) - 1, -1, -1):
            left += l[i] * (10**(i*3))
        for i in range(len(r) - 1, -1, -1):
            right += r[i] * (10**(i*3))
        
        return left, right
        # TODO: Maybe larger strings should be split into smaller chunks
        #   after being split in half


    def rejoin(self, input: int) -> str:
        """Recreate a string from an int. """
        # divide the int into groups of 3
        chars = []
        while input > 0:
            chars.append(input % 1000)
            input //= 1000

        # get the ASCII character of each group
        chars = [chr(i) for i in chars]

        # combine the string
        return ''.join(chars)
