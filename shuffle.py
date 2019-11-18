import time


def do_a_shuffle():
    """
    do...a...shuffle...
    shuffling is better if you do it a few different ways
    """
    print(wash(split_and_merge(amateur_odd_chop(build_deck()))))


def build_deck(n=52):
    """
    does what it says on the tin
    """
    return [card for card in range(0, n)]


def random_bit():
    """
    Is it really random? Probably...
    """
    return int(str(time.time_ns())[-5]) % 2


def random_bit_more(n=5):
    """
    sum of n random_bit()s
    """
    return max(1, sum([random_bit() for i in range(0, n)]))


def split_and_merge(deck):
    """
    the shuffle where the dealer splits the deck in roughly two
    and then flicks them back together thinking he/she is cool
    """
    shuffled_deck = []
    l_hand = deck[:len(deck) // 2]
    r_hand = deck[len(deck) // 2:]
    if random_bit():
        l_hand.append(r_hand.pop())
    else:
        r_hand.append(l_hand.pop())

    while len(shuffled_deck) != len(deck):
        if random_bit() and len(l_hand):
            shuffled_deck.append(l_hand.pop())
        elif len(r_hand):
            shuffled_deck.append(r_hand.pop())

    return shuffled_deck


def wash(deck):
    """
    the shuffle where the dealer chucks the cards on a table and does the karate kid thing
    """
    shuffled_deck = []

    def wax_on_wax_off(d, t):
        while len(d):
            for card in d:
                if random_bit():
                    d.remove(card)
                    t.append(card)
        return t

    for _ in range(0, random_bit_more()):
        shuffled_deck = wax_on_wax_off(deck, shuffled_deck)

    return shuffled_deck


def amateur_odd_chop(deck):
    """
    the shuffle that I can do
    """
    can_be_bothered = True
    so_many_times = 0
    while can_be_bothered:
        grabbed = random_bit_more()
        deck = deck[grabbed:] + deck[0:grabbed]
        if time.localtime().tm_wday in (4, 5):  # it's Friday or Saturday
            can_be_bothered = random_bit()
        elif time.localtime().tm_hour >= 22:  # it's getting late
            can_be_bothered = random_bit()
        elif so_many_times > 50:  # maybe I'll stop
            can_be_bothered = random_bit()
        elif so_many_times > 500:  # ok let's stop
            can_be_bothered = False
        so_many_times += 1

    return deck
