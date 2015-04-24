(defun add-mixed-list (arglist)
  (apply #'+
         (mapcar (lambda (x)
                   (if (not (numberp x))
                       0
                     x)) arglist)))
