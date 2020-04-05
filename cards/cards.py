
import random
import collections


CARD_VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
CARD_COLORS = ['CLOVERS', 'SPADES', 'HEARTS', 'DIAMONDS']


def make_deck():
    deck = []
    for color in CARD_COLORS:
        for value in CARD_VALUES:
            deck.append((value, color))

    return deck


def draw_hand(deck, size):
    return random.sample(deck, size)


def run_simulation(hand_size, simulations_amount):
    deck = make_deck()
    results = []
    for _ in range(simulations_amount):
        results.append(draw_hand(deck, hand_size))
    return results


def calc_probs(simulations):
    result = []
    counts = {'Ace': 0, 'Ace And King': 0, 'One Pair': 0, 'Two Pairs': 0, 'Three of a Kind': 0, 'Full House': 0,
              'Flush': 0, 'Four of a Kind': 0}

    for hand in simulations:
        colors = []
        values = []

        for card in hand:
            values.append(card[0])
            colors.append(card[1])

        val_counter = dict(collections.Counter(values))
        col_counter = dict(collections.Counter(colors))

        if 'A' in val_counter.keys():
            counts['Ace'] += 1
        if 'A' in val_counter.keys() and 'K' in val_counter.keys():
            counts['Ace And King'] += 1
        if 2 in val_counter.values():
            counts['One Pair'] += 1
        if list(val_counter.values()).count(2) == 2:
            counts['Two Pairs'] += 1
        if 3 in val_counter.values():
            counts['Three of a Kind'] += 1
        if 2 in val_counter.values() and 3 in val_counter.values():
            counts['Full House'] += 1
        if 4 in val_counter.values():
            counts['Four of a Kind'] += 1
        if 5 in col_counter.values():
            counts['Flush'] += 1

    result.append(('Ace', counts['Ace'] / len(simulations)))
    result.append(('Ace And King', counts['Ace And King'] / len(simulations)))
    result.append(('One Pair', counts['One Pair'] / len(simulations)))
    result.append(('Two Pairs', counts['Two Pairs'] / len(simulations)))
    result.append(('Three of a Kind', counts['Three of a Kind'] / len(simulations)))
    result.append(('Flush', counts['Flush'] / len(simulations)))
    result.append(('Full House', counts['Full House'] / len(simulations)))
    result.append(('Four of a Kind', counts['Four of a Kind'] / len(simulations)))
    return result


if __name__ == '__main__':
    hand_size = int(input('Hand Size -> '))
    sim_amnt = int(input('Simulations Amount -> '))

    simulations = run_simulation(hand_size, sim_amnt)
    for p in calc_probs(simulations):
        print(f'Prob of {p[0]} is: {p[1]}')
