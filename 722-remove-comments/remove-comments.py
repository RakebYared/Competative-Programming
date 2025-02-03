class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        is_multi = False
        res = []
        for line in source:
            i = 0
            if not is_multi:
                not_comment = []
            while i < len(line)-1:
                if not is_multi:
                    if line[i] == '/' and line[i+1] == '/': 
                        break
                    elif line[i] == '/' and line[i+1] == '*':
                        i+=1
                        is_multi = True
                    else:
                        not_comment.append(line[i])
                i+=1
                while is_multi and i<len(line)-1:
                    if line[i] == '*' and line[i+1] == '/':
                        is_multi = False
                        i+=1
                    i+=1
            if not is_multi:
                if i == len(line)-1:
                    not_comment.append(line[i])
                if not_comment: 
                    res.append(''.join(not_comment))
        return res