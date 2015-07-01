;; http://www.joelonsoftware.com/articles/TestYourself.html

(defun accumulate (combiner null-value l)
  (if (endp l)
      null-value
      (funcall combiner (car l)
               (accumulate combiner
                           null-value
                           (cdr l)))))

(defun sum-of-sq (lst)
  (accumulate #'(lambda (x y)
                  (+ (* x x) y))
              0
              lst))
