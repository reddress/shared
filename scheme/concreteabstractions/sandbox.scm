;; (define scheme-folder "/home/heitor/shared/scheme/concreteabstractions/")

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
