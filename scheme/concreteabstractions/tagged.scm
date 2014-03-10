(define working-folder "/home/heitor/shared/scheme/concreteabstractions/")

;; redefine for windows
(when (equal? (build-platform) 'mingw32)
      (define working-folder "C:/Users/Heitor/Desktop/emacs-24.3/bin/shared/scheme/concreteabstractions/"))


(define ark-volume (* (* 300 50) 30))
ark-volume

;; ex. 1.1
(/ (+ (* (- 17 14)
         5)
      6)
   7)

;; ex. 1.2
(define 5%-tax
  (lambda (x) (+ x (* 5/100 x))))

(5%-tax 1.29)
(5%-tax 2.40)

;; ex 1.3
(define f (lambda (x) (* x x)))
(define square (lambda (x) (* x x)))
(f 9)
(square 3)
(define f (lambda (x) (* 2 x)))

(define f (lambda (x) (* x x)))
(define square f)
(f 7)
(square 7)
(define f (lambda (x) (+ x 2)))
(f 7)
(square 7)

;; ex. 1.4
(define candy-temperature
  (lambda (recipe-temp elevation)
    (round 
     (- recipe-temp (/ elevation 500)))))
(candy-temperature 244 5280)

;; ex. 1.5
(define marginal-tax
  (lambda (income)
    (if (< income 10000)
        0
        (* 20/100 (- income 10000)))))
(marginal-tax 12500)

;; ex. 1.6
(define turkey-servings
  (lambda (turkey-weight)
    (if (> turkey-weight 12)
        (/ turkey-weight 1/2)
        (/ turkey-weight 3/4))))
(turkey-servings 9)

;; ex. 1.7
(define puzzle1
  (lambda (a b c)
    "sum of a and larger of b and c"
    (+ a (if (> b c)
             b
             c))))
(puzzle1 10 4 7)

(define puzzle2
  (lambda (x)
    "absolute value"
    ((if (< x 0)
         -
         +)
     0 x)))
(puzzle2 -3)
(puzzle2 9)
(puzzle2 0)

(define (my-load file)
  (load (string-append working-folder file)))

(my-load "fungraph.scm")
(my-load "quilting.scm")

(define eps
  (lambda (image filename)
    (save-image-as-epsf image (string-append working-folder filename ".eps"))))

;; ex. 1.8
(eps (stack (stack rcross-bb corner-bb)
            (stack (quarter-turn-right test-bb) test-bb)) "ex1-8")
(eps (stack rcross-bb corner-bb) "stack")

;; ex. 1.9
(define half-turn
  (lambda (image)
    (quarter-turn-right (quarter-turn-right image))))
(define quarter-turn-left
  (lambda (image)
    (quarter-turn-right (half-turn image))))
(define side-by-side
  (lambda (left right)
    (quarter-turn-right (stack (quarter-turn-left right)
                               (quarter-turn-left left)))))

(eps (side-by-side (half-turn corner-bb)
                   (quarter-turn-left test-bb)) "ex1-9")

;; ex. 1.10
(define pinwheel
  (lambda (image)
    (stack (side-by-side (quarter-turn-right image)
                         (half-turn image))
           (side-by-side image
                         (quarter-turn-left image)))))
(eps (pinwheel test-bb) "ex1-10")

;; ex. 1.11
(define my-corner
  (filled-triangle 0 1 1 1 1 0))
(eps my-corner "mycorner")

(define my-rcross
  (overlay (filled-triangle -0.5 0.5 -0.5 -0.5 0.5 -0.5)
           (filled-triangle -1 1 1 1 -0.5 0.5)
           (filled-triangle -0.5 0.5 1 1 0.5 0.5)
           (filled-triangle 0.5 0.5 1 1 0.5 -0.5)
           (filled-triangle 0.5 -0.5 1 1 1 -1)))
(eps my-rcross "myrcross")

;; ex. 1.12
(define f
  (lambda (x y)
    (if (even? x)
        7
        (* x y))))
(f 1 16)

;; ex. 1.13
(- (* 9 7 3) 9 7)

;; ex. 1.14
(define average
  (lambda (x y)
    (/ (+ x y) 2)))
(average 3 9)

;; ex. 1.15
(define foo
  (lambda (x y)
    (if (= y 0)
        (+ x y)
        (/ x y))))
(foo 9 0)

;; ex. 1.16
(define ladder-height
  (lambda (ladder-length base-distance)
    (sqrt (- (square ladder-length)
             (square base-distance)))))
(ladder-height 10 6)

;; tag-recursion p. 24
(define factorial
  (lambda (n)
    "this version does not end"
    (* (factorial (- n 1))
       n)))

(define factorial
  (lambda (n)
    (if (= n 1)
        1
        (* (factorial (- n 1))
           n))))
(factorial 52)

;; ex. 2.1
(define power
  (lambda (base exponent)
    (if (<= exponent 0)
        1
        (* base (power base (- exponent 1))))))
(power 2 8)
(expt 2 8)

;; ex. 2.2
;; Base case: (factorial 1) terminates with 1
;; Induction hypothesis: assume that (factorial k) terminates with value
;; k! for all k in the range 1 <= k < n
;; Inductive step: consider evaluating (factorial n), with n > 1. This
;; will terminaate if (factorial (- n 1)) does and will have value
;; (* (factorial (- n 1)) n). Because n * (n-1)! = n!, we see that
;; (factorial n) terminates with the correct value for any arbitrary positive
;; n, under the inductive hypothesis:.
;; Conclusion: Therefore, by mathematical induction on n, (factorial n)
;; terminates with the value n! for any positive n

;; ex. 2.3
(define square2.3
  (lambda (n)
    (if (<= n 0)
        0
        (+ (square2.3 (- n 2))
           (- (* 4 n) 4)))))
(square2.3 3)
;; does not work because (- n 2) does not hit zero if n is odd

;; ex. 2.4
(define square2.4
  (lambda (n)
    (if (= n 0)
        0.01
        (if (even? n)
            (* (square2.4 (/ n 2))
               4)
            (+ (square2.4 (- n 1))
               (- (+ n n) 1))))))
(square2.4 6)

(quotient 11 3)
(define quot
  (lambda (n d)
    (if (< n d)
        0
        (+ 1 (quot (- n d) d)))))
(quot 11 3)

(define -n 9)

(define quot
  (lambda (n d)
    (cond ((< d 0) (- (quot n (- d))))
          ((< n 0) (- (quot (- n) d)))
          ((< n d) 0)
          (else (+ 1 (quot (- n d) d))))))
(quot -9 -2)

;; ex. 2.5
(define multiply
  (lambda (a b)
    (cond ((< a 0) (- (multiply (- a) b)))
          ((< b 0) (- (multiply a (- b))))
          ((= a 0) 0)
          (else (+ b (multiply (- a 1) b))))))
(multiply 5 6)

;; ex. 2.6
(define subtract-the-first
  (lambda (n)
    (if (= n 0)
        0
        (- n
           (subtract-the-first (- n 1))))))
;; n))))
;; returns negative of sum of first n integers
(define my-loop
  (lambda (times counter command)
    (when (> times 0)
          (display counter)
          (display " ")
          (display (command counter))
          (newline)
          (my-loop (- times 1) (+ 1 counter) command))))

(my-loop 12 1 subtract-the-first)

;; ex. 2.7
(define sum-integers-from-to
  (lambda (low high)
    (if (> low high)
        0
        (+ (sum-integers-from-to (+ low 1) high)
           low))))
(sum-integers-from-to 1 10)

;; ex. 2.8
(define sum-of-what
  (lambda (n what)
    (if (= n 0)
        0
        (+ (what n) (sum-of-what (- n 1) what)))))
(define sum-of-squares
  (lambda (n)
    (sum-of-what n square)))
(sum-of-squares 30)

(define sum-of-cubes
  (lambda (n)
    (sum-of-what n (lambda (x) (* x x x)))))
(sum-of-cubes 5)  ;; 1 + 8 + 27 + 64 + 125

(define sum-of-powers
  (lambda (n p)
    (sum-of-what n (lambda (x) (expt x p)))))
(sum-of-powers 30 2)

(remainder 9 2)

;; ex. 2.9
;; 106 = f(106) + f(10) + f(1)
(define last-digit-matches
  (lambda (n digit)
    (if (= (remainder n 10) digit)
        1
        0)))
(define count-occurrences
  (lambda (n digit)
    (if (> n 0)
        (+ (last-digit-matches n digit)
           (count-occurrences (quotient n 10) digit))
        0)))
(count-occurrences 12313 3)

;; ex. 2.10
(define count-odd-digits
  (lambda (n)
    (if (> n 0)
        (+ (if (odd? (remainder n 10))
               1
               0)
           (count-odd-digits (quotient n 10)))
        0)))
(count-odd-digits 91123456)

;; ex. 2.11
(define sum-digits
  (lambda (n)
    (if (< n 10)
        n
        (+ (remainder n 10) (sum-digits (quotient n 10))))))
(sum-digits 12345999)
(+ 27 15)

;; ex.2.12
(define find-exp-of-2
  (lambda (n)
    (if (even? n)
        (+ 1 (find-exp-of-2 (/ n 2)))
        0)))
(find-exp-of-2 40)

;; ex. 2.13
;; (stack (stack (stack image)))
(define stack-copies-of
  (lambda (n image)
    (if (<= n 1)
        image
        (stack image (stack-copies-of (- n 1) image)))))
(eps (stack-copies-of 5 rcross-bb) "stack5rcross")

;; ex. 2.14
;; stack-copies-of height
;; then rotate-right
;; stack-copies-of width
;; then rotate-left
(define quilt
  (lambda (image width height)
    (quarter-turn-left
     (stack-copies-of width
                      (quarter-turn-right
                       (stack-copies-of height image))))))
(eps (quilt (pinwheel rcross-bb) 4 3) "rcrossquilt")
(eps (quilt test-bb 4 3) "testbbquilt")

;; ex. 2.15
(define stack-checkered-copies-of
  (lambda (n image)
    (if (<= n 1)
        image
        (stack (if (odd? n)
                   image
                   (invert image))
               (stack-checkered-copies-of (- n 1) image)))))
(define checkerboard
  (lambda (image width height)
    (quarter-turn-left
     (stack-checkered-copies-of width
                                (quarter-turn-right
                                 (stack-checkered-copies-of height image))))))
(eps (stack-checkered-copies-of 5 bitw-bb) "bitwstack")
(eps (checkerboard (pinwheel bitw-bb) 3 3) "bitwcheckered")
(eps (checkerboard (pinwheel rcross-bb) 4 3) "rcrosscheckered")
(eps (checkerboard test-bb 4 5) "testbb45")

;; tag-iteration p. 50
(define factorial-product
  (lambda (a b)
    (if (= b 0)
        a
        (factorial-product (* a b) (- b 1)))))
(define factorial-iter
  (lambda (n)
    (factorial-product 1 n)))
(factorial-iter 6)

;; ex. 3.1
(define alt-factorial-product
  (lambda (result i limit)
    (if (> i limit)
        result
        (alt-factorial-product (* result i) (+ 1 i) limit))))
(define alt-factorial-iter
  (lambda (n)
    (alt-factorial-product 1 1 n)))
(alt-factorial-iter 6)

;; tag-explanation p. 54
;; Recursive PROCEDURES are those that invoke themselves (directly or
;; indirectly).
;; If the self-invocation is to solve a subproblem, whose solution is not
;; the same as the solution to the main problem, the computational PROCESS
;; is a RECURSIVE PROCESS. On the other hand, if the self-invocation is to
;; solve a reduced version (with the same answer as the original), then the
;; process is ITERATIVE.

;; ex. 3.2
(define find-exp-of-2
  (lambda (n)
    (if (even? n)
        (+ 1 (find-exp-of-2 (/ n 2)))
        0)))
(define iter-step-find-exp-of-2
  (lambda (exp n)  ; n = 2^exp * k
    (if (odd? n)
        exp
        (iter-step-find-exp-of-2 (+ 1 exp) (/ n 2)))))
(define iter-find-exp-of-2
  (lambda (n)
    (iter-step-find-exp-of-2 0 n)))
(iter-find-exp-of-2 42)

;; ex. 3.3
(define iter-step-stack-copies-of
  (lambda (result n image)
    (if (= n 1)
        result
        (iter-step-stack-copies-of (stack image result) (- n 1) image))))

(define iter-stack-copies-of
  (lambda (n image)
    (iter-step-stack-copies-of image n image)))
(eps (iter-stack-copies-of 3 rcross-bb) "rcross3stack")

(define iter-step-quilt
  (lambda (image width height)
    (quarter-turn-left
     (iter-stack-copies-of width
                           (quarter-turn-right
                            (iter-stack-copies-of height image))))))
(eps (iter-step-quilt test-bb 2 3) "testbb23")

(define iter-step-stack-checkered-copies-of
  (lambda (result i limit image)
    (if (= i limit)
        result
        (iter-step-stack-checkered-copies-of
         (stack (if (even? i)
                    image
                    (invert image))
                result)
         (+ i 1)
         limit
         image))))
(define iter-stack-checkered-copies-of
  (lambda (n image)
    (iter-step-stack-checkered-copies-of image 1 n image)))
(eps (iter-stack-checkered-copies-of 5 test-bb) "teststack")
(define iter-checkerboard
  (lambda (image width height)
    (quarter-turn-left
     (iter-stack-checkered-copies-of width
                                     (quarter-turn-right
                                      (iter-stack-checkered-copies-of
                                       height image))))))
(eps (iter-checkerboard (pinwheel rcross-bb) 6 5) "rcrosscheckered")

(stack rcross-bb)

;; ex. 3.4
;; Base case: b^0 = 1
;; Induction hypothesis: assume that (power b k) terminates with value
;; b^k for all k in range 1 <= k < n
;; Inductive step: Consider evaluating (power b n), with n > 1. This will
;; terminate if (power b (- n 1)) does, and will have value (* b (power b
;; (- n 1))) that is the correct value for any arbitrary positive n
;; Conclusion: Therefore, by mathematical induction on n, (power b n)
;; terminates with the value b^n for any positive n

;; ex. 3.5
;; n = 2^exp * k
;; n/2 = 2^(exp-1)

(define fermat-number
  (lambda (n)
    (+ (repeatedly-square 2 n) 1)))

(define repeatedly-square
  (lambda (b n)
    (if (= n 0)
        b
        (repeatedly-square (* b b) (- n 1)))))
(fermat-number 4)

(define perfect?
  (lambda (n)
    (= (sum-of-divisors n) (* 2 n))))
(define sum-of-divisors
  (lambda (n)
    (define sum-from-plus  ; sum of all divisors of n which are >= low
      (lambda (low addend) ; plus addend
        (if (> low n)
            addend  ; no divisors of n are greater than n
            (sum-from-plus (+ low 1)
                           (if (divides? low n)
                               (+ addend low)
                               addend)))))
    (sum-from-plus 1 0)))

(define divides?
  (lambda (a b)
    (= (remainder b a) 0)))
(perfect? 33550336)
