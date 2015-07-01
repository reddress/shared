(defmacro expr-and-result (form)
  `(format t "~S returns ~S~%" ',form ,form))

(defmacro run-exprs (exprs)
  `(unless (null (list ,@exprs))
     (expr-and-result ,(car exprs))
     (run-exprs ,(cdr exprs))))

(run-exprs ((+ 1 2)
            (+ 3 9)
            (* 2 14)
            (= (/ 4 2) 2)))
