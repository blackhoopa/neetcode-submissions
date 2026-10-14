class Solution:
    def isPalindrome(self, s: str) -> bool:
        fwd = []
        bwd = []
        ns = s.lower()
        ns = ns.replace(" ","")
        for i in ns:
            if i.isalnum() == True: 
                fwd.append(i)
            else:
                continue
        for j in ns[::-1]:
            if j.isalnum() == True:
                bwd.append(j)
            else:
                continue
        print(fwd)
        print(bwd)
        if fwd == bwd:
            return True
        else:
            return False 