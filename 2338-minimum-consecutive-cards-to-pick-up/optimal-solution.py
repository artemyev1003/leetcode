class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        hand = {}
        min_val = float("inf")

        for index, card in enumerate(cards):
            if card in hand:
                if (curr := index - hand[card] + 1) < min_val:
                    min_val = curr
            hand[card] = index
        return min_val if min_val != float("inf") else -1
