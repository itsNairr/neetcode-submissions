class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        power = 0
        i = 0
        senate = list(senate)
        while i < len(senate):
            print(power)
            if senate[i] == 'R':
                power += 1
                if power <= 0:
                    senate.append('D')
            else:
                power -= 1
                if power >= 0:
                    senate.append('R')


            i+=1 
        print(power)
        if power > 0:
            return "Radiant"
        else:
            return "Dire"