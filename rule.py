import itertools
import collections
import numpy as np


class Compare:
    def __init__(self):
        self.pat_compare_dict = {'Spade': 4, 'Hearts': 3, 'Club': 2, 'Diamond': 1}
        CARD_NUM = [x for x in range(1, 14)]
        CARD_PATTERN = ['Diamond', 'Club', 'Hearts', 'Spade']
        list_of_card = [(num, pattern) for num, pattern in itertools.product(CARD_NUM, CARD_PATTERN)]
        list_of_card_sorted = list_of_card[8:] + list_of_card[:8]
        self.card_points_dict = {card: points for card, points in zip(list_of_card_sorted, range(1, 53))}

    def compare_pattern(self, pat1, pat2):
        val_1 = self.pat_compare_dict[pat1]
        val_2 = self.pat_compare_dict[pat2]
        if val_1 > val_2:
            return 1
        elif val_2 > val_1:
            return -1
        else:
            return 0

    def straight_flush(self,cards):
        card_num = [card.number for card in cards]
        card_pat = [card.pattern for card in cards]
        if len(set(card_pat)) != 1:
            return 0
        if np.diff(card_num).sum() == len(card_num):
            return np.max([self.card_points_dict[(num, pat)] for num, pat in zip(card_num, card_pat)])
        else:
            return 0

    @staticmethod
    def four_of_a_kind(cards):
        card_num = [card.number for card in cards]
        collect_counter = collections.Counter(card_num)
        if 4 in [count for item, count in collect_counter.items()]:
            return [num for num, count in collect_counter.items() if count == 4][0]
        else:
            return 0

    @staticmethod
    def full_house(cards):
        card_num = [card.number for card in cards]
        collect_counter = collections.Counter(card_num)
        card_counts = [count for item, count in collect_counter.items()]
        if 3 in card_counts and 2 in card_counts:
            return [num for num, count in collect_counter.items() if count == 3][0]
        else:
            return 0

    def flush(self, cards):
        card_pat = [card.pattern for card in cards]
        if len(set(card_pat)) == 1:
            return self.pat_compare_dict[list(set(set(card_pat)))[0]]
        else:
            return 0

    def flush_compare(self, cards_1, cards_2):
        card_num_1 = [card.number for card in cards_1]
        card_pat_1 = [card.pattern for card in cards_1]
        card_num_2 = [card.number for card in cards_2]
        card_pat_2 = [card.pattern for card in cards_1]
        card_value_1 = [self.card_points_dict[(num, pat)] for num, pat in zip(card_num_1, card_pat_1)]
        card_value_2 = [self.card_points_dict[(num, pat)] for num, pat in zip(card_num_2, card_pat_2)]
        return np.max(card_value_1) > np.max(card_value_2)

    def straight(self, cards):
        card_num = [card.number for card in cards]
        card_pat = [card.pattern for card in cards]
        if np.diff(card_num).sum() == len(card_num):
            return np.max([self.card_points_dict[(num, pat)] for num, pat in zip(card_num, card_pat)])
        else:
            return 0

    @staticmethod
    def three_of_a_kind(cards):
        card_num = [card.number for card in cards]
        collect_counter = collections.Counter(card_num)
        if 3 in [count for item, count in collect_counter.items()]:
            return [num for num, count in collect_counter.items() if count == 4][0]
        else:
            return 0

    def pair(self, cards):
        card_num = [card.number for card in cards]
        collect_counter = collections.Counter(card_num)
        if 2 in [count for item, count in collect_counter.items()]:
            pair_num = [num for num, count in collect_counter.items() if count == 2][0]
            pair = [card for card in cards if card.number == pair_num]
            return np.max([self.card_points_dict[(pair[0].number, pair[0].pattern)],
                          self.card_points_dict[(pair[1].number, pair[1].pattern)]])
        else:
            return 0

    def high_card(self, cards):
        card_num = [card.number for card in cards]
        card_pat = [card.pattern for card in cards]
        return np.max([self.card_points_dict[(num, pat)] for num, pat in zip(card_num, card_pat)])

    def compare(self, cards1, cards2):
        if self.straight_flush(cards1) == self.straight_flush(cards2):
            pass
        else:
            return self.straight_flush(cards1) > self.straight_flush(cards2)

        if self.four_of_a_kind(cards1) == self.four_of_a_kind(cards2):
            pass
        else:
            return self.four_of_a_kind(cards1) > self.four_of_a_kind(cards2)

        if self.full_house(cards1) == self.full_house(cards2):
            pass
        else:
            return self.full_house(cards1) > self.full_house(cards2)

        if self.flush(cards1) == self.flush(cards2):
            pass
        else:
            return self.flush(cards1) > self.flush(cards2)

        if self.straight(cards1) == self.straight(cards2):
            pass
        else:
            return self.straight(cards1) > self.straight(cards2)

        if self.three_of_a_kind(cards1) == self.three_of_a_kind(cards2):
            pass
        else:
            return self.three_of_a_kind(cards1) > self.three_of_a_kind(cards2)

        if self.pair(cards1) == self.pair(cards2):
            pass
        else:
            return self.pair(cards1) > self.pair(cards2)

        if self.high_card(cards1) == self.high_card(cards2):
            pass
        else:
            return self.high_card(cards1) > self.high_card(cards2)
