from random import randint
class Solution(object):

    def __init__(self, nums):
        self.original = nums
        self.copy = [i for i in nums]

    def reset(self):
        return self.original
        
        

    def shuffle(self):
        l = len(self.copy)
        for i in xrange(l):
            t = randint(i,l-1)
            self.copy[t], self.copy[i] = self.copy[i], self.copy[t]
        return self.copy
