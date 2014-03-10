(define scheme-folder "/home/heitor/shared/scheme/concreteabstractions/")

(define (my-load file)
  (load (string-append scheme-folder file)))
(my-load "fungraph.scm")
(my-load "quilting.scm")

(define eps
  (lambda (image filename)
    (save-image-as-epsf image (string-append scheme-folder filename ".eps"))))

(eps rcross-bb "rcross")
(eps (stack rcross-bb rcross-bb) "rcross2")
(eps nova-bb "nova")
