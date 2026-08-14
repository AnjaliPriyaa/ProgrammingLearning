class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        # if len(s) == len(t):
        #     for i,j in zip(s,t):
        #         if i not in dict1:
        #             dict1[i]=0
        #         if j not in dict2:
        #             dict2[j]=0
        #         dict1[i]+=1
        #         dict2[j]+=1
        #     if dict1 == dict2:
        #         return True
        # return False
        if len(s) == len(t):
            for i, j in zip(s, t):
                dict1[i] = dict1.get(i, 0) + 1
                dict2[j] = dict2.get(j, 0) + 1

            return dict1 == dict2

        return False
                
        