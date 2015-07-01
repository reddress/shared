(defmacro avg (&rest args)
  `(/ (+ ,@args) ,(length args)))

(macroexpand-1 '(avg 1 2 3))
