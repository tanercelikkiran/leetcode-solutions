class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A = int(a, 2) #Converts the binary string to an integer
        B = int(b, 2) #Converts the binary string to an integer
        binary_sum = A + B #Adds the two integers
        return bin(binary_sum)[2:] #Converts the sum to a binary string