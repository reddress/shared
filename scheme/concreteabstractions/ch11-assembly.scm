(define factorial-product
  (lambda (a b)
    (if (= b 0)
        a
        (factorial-product (* a b) (- b 1)))))

(define two-factorials
  (lambda (n)
    (+ (factorial-product 1 n)
       (factorial-product 1 (* 2 n)))))
(two-factorials 3)
(factorial-product 1 3)
(factorial-product 1 6)

(define v (make-vector 17))
(vector-set! v 13 7)
v
(vector-ref v 13)
