import re


class PalindromeChecker(object):

    def __init__(self):
        self.character = re.compile(r"[a-zA-Z]")

    def __call__(self, string):
        return self.is_palindrome(string)

    def is_palindrome(self, string):
        if len(string) == 0 or len(string) == 1:
            return True
        elif re.match(self.character, string[0]) is None:
            return self.is_palindrome(string[1:])
        elif re.match(self.character, string[-1]) is None:
            return self.is_palindrome(string[:-1])
        elif string[0] == string[-1]:
            return self.is_palindrome(string[1:-1])
        else:
            return False
