(setq python-shell-interpreter "/home/tinacgh/.local/bin/python3")
(add-to-list 'default-frame-alist '(tty-color-mode  . -1))

(global-set-key (kbd "RET") 'newline-and-indent)

(global-set-key (kbd "<f5>") 'run-python)
(global-set-key (kbd "<f6>") 'eval-print-last-sexp)
(global-set-key (kbd "<f7>") 'make-directory)
(global-set-key (kbd "<f8>") 'kill-this-buffer)
(global-set-key (kbd "<f9>") 'find-file)
(global-set-key (kbd "<f10>") 'save-buffer)
(global-set-key (kbd "<f11>") 'write-file)
(global-set-key (kbd "<f12>") 'split-window-below)

(global-set-key (kbd "<M-up>") 'other-window)
(global-set-key (kbd "<M-down>") 'other-window)

(defun my-python-send-statement ()
  (interactive)
  (local-set-key [S-return] 'my-python-send-statement)
  (python-shell-send-string (thing-at-point 'line))
  (python-shell-send-string "\n")
  (move-end-of-line nil))

(defun trim-string (string)
  "Remove white spaces in beginning and ending of STRING.
White space here is any of: space, tab, emacs newline (line feed, ASCII 10)."
  (replace-regexp-in-string "\\`[ \t\n]*" "" (replace-regexp-in-string "[ \t\n]*\\'" "" string)))

;;; send paragraph is the new hotness, send-block is old and busted
(defun my-python-send-paragraph ()
  (interactive)
  (save-excursion
    ;;; (mark-paragraph)
    ;;; (call-interactively 'python-shell-send-region)))
    ;; (python-shell-send-string "print(\"--SENT--\")")
    (python-shell-send-string (concat "print('''\n"
                                      (trim-string (thing-at-point 'paragraph)) "''')"))
    (python-shell-send-string (concat "print()\n" (trim-string (thing-at-point 'paragraph))))))

(defun my-python-send-buffer ()
  (interactive)
  (save-excursion
    ;;; (end-of-buffer))
    ;; (python-shell-send-string "print(\"--SENT--\")")
    (python-shell-send-string (concat "print('''" (trim-string (buffer-string)) "''')"))
    ;; (mark-whole-buffer)
    ;; (call-interactively 'python-shell-send-region)))
    (python-shell-send-string (concat "print('')\n" (trim-string (buffer-string))))))

(defun my-python-test-buffer ()
  (interactive)
  (save-excursion
    ;; (python-shell-send-string (concat "print('')\n" (trim-string (buffer-string))))
    (python-shell-send-string (trim-string (buffer-string)))
    (python-shell-send-string (concat "print('')\n" "test()"))))

(defun my-python-send-block ()
  (interactive)
  (local-set-key [C-return] 'my-python-send-block)
  (set-mark (line-end-position))
                                        ; (previous-line)
  (let ((lines-of-block 0))
    (while (or (equal (line-beginning-position) 0) (not (line-emptyp)))
      (previous-line)
      (beginning-of-line)
      (set 'lines-of-block (+ 1 lines-of-block)))
    (beginning-of-line)
    (call-interactively 'python-shell-send-region)
    (python-shell-send-string "\n")
    (dotimes (i lines-of-block)
      (next-line))
    (end-of-line)))

(add-hook 'python-mode-hook
          (lambda ()
            (local-set-key [M-return] 'my-python-test-buffer)
            (local-set-key [S-return] 'my-python-send-paragraph)
            ;; S, C, M-return don't seem to work
            (local-set-key (kbd "<f2>") 'my-python-send-buffer)))