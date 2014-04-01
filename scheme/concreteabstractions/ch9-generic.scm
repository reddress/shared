;; ex. 9.21 p. 275

(define element-of-set?
  (lambda (elt set)
    (set elt)))

(element-of-set? 2 number?)
(element-of-set? 'a number?)

(define add-to-set
  (lambda (elt set)
    (lambda (e)
      (or (set e) (equal? e elt)))))

(element-of-set? 'b (add-to-set 'a number?))

(define number-plus-a? (add-to-set 'a number?))
(element-of-set? 3 number-plus-a?)
(element-of-set? 'a number-plus-a?)

(define number-plus-a-plus-b (add-to-set 'b number-plus-a?))
(element-of-set? 'b number-plus-a-plus-b)
