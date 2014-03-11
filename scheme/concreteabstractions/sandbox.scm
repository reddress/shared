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
