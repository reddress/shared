;; On lisp p. 6

(mapcar (lambda (n) (* n 10))
        (do* ((x 1 (1+ x))
              (result (list x) (push x result)))
             ((= x 10) (nreverse result))))

(defun my-map (fn lst)
  (if (null lst)
      '()
      (cons (funcall fn (car lst)) (my-map fn (cdr lst)))))

(my-map (lambda (n) (* n 100)) '(1 2 3))

(defun range-from-one (n)
  (do ((x 1 (+ x 1))
       (result '() (cons x result)))
      ((> x n) (nreverse result))))

(defun better-map (fn n)
  (my-map fn (range-from-one n)))
