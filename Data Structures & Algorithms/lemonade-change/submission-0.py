class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f, t = 0, 0
        for b in bills:
            print(f, t, b)
            if b == 5:
                f += 1
            elif b == 10:
                if f > 0:
                    f -=1
                    t += 1
                else:
                    return False
            else:
                if f > 0 and t > 0:
                    f -= 1
                    t -= 1
                elif f >= 3:
                    f -= 3
                else:
                    return False
        return True
                