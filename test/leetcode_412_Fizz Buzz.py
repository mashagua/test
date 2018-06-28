# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:31:43 2018

@author: user
"""

class Solution:
    def fizzBuzz(self,n):
        """
        :type n: int
        :rtype: List[str]
        """
        list_result=[]
        for i in range(1,(n+1)):
            if (i%3==0) & (i%5==0):
                list_result.append('FizzBuzz')
            elif i%5==0:
                list_result.append('Buzz')
            elif i%3==0:
                list_result.append('Fizz')
            else:
                list_result.append(str(i))
        return list_result

aa=Solution()
print(aa.fizzBuzz(17))

#方法二
class Solution(object):
    def fizzBuzz(self, n):
       return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
