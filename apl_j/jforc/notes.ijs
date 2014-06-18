NB. p. 15

1 2 + 3
3 + 1 2

NB. p. 16

h =. verb : '''Hello world.'''
h ''

1 - 10

NB. p. 21 adjacent named nouns (a b) do not join as a list

a =. 2
b =. 3
NB. a b     NB. syntax error, is equivalent to (2) (3)

NB. p. 22 assignment

a =. 1 + b =. 5
a  NB. 6 right-to-left execution
b  NB. 5

NB. p. 23
_5 + _4  NB. _9

-5 + -4  NB. _1 because - is applied to 1

a =. 3 + b =. 4 * 1 + 4
a  NB. 23
b  NB. 20

NB. p. 25 special names x, y, u, v, m, n represent arguments

NB. verb define without a : will implicitly be monadic, otherwise use
NB. "monad define" or "dyad define". When defining both:
NB. f =: verb define
NB. [ monadic case here ]
NB. :
NB. [ dyadic case here ]
NB. )

NB. alternatively,
NB. f =: monad : 'text of verb'
NB. f =: dyad : 'text of verb'

add2x3y =: dyad : '(2 * x) + 3 * y'
10 add2x3y 100  NB. 320
1 2 3 add2x3y 4 5 6

c =: 30