;;; repeat function call n times
(defmacro repeat (form times)
  `(dotimes (i ,times)
    ,form))

(let ((base 1))
  (repeat (setf base (* base 2)) 9)
  base)

(repeat-fn (format t "Hello~%") 9)

(defun repeat-fn (f times)
  (dotimes (i times)
    ;; f))    ;; f, by itself, becomes unused
    (format t f)))
