class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Check if the input 'digits' is an empty string
        if '' == digits: 
            return []
        # Define a dictionary that maps each digit to its associated letters
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        # Use the 'reduce' function to compute the letter combinations
        '''
        It applies a lambda function to each digit in the input string 'digits', starting with an initial value of ['']. The lambda function takes two arguments: acc (the accumulated result so far) and digit (the current digit being processed).
        '''
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])