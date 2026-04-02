class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        power = 0
        i = 0
        senate = list(senate)
        while i < len(senate):
            print(power)
            if senate[i] == 'R':
                if power < 0:
                    senate.append('D')
                power += 1
            else:
                if power > 0:
                    senate.append('R')
                power -= 1

            i+=1 
        if power > 0:
            return "Radiant"
        else:
            return "Dire"