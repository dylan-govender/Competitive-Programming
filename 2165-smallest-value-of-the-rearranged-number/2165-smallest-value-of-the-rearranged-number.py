class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            s = sorted(str(num))
            min_chr = min(s)
            n = len(s)
            i = 0
            while i < n:
                if s[i] != '0':
                    min_chr = s[i]
                    s[0], s[i] = s[i], s[0]
                    break
                i += 1
            return int(''.join(s))
        else:
            s = sorted(str(abs(num)), reverse=True)
            return int('-'+''.join(s))
        
        
        
        