class Check:
    def is_palindrome(self, data):
        data = str(data)
        return data == data[::-1]

c = Check()
print(c.is_palindrome("level"))
print(c.is_palindrome(121))
