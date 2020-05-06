;;; mysend-mode adds send-region to isend-mode.el

;;; mysend-mode.el --- Interactively send parts of an Emacs buffer to an interpreter

;; Copyright (C) 2012 François Févotte
;; Author:  François Févotte <fevotte@gmail.com>
;; URL:     https://github.com/ffevotte/mysend-mode.el
;; Version: 0.2

;; This file is NOT part of Emacs.

;; This program is free software: you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation, either version 3 of the License, or
;; (at your option) any later version.

;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.

;; You should have received a copy of the GNU General Public License
;; along with this program.  If not, see <http://www.gnu.org/licenses/>.


;;; Commentary:

;; `mysend-mode' is an Emacs extension allowing interaction with code
;; interpreters in `ansi-term' or `term' buffers. Some language-specific
;; modes (e.g. `python-mode') already provide similar features; `mysend-mode'
;; does the same in a language-agnostic way.


;; Basic usage:

;; 1. Open an `ansi-term' buffer where the interpreter will live.
;;    For example:
;;
;;      M-x ansi-term RET /bin/sh RET

;; 2. Open a buffer with the code you want to execute, and associate it
;;    to the interpreter buffer using the `mysend-associate' command (also
;;    aliased to `mysend'). For example:
;;
;;      M-x mysend-associate RET *ansi-term* RET

;; 3. Press C-RET (or M-x `mysend-send') to send the current line to the
;;    interpreter. If the region is active, all lines spanned by the region
;;    will be sent (i.e. no line will be only partially sent). Point is
;;    then moved to the next non-empty line (but see configuration variable
;;    `mysend-skip-empty-lines').


;; Contributing:

;; If you make improvements to this code or have suggestions, please do not
;; hesitate to fork the repository or submit bug reports on github. The
;; repository is at:
;;
;;     https://github.com/ffevotte/mysend-mode.el

;;; Code:

;; Get rid of warning about `term-send-input' not being defined.
(require 'term)

;; if-let
(require 'subr-x)



;; Customization variables

;;;###autoload
(defgroup mysend nil
  "Interactively send parts of an Emacs buffer to an interpreter."
  :group 'processes)

;;;###autoload
(defcustom mysend-forward-line t
  "If non-nil, `mysend-send' advances by one line after sending content."
  :group 'mysend
  :type  'boolean)

;;;###autoload
(defcustom mysend-skip-empty-lines t
  "If non-nil, `mysend-send' skips empty lines (i.e. lines containing only spaces).

Note that this is effective only for sending single lines. To strip whitespace
from sent regions use `mysend-strip-empty-lines'."
  :group 'mysend
  :type  'boolean)

;;;###autoload
(defcustom mysend-strip-empty-lines nil
  "If non-nil, `mysend-send' strips empty lines (i.e. lines containing only spaces).

Note that this works when sending an entire region. If enabled, all lines containing
whitespace only will be stripped from the region before it is sent."
  :group 'mysend
  :type  'boolean)

;;;###autoload
(defcustom mysend-delete-indentation nil
  "If non-nil, `mysend-send' deletes indentation in regions sent.

Note that this only works when sending a region (as opposed to a
single line). Relative indentation with respect to the first line
in the region is preserved.

This is useful to send e.g. Python blocks.")

;;;###autoload
(defcustom mysend-end-with-empty-line nil
  "If non-nil, `mysend-send' appends an empty line to everything you send.

This is useful, for example, when working with python code,
in which whitespace terminates definitions."
  :group 'mysend
  :type  'boolean)

;;;###autoload
(defcustom mysend-bracketed-paste nil
  "If non-nil, `mysend-send' will use \"bracketed paste\".

Bracketed paste surrounds the contents it sends with escape
sequences indicating to the underlying process that this content
is being pasted."
  :group 'mysend
  :type  'boolean)

;;;###autoload
(defcustom mysend-send-line-function nil
  "Function used by `mysend-send' to send a single line.

This function is called in a buffer containing the text to be
sent. It can modify it as needed before it is sent to the
process. It also receives as argument the destination buffer, in
case some interaction with it would be useful.

Possible values include:
- nil (default)
- `mysend--ipython-cpaste'
- `mysend--ipython-paste'"
  :group 'mysend
  :type  'function)

;;;###autoload
(defcustom mysend-send-region-function nil
  "Function used by `mysend-send' to send a region.

This function is called in a buffer containing the text to be
sent. It can modify it as needed before it is sent to the
process.  It also receives as argument the destination buffer,
in case some interaction with it would be useful.

Possible values include:
- nil (default)
- `mysend--ipython-cpaste'
- `mysend--ipython-paste'"
  :group 'mysend)

;;;###autoload
(defcustom mysend-mark-defun-function 'mark-defun
  "Function used by `mysend-defun' to select a function definition.

This function should take no argument.

Possible values include:
- `mark-defun' (default)
- `mysend--python-mark-defun'"
  :group 'mysend)



;; Setup helpers

;; Put something like this in your init file to use:
;;
;;   (add-hook 'mysend-mode-hook 'mysend-default-shell-setup)

;;;###autoload
(defun mysend-default-shell-setup ()
  (when (eq major-mode 'sh-mode)
    (set (make-local-variable 'mysend-skip-empty-lines)     t)
    (set (make-local-variable 'mysend-strip-empty-lines)    nil)
    (set (make-local-variable 'mysend-delete-indentation)   nil)
    (set (make-local-variable 'mysend-end-with-empty-line)  nil)
    (set (make-local-variable 'mysend-bracketed-paste)      nil)
    (set (make-local-variable 'mysend-send-line-function)   nil)
    (set (make-local-variable 'mysend-send-region-function) nil)
    (set (make-local-variable 'mysend-mark-defun-function)  #'mark-defun)))

;;;###autoload
(defun mysend-default-python-setup ()
  (when (eq major-mode 'python-mode)
    (set (make-local-variable 'mysend-skip-empty-lines)     nil)
    (set (make-local-variable 'mysend-strip-empty-lines)    t)
    (set (make-local-variable 'mysend-delete-indentation)   t)
    (set (make-local-variable 'mysend-end-with-empty-line)  t)
    (set (make-local-variable 'mysend-bracketed-paste)      t)
    (set (make-local-variable 'mysend-send-line-function)   nil)
    (set (make-local-variable 'mysend-send-region-function) nil)
    (set (make-local-variable 'mysend-mark-defun-function)  #'mysend--python-mark-defun)))

;;;###autoload
(defun mysend-default-ipython-setup ()
  (when (eq major-mode 'python-mode)
    (set (make-local-variable 'mysend-skip-empty-lines)     nil)
    (set (make-local-variable 'mysend-strip-empty-lines)    nil)
    (set (make-local-variable 'mysend-delete-indentation)   nil)
    (set (make-local-variable 'mysend-end-with-empty-line)  nil)
    (set (make-local-variable 'mysend-bracketed-paste)      nil)
    (set (make-local-variable 'mysend-send-line-function)   nil)
    (set (make-local-variable 'mysend-send-region-function) #'mysend--ipython-paste)
    (set (make-local-variable 'mysend-mark-defun-function)  #'mysend--python-mark-defun)))

;;;###autoload
(defun mysend-default-clojure-setup ()
  (when (eq major-mode 'clojure-mode)
    (set (make-local-variable 'mysend-skip-empty-lines)     nil)
    (set (make-local-variable 'mysend-strip-empty-lines)    nil)
    (set (make-local-variable 'mysend-delete-indentation)   nil)
    (set (make-local-variable 'mysend-end-with-empty-line)  nil)
    (set (make-local-variable 'mysend-bracketed-paste)      nil)
    (set (make-local-variable 'mysend-send-line-function)   nil)
    (set (make-local-variable 'mysend-send-region-function) #'mysend--clojure-send-region)
    (set (make-local-variable 'mysend-mark-defun-function)  #'mysend--clojure-mark-defun)))

;;;###autoload
(defun mysend-default-julia-setup ()
  (when (eq major-mode 'julia-mode)
    (set (make-local-variable 'mysend-skip-empty-lines)     t)
    (set (make-local-variable 'mysend-strip-empty-lines)    nil)
    (set (make-local-variable 'mysend-delete-indentation)   nil)
    (set (make-local-variable 'mysend-end-with-empty-line)  nil)
    (set (make-local-variable 'mysend-bracketed-paste)      t)
    (set (make-local-variable 'mysend-send-line-function)   nil)
    (set (make-local-variable 'mysend-send-region-function) nil)
    (set (make-local-variable 'mysend-mark-defun-function)  #'mark-defun)))



;; User interface

(define-minor-mode mysend-mode
  "Toggle Mysend (Interactive Send) mode\\<mysend-mode-map>.
With ARG, turn Mysend mode on if ARG is positive, otherwise
turn it off.

This mode allows sending commands from a regular buffer to an
interpreter in a terminal buffer (such as `ansi-term' or
`eshell')

Note that you should NOT manually activate this mode. You should
use `mysend-associate' instead.

When Mysend mode is enabled and a destination buffer has been
defined using `mysend-associate', you can send lines or regions to
the associated buffer using \\[mysend-send] (or `mysend-send').


\\{mysend-mode-map}"
  :init-value nil
  :lighter    " Mysend"
  :keymap     '(([C-return] . mysend-send)))

(defvar mysend--command-buffer)
(make-variable-buffer-local 'mysend--command-buffer)

;;;###autoload
(defun mysend-associate (buffername)
 "Set the buffer to which commands will be sent using `mysend-send'.
This should usually be something like '*ansi-term*' or '*terminal*'."
 (interactive "bAssociate buffer to terminal: ")
 (setq mysend--command-buffer buffername)
 (mysend-mode 1))

;;;###autoload
(defalias 'mysend 'mysend-associate)



(defun mysend-send ()
  "Send the current line to a terminal.
Use `mysend-associate' to set the associated terminal buffer. If
the region is active, all lines spanned by it are sent."
  (interactive)
  (mysend--check)

  (let* ((region-active (region-active-p))

         ;; The region to be sent
         (bds   (mysend--region-boundaries))
         (begin (car bds))
         (end   (cdr bds))

         ;; Configuration variables values need to be taken from
         ;; the origin buffer (they are potentially local)
         (mysend-strip-empty-lines-1    mysend-strip-empty-lines)
         (mysend-delete-indentation-1   mysend-delete-indentation)
         (mysend-end-with-empty-line-1  mysend-end-with-empty-line)
         (mysend-send-region-function-1 mysend-send-region-function)
         (mysend-send-line-function-1   mysend-send-line-function)
         (mysend-bracketed-paste-1      mysend-bracketed-paste)

         ;; Buffers involved
         (origin (current-buffer))
         (destination (get-buffer mysend--command-buffer)))

    ;; A temporary buffer is used to apply filters
    (with-temp-buffer
      (insert-buffer-substring origin begin end)

      ;; Phase 1 - Apply filters on the region
      (when region-active
        (when mysend-strip-empty-lines-1
          (delete-matching-lines "^[[:space:]]*$" (point-min) (point-max)))

        (when mysend-delete-indentation-1
          (goto-char (point-min))
          (back-to-indentation)
          (indent-rigidly (point-min) (point-max) (- (current-column))))

        (when mysend-end-with-empty-line-1
          (goto-char (point-max))
          (insert "\n")))

      (if region-active
          (and mysend-send-region-function-1
               (funcall mysend-send-region-function-1 destination))
        (and mysend-send-line-function-1
             (funcall mysend-send-line-function-1 destination)))

      (when mysend-bracketed-paste-1
        (goto-char (point-min)) (insert "\e[200~")
        (goto-char (point-max)) (insert "\e[201~"))

      ;; Phase 2 - Actually send the region to the associated buffer
      (let ((filtered (current-buffer)))
        (with-current-buffer destination
          ;; Move to the process mark if there is one
          (if-let ((process (get-buffer-process (current-buffer))))
              (goto-char (process-mark process)))

          ;; Insert the contents
          (let ((inhibit-read-only t))
            (insert-buffer-substring filtered))

          (cond
           ;; Terminal buffer: specifically call `term-send-input'
           ;; to handle both the char and line modes of `ansi-term'.
           ((eq major-mode 'term-mode)
            (term-send-input))

           ;; Other buffer: call whatever is bound to 'RET'
           (t
            (funcall (key-binding (kbd "RET")))))))))

  (deactivate-mark)

  ;; Move point to the next line
  (when mysend-forward-line
    (mysend--next-line)))


(defun mysend-send-buffer ()
  (interactive)
  (save-excursion
    (mark-whole-buffer)
    (mysend-send)))


(defun mysend-send-defun ()
  (interactive)
  (save-excursion
    (funcall mysend-mark-defun-function)
    (mysend-send)))


(defun mysend-display-buffer ()
  (interactive)
  (mysend--check)
  (display-buffer mysend--command-buffer))


;; Helper functions

(defun mysend--check ()
  "Check whether the current buffer has been associated to a terminal."
  (when (not (boundp 'mysend--command-buffer))
    (error "No associated terminal buffer. You should run `mysend-associate'")))

(defun mysend--region-seed ()
  "Return a 'seed' of the region to be sent.
The result is a cons cell of the form (beg . end)"
  (cond
   ;; If the region is active, use region boundaries
   ((use-region-p)
    (cons (region-beginning)
          (- (region-end) 1)))

   ;; If the region is not active and `mysend-skip-empty-lines' is non-nil,
   ;; move forward to the first non-empty line.
   (mysend-skip-empty-lines
    (skip-chars-forward "[:space:]\n")
    (cons (point)
          (point)))

   ;; Otherwise, use current point
   (t
    (cons (point)
          (point)))))

(defun mysend--region-boundaries ()
  "Return the boundaries of the region to be sent.
The result is a cons cell of the form (beg . end)
The region is expanded so that no line is only partially sent."
  (let* ((bds (mysend--region-seed))
         (beg (car bds))
         (end (cdr bds)))

    ;; Expand the region to span whole lines
    (goto-char beg)
    (setq beg (line-beginning-position))
    (goto-char end)
    (setq end (line-end-position))
    (when (= beg (point-max))
      (error "Nothing more to send!"))
    (cons beg end)))

(defun mysend--next-line ()
  "Move point to the next line.
Empty lines are skipped if `mysend-skip-empty-lines' is non-nil."
  (goto-char (line-end-position))
  (if mysend-skip-empty-lines
      (when (> (skip-chars-forward "[:space:]\n") 0)
        (goto-char (line-beginning-position)))
    (beginning-of-line 2)))

(defun mysend--ipython-cpaste (destination)
  ""
  (term-send-string (get-buffer-process destination) "%cpaste\n")
  (with-current-buffer destination (term-send-input))
  (sleep-for 0.1)
  (goto-char (point-max)) (insert "\n--"))

(defun mysend--ipython-paste (destination)
  ""
  (clipboard-kill-ring-save (point-min) (point-max))
  (erase-buffer)(insert "%paste"))

(defun mysend--clojure-send-region (destination)
  ""
  (clipboard-kill-ring-save (point-min) (point-max))
  (erase-buffer)(insert "%paste"))

(defun mysend--python-mark-defun ()
  "Mark the current top-level python block.

A block is defined as in `python-nav-beginning-of-block' and
`python-nav-end-of-block'. A top-level block begins without
indentation."
  (let ((loop t))
    (while loop
      (unless (python-nav-beginning-of-block)
        (error "Not in a python block"))
      (if (bolp)
          (setq loop nil)
        (forward-line -1))))
  (push-mark (point))
  (python-nav-end-of-block)
  (exchange-point-and-mark))

(provide 'mysend-mode)

;;; mysend-mode.el ends here
