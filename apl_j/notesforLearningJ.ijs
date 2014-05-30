NB. p. 15

x =: 5 4 1 9 2 0
x > 2
x -. (x * (-. x < 5))   NB. n00b filter, keeping numbers satisfying x < 5
(x * x < 5) -. 0        NB. better, but still breaks when 0 is in x

# x                     NB. "tally" counts the length of the list

x =: 1 + 2 3 4
x = x
+/ x = x
+/ (x = x)              NB. 3
(+/ x) = x              NB. 0 0 0

y =: 6 7 8 9 10
(0 = 3 | y) # y         NB. 1337 filter: select items from right argument

x =: 5 4 1 9 2 0
(x < 5) # x             NB. as first filter above

NB. largest number p. 20
>. / 1 6 5
1 >. 6 >. 5

NB. shape $ values
3 $ 1
2 3 4 $ 1               NB. planes, rows, columns

NB. p. 27 Rank is the dimension count of an array (everything is an array).
NB. Single numbers have rank 0, lists are rank-1 arrays, tables rank-2,
NB. and so on. Arrays with rank 3 and higher are called "reports".

NB. p. 29