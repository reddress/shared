(defun my-insert-to-other (s)
  (other-window 1)
  (end-of-buffer)
  (insert s)
  (other-window 1))