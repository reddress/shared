(define integers-from-to
  (lambda (low high)
    (if (> low high)
        '()
        (cons low (integers-from-to (+ 1 low) high)))))

(define add-to-end
  (lambda (lst elt)
    (if (null? lst)
        (cons elt '())
        (cons (car lst)
              (add-to-end (cdr lst)
                          elt)))))

(define repeat
  (lambda (value times)
    (if (= 0 times)
        '()
        (cons value (repeat value (- times 1))))))
