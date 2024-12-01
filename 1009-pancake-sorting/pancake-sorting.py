class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        order = {x:y for y,x in enumerate(sorted(arr))}
        k = []
        for key in list(order.keys())[::-1]:
            if arr == list(order.keys()):
                return k
            for i in range(len(arr)):
                if arr[i] == key:
                    if i == order[key]:
                        break
                    else:
                        k.append(i+1)
                        k.append(order[key]+1)
                        arr[:i+1] = reversed(arr[:i+1])
                        arr[:order[key]+1] = reversed(arr[:order[key]+1])