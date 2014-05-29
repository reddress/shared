NB. convert f to c if x is 'c', otherwise c to f

convert =: dyad : 0
if. x = 'c'
 do. centigrade y
 else. fahrenheit y
end.
)

centigrade =: 3 : 0
t1 =. y - 32
t2 =. t1 * 5
t3 =. t2 % 9
)

fahrenheit =: 3 : 0
t1 =. y * 9
t2 =. t1 % 5
t3 =. t2 + 32
)

localf_q_ =. 3 : 0
y
)

localg_base_ =. 3 : 0
y
)