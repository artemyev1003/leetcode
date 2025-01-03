class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        hand = set()
        max_val = 10 ** 5 + 1
        l, min_hand = 0, max_val

        for r in range(len(cards)):
            if cards[r] in hand:
                while cards[r] in hand:
                    hand.remove(cards[l])
                    l += 1
                min_hand = min(min_hand, r - l + 2)
            hand.add(cards[r])
        return min_hand if min_hand != max_val else -1