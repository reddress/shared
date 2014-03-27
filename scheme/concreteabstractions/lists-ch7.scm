 (define working-folder "/home/heitor/shared/scheme/concreteabstractions/")

;; redefine for windows
(when (equal? (build-platform) 'mingw32)
      (define working-folder "C:/Users/Heitor/Desktop/emacs-24.3/bin/shared/scheme/concreteabstractions/"))

(define (my-load file)
  (load (string-append working-folder file)))

(my-load "library.scm")

(define filter
  (lambda (ok? lst)
    (cond ((null? lst)
           '())
          ((ok? (car lst))
           (cons (car lst) (filter ok? (cdr lst))))
          (else
           (filter ok? (cdr lst))))))

(filter odd? (integers-from-to 1 15))

(define first-elements-of
  (lambda (n lst)
    (if (= n 0)
        '()
        (cons (car lst)
              (first-elements-of (- n 1) (cdr lst))))))

;; ex. 7.10 p. 176
(define my-list-tail
  (lambda (lst n)
    (if (= n 0)
        lst
        (my-list-tail (cdr lst) (- n 1)))))
(my-list-tail '(1 2 3 4 5) 2)

;; p. 176
(define interleave
  (lambda (lst1 lst2)
    (if (null? lst1)
        lst2
        (cons (car lst1)
              (interleave lst2 (cdr lst1))))))

(interleave '(1 2 3 4 5 6 7 8 9) '(a b c d e f))
