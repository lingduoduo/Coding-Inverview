class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        else:
            b = "0" * (len(a) - len(b)) + b
        stack1 = list(a)
        stack2 = list(b)
        result = ""
        carry = 0
        while stack1 and stack2:
            s1, s2 = stack1.pop(), stack2.pop()
            curr = int(s1) + int(s2) + carry
            if curr >= 2:
                carry = 1
                curr = curr % 2
            else:
                carry = 0
            result = str(curr) + result
        if carry == 1:
            result = "1" + result
        return result
