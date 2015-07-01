(defun my-reverse (lst)
  (labels ((iter (in out)
             (if (endp in)
                 out
                 (iter (cdr in) (cons (car in) out)))))
    (iter lst '())))

;; out gets updated in each step
;; out is initially '()
;; step 1: (cons 1 '()) is '(1)
;; step 2: (cons 2 '(1)) is '(2 1)

;; consider the first and second steps. Since 2 comes before 1, it follows
;; that the result will be backwards.

;; step 3: (cons 3 '(2 1)) is '(3 2 1)
;; Each step pushes the first element to the front of the result list, so
;; the result is backwards.

;; first element is innermost cons, so first element appears last in the
;; result.
;; last element is last cons, so last element appears first in the result

(defun my-echo (lst)
  (if (endp lst)
      '()
      (cons (car lst) (my-echo (cdr lst)))))

;; computation of my-echo is delayed,
;; it builds its result until the input is empty
;; step 1: (cons 1 (my-echo '(2 3)))
;; step 2: (cons 1 (cons 2 (my-echo '(3))))

;; consider the first two steps. Since (cons 1 (cons 2 ... eventually
;; becomes (1 2 ... , conclude that the resulting order is the same

;; step 3: (cons 1 (cons 2 (cons 3 (my-echo '()))))
;; step 4: (cons 1 (cons 2 (cons 3 '()))) is '(1 2 3)

;; first element is in outermost cons, so first element appears first in
;; the result.
;; last element is innermost cons, so last element appears last in result

(setf my-lst '(1 2 3))

(my-reverse my-lst)
(my-echo my-lst)
