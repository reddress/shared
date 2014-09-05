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

