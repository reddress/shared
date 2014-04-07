;; p. 31
;; EXPRESSIONS may be primitive, such as numbers and arithmetic operators
;; a COMBINATION is itself an expression, a list containing an operator
;; and operands
(/ 10 5)  ;; a combination

(+ (* 3
      (+ (* 2 4)
         (+ 3 5)))
   (+ (- 10 7)
      6))

(define size 2)
(define pi 3.14)
(define radius 7)
(define circumference (* 2 pi radius))
circumference

;; p. 36
;; (define x 3) is not a combination, but a SPECIAL FORM
(define (square x) (* x x))
(define (sum-of-squares x y)
  (+ (square x)
     (square y)))

(sum-of-squares 3 4)

;; normal-order fully expands then reduces. Evaluator uses applicative-order
;; evaluation, to avoid doing calculations twice.

