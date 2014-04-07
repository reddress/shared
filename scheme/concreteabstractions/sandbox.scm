(define scheme-folder "/home/heitor/shared/scheme/concreteabstractions/")

(define (my-load file)
  (load (string-append scheme-folder file)))
(my-load "fungraph.scm")
(my-load "quilting.scm")

(define eps
  (lambda (image filename)
    (save-image-as-epsf image (string-append scheme-folder filename ".eps"))))

;; (eps rcross-bb "rcross")
;; (eps (stack rcross-bb rcross-bb) "rcross2")
;; (eps nova-bb "nova")

(define product
  (lambda (low high)
    (if (> low high)
        1
        (* low (product (+ low 1) high)))))
(product 3 5)

;; joelonsoftware,com test yourself (link from perils of java schools)
(define (accumulate combiner null-value l)
  (if (null? l)
      null-value
      (combiner (car l)
                (accumulate combiner
                            null-value
                            (cdr l)))))
(define (sum-of-squares lst)
  (accumulate (lambda (x y) (
                             + (* x x) y)) 0 lst))
(sum-of-squares '(1 2 3 4 5))

(define (recursive-log n)
  (if (= n 1)
      0
      (+ 1 (recursive-log (/ n 2)))))

(let my-loop
    ((numbers '(3 -2 1 -5 3 2))
     (pos '())
     (neg '()))
  (cond ((null? numbers) (list pos neg))
        ((>= (car numbers) 0)
         (my-loop (cdr numbers)
                  (cons (car numbers) pos)
                  neg))
        (else
         (my-loop (cdr numbers)
                  pos
                  (cons (car numbers) neg)))))

(define my-dupl
  (lambda (orig-lst)
    (define rec
      (lambda (lst acc)
        (if (null? lst)
            acc
            (rec (cdr lst) (cons (car lst) (cons (car lst) acc))))))
    (rec orig-lst '())))
(my-dupl '(1 2 3))

(cons 1 (cons 2 (cons 3 '())))  ;; (1 2 3)

;; p. 175
(define my-filter
  (lambda (ok? lst)
    (cond ((null? lst)
           '())
          ((ok? (car lst))
           (cons (car lst) (my-filter ok? (cdr lst))))
          (else
           (my-filter ok? (cdr lst))))))
(my-filter odd? (integers-from-to 1 9))

(define check-num
  (lambda (n)
    (cond ((< n 0)
           'negative)
          ((= n 0)
           'zero)
          ((> n 0)
           
           'positive))))
(check-num 2)
