# Obviously -- this file should run without a game of wordle happening. If that's not possible something is wrong!

print("Test check_word")
from wordle import check_word

# Tests based largely on the examples in the pdf
print(
    check_word("LERED", "RADIO")
)  # ['yellow', 'grey', 'yellow', 'grey', 'grey']
print(
    check_word("LERED", "DRUID")
)  # ['grey', 'yellow', 'grey', 'grey', 'green']
print(
    check_word("LERED", "LERED")
)  # ['green', 'green', 'green', 'green', 'green']
print(
    check_word("PERIS", "RAISE")
)  # ['yellow', 'grey', 'yellow', 'yellow', 'yellow']
print(
    check_word("OPENS", "EPICS")
)  # ['yellow', 'green', 'grey', 'grey', 'green']
print(
    check_word("MISTS", "MISTY")
)  # ['green', 'green', 'green', 'green', 'grey']
print(
    check_word("ELUDE", "LEDGE")
)  # ['yellow', 'yellow', 'yellow', 'grey', 'green']
print(
    check_word("CRANE", "BEEPS")
)  # ['grey', 'yellow', 'grey', 'grey', 'grey']
print(
    check_word("ROBOT", "REORG")
)  # ['green', 'grey', 'yellow', 'grey', 'grey']
print(
    check_word("BOOKS", "SHOES")
)  # ['grey', 'grey', 'green', 'grey', 'green']


print("Test known_word")
from wordle import known_word

# First block of tests is from the examples on page 6.

clues = []
print(known_word(clues))  # _____

clues = [("RADIO", ["yellow", "grey", "yellow", "grey", "grey"])]
print(known_word(clues))  # _____

clues = [
    ("RADIO", ["yellow", "grey", "yellow", "grey", "grey"]),
    ("DRUID", ["grey", "yellow", "grey", "grey", "green"]),
]
print(known_word(clues))  # ____D

clues = [
    ("RADIO", ["yellow", "grey", "yellow", "grey", "grey"]),
    ("DRUID", ["grey", "yellow", "grey", "grey", "green"]),
    ("LERED", ["green", "green", "green", "green", "green"]),
]
print(known_word(clues))  # LERED

# Next a more contrived examples. Let's say the user is being strategic:

clues = [("TUNES", ["yellow", "green", "green", "grey", "green"])]
print(known_word(clues))  # _UN_S

clues = [
    ("TUNES", ["yellow", "green", "green", "grey", "green"]),
    ("ALPHA", ["green", "grey", "grey", "grey", "grey"]),
]
print(known_word(clues))  # AUN_S

clues = [
    ("TUNES", ["yellow", "green", "green", "grey", "green"]),
    ("ALPHA", ["green", "grey", "grey", "grey", "grey"]),
    ("MONTH", ["grey", "grey", "green", "green", "grey"]),
]
print(known_word(clues))  # AUNTS

clues = [
    ("TUNES", ["yellow", "green", "green", "grey", "green"]),
    ("ALPHA", ["green", "grey", "grey", "grey", "grey"]),
    ("MONTH", ["grey", "grey", "green", "green", "grey"]),
    ("DUMMY", ["grey", "green", "grey", "grey", "grey"]),
]
print(known_word(clues))  # AUNTS

clues = [
    ("TUNES", ["yellow", "green", "green", "grey", "green"]),
    ("ALPHA", ["green", "grey", "grey", "grey", "grey"]),
    ("MONTH", ["grey", "grey", "green", "green", "grey"]),
    ("DUMMY", ["grey", "green", "grey", "grey", "grey"]),
    ("AUNTS", ["green", "green", "green", "green", "green"]),
]
print(known_word(clues))  # AUNTS


print("Test no_letters")
from wordle import no_letters

# First block of tests is from the examples on page 6.

clues = []
print(no_letters(clues))  # (empty line)
clues = [("RADIO", ["yellow", "grey", "yellow", "grey", "grey"])]
print(no_letters(clues))  # AIO

clues = [
    ("RADIO", ["yellow", "grey", "yellow", "grey", "grey"]),
    ("DRUID", ["grey", "yellow", "grey", "grey", "green"]),
]
print(no_letters(clues))  # AIOU

clues = [
    ("RADIO", ["yellow", "grey", "yellow", "grey", "grey"]),
    ("DRUID", ["grey", "yellow", "grey", "grey", "green"]),
    ("LERED", ["green", "green", "green", "green", "green"]),
]
print(no_letters(clues))  # AIOU

# Next a more contrived examples.
# first -- making sure things stay sorted.
clues = [("YELPS", ["grey", "grey", "grey", "green", "green"])]
print(no_letters(clues))  # ELY

clues = [
    ("YELPS", ["grey", "grey", "grey", "green", "green"]),
    ("ZUMBA", ["grey", "green", "green", "yellow", "grey"]),
]
print(no_letters(clues))  # AELYZ

# next let's check for good/bad duplicate behavior
clues = [
    ("YELPS", ["grey", "grey", "grey", "green", "green"]),
    ("ZUMBA", ["grey", "green", "green", "yellow", "grey"]),
    ("YELPS", ["grey", "grey", "grey", "green", "green"]),
]
print(no_letters(clues))  # AELYZ

clues = [
    ("YELPS", ["grey", "grey", "grey", "green", "green"]),
    ("ZUMBA", ["grey", "green", "green", "yellow", "grey"]),
    ("YELPS", ["grey", "grey", "grey", "green", "green"]),
    ("BOOKS", ["green", "grey", "grey", "grey", "green"]),
]
print(no_letters(clues))  # AEKLOYZ

# finally, let's test the tricky case where things are mixed yellow/grey and green/grey

clues = [
    ("YELPS", ["grey", "grey", "grey", "green", "green"]),
    ("ZUMBA", ["grey", "green", "green", "yellow", "grey"]),
    ("YELPS", ["grey", "grey", "grey", "green", "green"]),
    ("BOOKS", ["green", "grey", "grey", "grey", "green"]),
    ("HIPPO", ["grey", "grey", "grey", "green", "grey"]),
]
print(no_letters(clues))  # AEHIKLOYZ

clues = [
    ("YELPS", ["grey", "grey", "grey", "green", "green"]),
    ("ZUMBA", ["grey", "green", "green", "yellow", "grey"]),
    ("YELPS", ["grey", "grey", "grey", "green", "green"]),
    ("BOOKS", ["green", "grey", "grey", "grey", "green"]),
    ("HIPPO", ["grey", "grey", "grey", "green", "grey"]),
    ("SOCKS", ["grey", "grey", "grey", "grey", "green"]),
]
print(no_letters(clues))  # ACEHIKLOYZ

clues = [("BOOKS", ["grey", "yellow", "grey", "grey", "green"])]
print(no_letters(clues))  # BK


print("Test yes_letters")
from wordle import yes_letters

# First block of tests is from the examples on page 6.

clues = []
print(yes_letters(clues))  # (empty line)

clues = [("RADIO", ["yellow", "grey", "yellow", "grey", "grey"])]
print(yes_letters(clues))  # DR

clues = [
    ("RADIO", ["yellow", "grey", "yellow", "grey", "grey"]),
    ("DRUID", ["grey", "yellow", "grey", "grey", "green"]),
]
print(yes_letters(clues))  # DR

clues = [
    ("RADIO", ["yellow", "grey", "yellow", "grey", "grey"]),
    ("DRUID", ["grey", "yellow", "grey", "grey", "green"]),
    ("LERED", ["green", "green", "green", "green", "green"]),
]
print(yes_letters(clues))  # DELR

# A few more focused examples.
# first let's be sure repeated and mixed clues work.

clues = [("BOOKS", ["yellow", "yellow", "grey", "grey", "grey"])]
print(yes_letters(clues))  # BO

clues = [
    ("BOOKS", ["yellow", "yellow", "grey", "grey", "grey"]),
    ("ELECT", ["green", "green", "grey", "grey", "grey"]),
]
print(yes_letters(clues))  # BELO

clues = [("BEBOP", ["grey", "yellow", "green", "green", "grey"])]
print(yes_letters(clues))  # BEO


print("Test filter_word_list")
# note -- since we didn't specify an order for this function testing it gets a little _funky_
from easy_wordle import filter_word_list
from words import words

original_words = (
    words.copy()
)  # we'll want to check if you're messing up the words list!

clues = []
result = filter_word_list(words, clues)
print(words == original_words)  # True
print(len(words) == len(result))  # True
print(set(words) == set(result))  # True

words = original_words
clues = [("RAISE", ["yellow", "grey", "yellow", "yellow", "yellow"])]
result = filter_word_list(words, clues)
print(words == original_words)  # True
print(len(result))  # 39
expected = [
    "miser",
    "wires",
    "siler",
    "tiers",
    "sider",
    "sevir",
    "siker",
    "peris",
    "speir",
    "sizer",
    "sweir",
    "serir",
    "meris",
    "kiers",
    "vires",
    "tires",
    "sehri",
    "hires",
    "fiers",
    "cires",
    "sieur",
    "siver",
    "biers",
    "serif",
    "fires",
    "sixer",
    "epris",
    "liers",
    "siren",
    "serin",
    "icers",
    "piers",
    "sired",
    "sires",
    "seric",
    "viers",
    "wiser",
    "breis",
    "mires",
]
print(set(expected) == set(result))  # True

words = original_words
clues = [
    ("RAISE", ["yellow", "grey", "yellow", "yellow", "yellow"]),
    ("SERIF", ["yellow", "green", "green", "green", "grey"]),
]
result = filter_word_list(words, clues)
print(words == original_words)  # True
print(len(result))  # 2
expected = ["peris", "meris"]
print(set(expected) == set(result))  # True

words = original_words
clues = [
    ("RAISE", ["yellow", "grey", "yellow", "yellow", "yellow"]),
    ("SERIF", ["yellow", "green", "green", "green", "grey"]),
    ("MERIS", ["grey", "green", "green", "green", "green"]),
]
print(filter_word_list(words, clues))  # ['peris']

# The words list doesn't have to be the given word list!
dum_words = ["aaaaa", "bbbbb", "ccccc", "ddddd"]
clues = [("APPLE", ["green", "grey", "grey", "grey", "grey"])]
print(filter_word_list(dum_words, clues))  # ['aaaaa']

# And let's bring back a few of the earlier test and see if we can't narrow down the words...
clues = [("TUNES", ["yellow", "green", "green", "grey", "green"])]
result = filter_word_list(words, clues)
expected = [
    "munts",
    "runts",
    "lunts",
    "punts",
    "funts",
    "sunts",
    "aunts",
    "cunts",
    "hunts",
    "bunts",
    "dunts",
]
print(set(result) == set(expected))

clues = [
    ("TUNES", ["yellow", "green", "green", "grey", "green"]),
    ("ALPHA", ["green", "grey", "grey", "grey", "grey"]),
]
print(filter_word_list(words, clues))  # ['aunts']
clues = [
    ("TUNES", ["yellow", "green", "green", "grey", "green"]),
    ("ALPHA", ["green", "grey", "grey", "grey", "grey"]),
    ("MONTH", ["grey", "grey", "green", "green", "grey"]),
]
print(filter_word_list(words, clues))  # ['aunts']

clues = [
    ("TUNES", ["yellow", "green", "green", "grey", "green"]),
    ("ALPHA", ["green", "grey", "grey", "grey", "grey"]),
    ("MONTH", ["grey", "grey", "green", "green", "grey"]),
    ("DUMMY", ["grey", "green", "grey", "grey", "grey"]),
]
print(filter_word_list(words, clues))  # ['aunts']

clues = [
    ("TUNES", ["yellow", "green", "green", "grey", "green"]),
    ("ALPHA", ["green", "grey", "grey", "grey", "grey"]),
    ("MONTH", ["grey", "grey", "green", "green", "grey"]),
    ("DUMMY", ["grey", "green", "grey", "grey", "grey"]),
    ("AUNTS", ["green", "green", "green", "green", "green"]),
]
print(filter_word_list(words, clues))  # ['aunts']


clues = [
    ("YELPS", ["grey", "grey", "grey", "green", "green"]),
    ("ZUMBA", ["grey", "green", "green", "yellow", "grey"]),
]
print(filter_word_list(words, clues))  # ['bumps']

clues = [
    ("YELPS", ["grey", "grey", "grey", "green", "green"]),
    ("ZUMBA", ["grey", "green", "green", "yellow", "grey"]),
    ("YELPS", ["grey", "grey", "grey", "green", "green"]),
]
print(filter_word_list(words, clues))  # ['bumps']


clues = [
    ("RADIO", ["yellow", "grey", "yellow", "grey", "grey"]),
    ("DRUID", ["grey", "yellow", "grey", "grey", "green"]),
]
result = filter_word_list(words, clues)
expected = [
    "gyred",
    "cered",
    "mered",
    "spred",
    "shred",
    "sered",
    "sherd",
    "lered",
    "tyred",
]
print(set(result) == set(expected))  # True

clues = [
    ("RADIO", ["yellow", "grey", "yellow", "grey", "grey"]),
    ("DRUID", ["grey", "yellow", "grey", "grey", "green"]),
    ("LERED", ["green", "green", "green", "green", "green"]),
]
print(filter_word_list(words, clues))  # ['lered']


clues = [
    ("BOOKS", ["yellow", "yellow", "grey", "grey", "grey"]),
    ("ELECT", ["green", "green", "grey", "grey", "grey"]),
]
print(filter_word_list(words, clues))  # ['elbow']

clues = [("BEBOP", ["grey", "yellow", "green", "green", "grey"])]
result = filter_word_list(words, clues)
expected = ["elbow", "embox", "syboe", "embow", "embog"]
print(set(expected) == set(result))  # True

"""
EXPECTED OUTPUT


Test check_word
['yellow', 'grey', 'yellow', 'grey', 'grey']
['grey', 'yellow', 'grey', 'grey', 'green']
['green', 'green', 'green', 'green', 'green']
['yellow', 'grey', 'yellow', 'yellow', 'yellow']
['yellow', 'green', 'grey', 'grey', 'green']
['green', 'green', 'green', 'green', 'grey']
['yellow', 'yellow', 'yellow', 'grey', 'green']
['grey', 'yellow', 'grey', 'grey', 'grey']
['green', 'grey', 'yellow', 'grey', 'grey']
['grey', 'grey', 'green', 'grey', 'green']
Test known_word
_____
_____
____D
LERED
_UN_S
AUN_S
AUNTS
AUNTS
AUNTS
Test no_letters

AIO
AIOU
AIOU
ELY
AELYZ
AELYZ
AEKLOYZ
AEHIKLOYZ
ACEHIKLOYZ
BK
Test yes_letters

DR
DR
DELR
BO
BELO
BEO
Test filter_word_list
True
True
True
True
39
True
True
2
True
['peris']
['aaaaa']
True
['aunts']
['aunts']
['aunts']
['aunts']
['bumps']
['bumps']
True
['lered']
['elbow']
True


"""
