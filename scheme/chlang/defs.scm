(define first car)

(define second
  (lambda (lst)
    (car (cdr lst))))

(define rest cdr)

(define length
  (lambda (lst)
    (if (null? lst)
        0
        (+ 1 (length (rest lst))))))

(define nth
  (lambda (lst i)
    (cond ((= i 0)
           (first lst))
          ((> i (- (length lst) 1))
           '())
          (else
           (nth (rest lst) (- i 1))))))

(define empty? null?)

(define (append elt lst)
  (if (empty? lst)
      (list elt)
      (cons (first lst) (append elt (rest lst)))))

(define (reverse lst)
  (define (accum lst2 result)
    (if (empty? lst2)
        result
        (accum (rest lst2) (append (first lst2) result))))
  (accum lst '()))
