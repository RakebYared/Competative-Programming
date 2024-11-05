class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        inmulti = False
        s = ""
        for line in source:
            i = 0
            while i < len(line)-1:
                if not inmulti:
                    if line[i] == '/' and line[i+1]=="/":
                        break
                    elif line[i] == "/" and line[i+1]=="*":
                        i += 1
                        inmulti = True    
                    else: s+= line[i]
                    i+=1
                while inmulti and i<len(line)-1:
                    if line[i] == '*' and line[i+1]=="/":
                        i+=2
                        inmulti = False
                        break
                    i+=1
            if not inmulti and i == len(line)-1:
                s+=line[i]
            if not inmulti and s: 
                ans.append(s) 
                s = ""
        return ans
    