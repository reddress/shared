(define (my-reverse-iter lst out)
  (if (null? lst)
      out
      (my-reverse-iter (cdr lst) (cons (car lst) out))))

(define (my-reverse lst)
  (my-reverse-iter lst '()))
  

(define (range-iter a b lst)
  (if (> a b)
      (my-reverse lst)
      (range-iter (+ 1 a) b (cons a lst))))

(define (range a b)
  (range-iter a b '()))

(define (primes-up-to-step limit base-multiplier lst)
  ;; (display base-multiplier)
  (if (> base-multiplier (floor (sqrt limit)))
      lst
      (primes-up-to-step limit (+ base-multiplier 2)
                         (filter
                          (lambda (x) (or (= x base-multiplier) (not (= 0 (remainder x base-multiplier)))))
                          lst))))

(define (primes-up-to n)
  (cons 2 (filter odd? (primes-up-to-step n 3 (range 2 n)))))

(primes-up-to 73)
