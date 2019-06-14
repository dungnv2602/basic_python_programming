from typing import Callable
from __future__ import annotations
from typing import Sequence, TypeVar
from typing import Sequence, Optional
from typing import NoReturn
from typing import List, Tuple
from typing import List, Sequence
from typing import Dict, List, Tuple
import random
'''The text: str syntax says that the text argument should be of type str. Similarly, the optional align argument should have type bool with the default value True.
Finally, the -> str notation specifies that headline() will return a string.

In terms of style, PEP 8 recommends the following:

Use normal rules for colons, that is, no space before and one space after a colon: text: str.
Use spaces around the = sign when combining an argument annotation with a default value: align: bool = True.
Use spaces around the -> arrow: def headline(...) -> str.
Adding type hints like this has no runtime effect: they are only hints and are not enforced on their own. For instance,
if we use a wrong type for the (admittedly badly named) align argument, the code still runs without any problems or warnings'''


def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f"{text.title()} ".center(50, "o")


print(headline("python type checking"))
print(headline("use mypy", align=True))

name: str = "Guido"
pi: float = 3.142
centered: bool = False


names: List[str] = ["Guido", "Jukka", "Ivan"]
version: Tuple[int, int, int] = (3, 7, 1)
options: Dict[str, bool] = {"centered": False, "capitalize": True}


# In many cases your functions will expect some kind of sequence, and not really care whether it is a list or a tuple. In these cases you should use typing.Sequence when annotating the function argument

def square(elems: Sequence[float]) -> List[float]:
    return [x**2 for x in elems]


# Type Aliases
Card = Tuple[str, str]
Deck = List[Card]


def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

# Functions Without Return Values


def play(player_name: str) -> None:
    print(f"{player_name} plays")


# As a more exotic case, note that you can also annotate functions that are never expected to return normally. This is done using NoReturn:
# Since black_hole() always raises an exception, it will never return properly.


def black_hole() -> NoReturn:
    raise Exception("There is no going back ...")


Choosable = TypeVar("Choosable", str, Card)


def choose(items: Sequence[Choosable]) -> Choosable:
    ...


def player_order(
    names: Sequence[str], start: Optional[str] = None
) -> Sequence[str]:
    ...

# Type Hints for Methods


class Card:
    SUITS = "♠ ♡ ♢ ♣".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, suit: str, rank: str) -> None:  # no using __future__
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        return f"{self.suit}{self.rank}"


# Classes as Types
# Such functionality is planned to become standard in the still mythical Python 4.0. However, in Python 3.7 and later, forward references are available through a __future__ import:
# With the __future__ import you can use Deck instead of "Deck" even before Deck is defined.


class Deck:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards

    @classmethod
    def create(cls, shuffle: bool = False) -> 'Deck':
        """Create a new deck of 52 cards"""
        cards = [Card(s, r) for r in Card.RANKS for s in Card.SUITS]
        if shuffle:
            random.shuffle(cards)
        return cls(cards)


class Player:
    def __init__(self, name: str, hand: Deck) -> None:
        self.name = name
        self.hand = hand

# Annotating *args and **kwargs


class Game:
    def __init__(self, *names: str) -> None:
        """Set up the deck and deal cards to 4 players"""
        deck = Deck.create(shuffle=True)
        self.names = (list(names) + "P1 P2 P3 P4".split())[:4]
        self.hands = {
            n: Player(n, h) for n, h in zip(self.names, deck.deal(4))
        }


'''Callables
Functions are first-class objects in Python. This means that you can use functions as arguments to other functions. That also means that you need to be able to add type hints representing functions.

Functions, as well as lambdas, methods and classes, are represented by typing.Callable. The types of the arguments and the return value are usually also represented. For instance, Callable[[A1, A2, A3], Rt] represents a function with three arguments with types A1, A2, and A3, respectively. The return type of the function is Rt.'''


def do_twice(func: Callable[[str], str], argument: str) -> None:
    print(func(argument))
    print(func(argument))


def create_greeting(name: str) -> str:
    return f"Hello {name}"


do_twice(create_greeting, "Jekyll")
