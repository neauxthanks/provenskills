class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        #the goal of this is to see if the needle is in the haystack. you just need to find the instance in which it occurs first

        haydummy = 0 #pointer for haystack
        needummy = 0 #pointer for needle
        returning = -1
        done = false
        while (not done):
            
            if haydummy == len(haystack) -1:
                done = true
            else: 
                if haystack[haydummy] == needle[needummy]:
                    while (needummy < len(needummy)) - 1:
                        if haystack[haydummy] == needle[needummy]:
                            haydummy+=1
                            needummy+=1
                        else:
                            break
                        