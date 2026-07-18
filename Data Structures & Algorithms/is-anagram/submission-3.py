"""
unlike sol 1, this strategy instead, uses a dict to track the
character appearance within each word, then compares the ledger,
to see if they are the same
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initialize dicts tracking the letters in each word
        s_dict = {}
        t_dict = {}
        
        for letter in s:
            if not letter in s_dict:
                s_dict[letter] = 0
            
            # add to letter count
            s_dict[letter] += 1
        
        for letter in t:
            if not letter in t_dict:
                t_dict[letter] = 0
            
            # add to letter count
            t_dict[letter] += 1

        # compare dicts
        if s_dict == t_dict:
            return True
        
        return False

        # first check - keys
        # if s_dict.keys() == t_dict.keys():
        #     # second check - values
        #     for key in s_dict:
        #         if not t_dict[key] == s_dict[key]:
        #             return False
            
        #     return True
        # return False
