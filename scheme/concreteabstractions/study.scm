;; tag-iteration tag-recursion tag-build-list
;;
;; when iterating (the result lst as a function parameter),
;; the first consed value ends up on the right side. Conses are applied before
;; next iteration

;; when using recursion (cons elt (function (cdr lst))),
;; the first consed value ends up on the left side. Conses are delayed.

;; Iteration:
;; (define lst '())
;; (cons 1 lst) -> (1)
;; (cons 2 lst) -> (2 1)
;; (cons 3 lst) -> (3 2 1)

;; Recursion:
;; (define lst '(1 2 3))
;; (cons (car lst) (func (cdr lst)))
;; (cons 1 (func (cdr lst))) -> (1 ...)
;; (cons 1 (cons 2 (func (cdr lst)))) -> (1 2 ...)
;; (cons 1 (cons 2 (cons 3 '()))) -> (1 2 3)

(define iteration-cdr-down
  (lambda (source result)
    (if (null? source)
        result
        (iteration-cdr-down (cdr source) (cons (car source) result)))))
(iteration-cdr-down '(1 2 3) '())

(define recursion-cdr-down
  (lambda (lst)
    (if (null? lst)
        '()
        (cons (car lst) (recursion-cdr-down (cdr lst))))))
(recursion-cdr-down '(1 2 3))

