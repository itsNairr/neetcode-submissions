class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if len(hand) % groupSize != 0:
        #     return False
        hand.sort()
        count = Counter(hand)
        for num in hand:
            if count[num]:
                for n in range(num, num + groupSize):
                    if not count[n]:
                        return False
                    count[n] -= 1
        return True