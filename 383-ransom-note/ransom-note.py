class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store = [0]*26
        for a in magazine:
            store[ord("a")- ord(a)]+=1
        for a in ransomNote:
            store[ord("a")- ord(a)]-=1
            if store[ord("a")- ord(a)]<0:
                return False
        return True




        

        