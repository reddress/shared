(when (>= emacs-major-version 24)
  (require 'package)
  (add-to-list
   'package-archives
   '("melpa" . "http://melpa.org/packages/")
   t)
  (package-initialize))

(setq inhibit-startup-screen t)

;; Custom
(custom-set-variables
 '(ansi-color-names-vector ["black" "red" "green" "yellow" "blue" "magenta" "cyan" "white"])
 '(js-indent-level 2)
 '(c-basic-offset 4)
 '(c-default-style "linux")
 '(column-number-mode t)
 '(default-tab-width 4 t)
 '(fill-column 79)
 '(global-visual-line-mode nil)
 '(indent-tabs-mode nil)
 '(ispell-personal-dictionary (expand-file-name "~/.aspell"))
 '(iswitchb-mode t)
 '(scroll-conservatively 100)
 '(scroll-preserve-screen-position t)
 '(scroll-step 1)
 '(tool-bar-mode nil)
 '(yas/prompt-functions (quote (yas/ido-prompt yas/x-prompt yas/completing-prompt yas/no-prompt))))

(custom-set-faces
 '(default ((t (:inherit nil :stipple nil :background "white" :foreground "black" :inverse-video nil :box nil :strike-through nil :overline nil :underline nil :slant normal :weight normal :height 120 :width normal :foundry "outline" :family "ProggyTinyTTSZ")))))


;;; Greek font
(set-fontset-font "fontset-default" '(#x0370 . #x03ff)
                  "-bitstream-bitstream charter-medium-r-normal--17-120-100-100-p-0-iso10646-1")

;; MELPA
(when (>= emacs-major-version 24)
  (require 'package)
  (package-initialize)
  (add-to-list 'package-archives '("melpa" . "http://melpa.milkbox.net/packages/") t))

;; globals
(setq-default frame-title-format
              '((:eval (if (buffer-file-name)
                           (abbreviate-file-name (buffer-file-name))
                         "%b"))))

(add-to-list 'load-path "/home/heitor/.emacs.d/lisp")
(add-to-list 'load-path "/home/heitor/.emacs.d/auto-complete")
(add-to-list 'load-path "/home/heitor/.emacs.d/s")
(add-to-list 'load-path "/home/heitor/.emacs.d/virtualenvwrapper")

;; (add-to-list 'load-path "c:/Users/Heitor/Desktop/emacs-24.3/site-lisp/js-comint")
(set-language-environment "UTF-8")

(setq default-input-method "latin-1-postfix")

(require 'julia-mode)

(require 'web-mode)
(add-to-list 'auto-mode-alist '("\\.html?\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.php\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.[agj]sp\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.as[cp]x\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.erb\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.mustache\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.djhtml\\'" . web-mode))

(defun my-previous-window ()
  (interactive)
  (other-window -1))

(defun my-indent-whole-buffer ()
  (interactive)
  (save-excursion
    (mark-whole-buffer)
    (call-interactively 'indent-region)))

(defun my-insert-console-log ()
  (interactive)
  (insert "console.log("))

;; (global-set-key (kbd "<S-backspace>") 'move-beginning-of-line)

;; copy and paste
;; M-w saves region
(global-set-key (kbd "M-e") 'yank)

(global-set-key (kbd "M-u") 'undo)

(global-set-key (kbd "C-x p") 'my-previous-window)
(global-set-key (kbd "C-<") 'previous-buffer)
(global-set-key (kbd "C->") 'next-buffer)

(global-set-key (kbd "C-'") 'iswitchb-buffer)

(global-set-key (kbd "<f3>") 'isearch-forward)
(define-key isearch-mode-map (kbd "<f3>") 'isearch-repeat-forward)
(global-set-key (kbd "<f5>") 'run-python)
(global-set-key (kbd "<f6>") 'eval-print-last-sexp)
(global-set-key (kbd "<f7>") 'make-directory)
(global-set-key (kbd "<f8>") 'kill-this-buffer)
(global-set-key (kbd "<f9>") 'find-file)
(global-set-key (kbd "<f10>") 'save-buffer)
(global-set-key (kbd "<f11>") 'write-file)
(global-set-key (kbd "<f12>") 'split-window-below)
(global-set-key (kbd "S-<f12>") 'split-window-right)

(global-set-key (kbd "<M-up>") 'other-window)
(global-set-key (kbd "<M-down>") 'other-window)

(global-set-key (kbd "C-c j") 'javascript-mode)
(global-set-key (kbd "C-c h") 'html-mode)

(global-set-key (kbd "C-c C-e") 'electric-indent-mode)

(global-set-key (kbd "C-c i") 'my-indent-whole-buffer)
(global-set-key (kbd "C-c l") 'my-insert-console-log)

(global-unset-key (kbd "C-t"))

;;; languages
(global-set-key (kbd "C-c 0") (lambda () (interactive) (set-input-method 'british)))

(global-set-key (kbd "C-c o") 'my-input-greek)
(global-set-key (kbd "C-c g") 'my-input-greek)
(global-set-key (kbd "C-c p") 'my-input-portuguese)

(defun my-input-greek ()
  (interactive)
  (set-input-method 'greek))

(defun my-input-portuguese ()
  (interactive)
  (set-input-method 'portuguese-prefix))

;;; (global-set-key [C-return] 'my-isend-send-buffer)
                                        ;(color-theme-emacs-nw)
(setq backup-inhibited t)
(delete-selection-mode t)
(menu-bar-mode -1)

;; cursor
(blink-cursor-mode -1)
(set-default 'cursor-type 'bar)
(set-cursor-color "#338833")

;; force regular font
(defun disable-bold ()
  (interactive)
  (mapc (lambda (face) (set-face-attribute face nil :weight 'normal :underline nil)) (face-list)))
(call-interactively 'disable-bold)

;;; (electric-indent-mode t)
(electric-indent-mode 0)

;; window position
;; (setq initial-frame-alist '((top . 0) (left . 0) (width . 77) (height . 63)))
(setq initial-frame-alist '((top . 0) (left . 0) (width . 76) (height . 63)))

;; custom functions
;; general
(defun kill-all-buffers ()
  (interactive)
  (mapc 'kill-buffer (buffer-list)))

(defun restore-parens ()
  (interactive)
  (keyboard-translate ?\[ ?\[)
  (keyboard-translate ?\] ?\])
  (keyboard-translate ?\{ ?\{)
  (keyboard-translate ?\} ?\})
  (keyboard-translate ?\( ?\()
  (keyboard-translate ?\) ?\)))

(defun convert-parens ()
  (interactive)
  (keyboard-translate ?\[ ?\()
  (keyboard-translate ?\] ?\))
  (keyboard-translate ?\{ ?\()
  (keyboard-translate ?\} ?\))
  (keyboard-translate ?\( ?\()
  (keyboard-translate ?\) ?\)))

(defun add-letters (letters)
  (interactive "sEnter letters:")
  (move-end-of-line nil)
  (newline-and-indent)
  (previous-line)
  (move-beginning-of-line nil)
  (kill-line 1)
  (let ((letterlist (string-to-list letters)))
    (dolist (element letterlist)
      (yank)
      (left-char 1)
      (insert (char-to-string element))
      (next-line)))
  (delete-forward-char 1))

(defun add-nums-in-brackets ()
  "add all values stored inside [brackets], first only per line"
  (interactive)
  (setq total 0)
  (save-excursion
    (end-of-buffer)
    (beginning-of-line)
    (setq num-lines (count-lines 1 (point)))
    (dotimes (j (+ 1 num-lines))
      (beginning-of-line)
      (setq curline (thing-at-point 'line))
      (message curline)
      (when (string-match "\\[\\([0-9]+\\)\\]" curline)
        (setq total (+ total (string-to-number (match-string 1 curline)))))
      (when (< j num-lines)
        (previous-line)))
    (end-of-buffer))
  (message "total %s" total))

;; Lisp
(defun hide-eol ()
  (interactive)
  (setq buffer-display-table (make-display-table))
  (aset buffer-display-table ?\^M []))

;; Clozure
;; (setq inferior-lisp-program "/home/heitor/Downloads/ccl/lx86cl")

;; CLISP
(setq inferior-lisp-program "clisp -p HC")

;; SBCL
;; (setq inferior-lisp-program "sbcl")

;; Allegro
;; (setq inferior-lisp-program "/home/heitor/Downloads/acl100express/alisp")

(defun my-lisp-send-buffer ()
  (interactive)
  (save-excursion
    (mark-whole-buffer)
    (call-interactively 'lisp-eval-region)
    (deactivate-mark)
    (end-of-buffer)))

(defun my-lisp-send-paragraph ()
  (interactive)
  (save-excursion
    (mark-paragraph)
    (call-interactively 'lisp-eval-region)))

;;; http://emacs.stackexchange.com/questions/777/closing-all-pending-parenthesis
;;; (defun close-all-parentheses ()
;;; BROKEN IN UBUNTU EMACS 24.5


;; Scheme
;; (setq scheme-program-name "petite") ;; Petite Chez
;; (setq scheme-program-name "csi") ;; Chicken
;; (setq scheme-program-name "guile") ;; Guile
(setq scheme-program-name "mit-scheme") ;; MIT-Scheme
;; (setq scheme-program-name "\"C:/Program Files/MIT-GNU Scheme/bin/mit-scheme.exe\" --library \"C:/Program Files/MIT-GNU Scheme/lib\" --emacs")

(defun my-scheme-send-buffer ()
  (interactive)
  (mark-whole-buffer)
  (call-interactively 'scheme-send-region)
  (deactivate-mark)
  (end-of-buffer))

;; Python
;; (setq python-shell-interpreter "python3")
(setq python-shell-interpreter "/usr/bin/python3")
;;(setq python-shell-interpreter "C:/Python27/python.exe")

(setenv "PYTHONUNBUFFERED" "x")

(defun line-emptyp ()
  (= (line-beginning-position) (line-end-position)))

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

(defun my-js-send-block ()
  (interactive)
  (set-mark (line-end-position))
                                        ; (previous-line)
  (let ((lines-of-block 0))
    (while (or (equal (line-beginning-position) 0) (not (line-emptyp)))
      (previous-line)
      (beginning-of-line)
      (set 'lines-of-block (+ 1 lines-of-block)))
    (beginning-of-line)
    (call-interactively 'js-send-region)
    (dotimes (i lines-of-block)
      (next-line))
    (end-of-line)))

(defun my-js-send-line ()
  (interactive)
  (set-mark (line-end-position))
  (beginning-of-line)
  (call-interactively 'js-send-region)
  (end-of-line))

;; (js-send-last-sexp))

;; (defun node-suppress-undefined ()
;;  (interactive)
;;  (comint-send-string inferior-js-buffer "module.exports.repl.ignoreUndefined = true;"))

;; auto-complete-mode
(require 'auto-complete-config)
;; (add-to-list 'ac-dictionary-directories "c:/Users/Heitor/Desktop/LispCabinetHome/.emacs.d/dict")
;; (setq-default ac-sources (add-to-list 'ac-sources 'ac-source-dictionary))

(global-auto-complete-mode t)
(setq ac-ignore-case nil)
(define-key ac-completing-map "\r" nil)  ; remove completion with RET
(setq ac-auto-start 1)
;; prevent pop-up on arrow keys
(define-key ac-completing-map (kbd "<down>") nil)
(define-key ac-completing-map (kbd "<up>") nil)
(setq ac-delay 0.0001)
(setq ac-disable-faces nil)
(setq ac-auto-show-menu 0.0001)

;; settings for not immediately completing
                                        ;(global-auto-complete-mode t)
                                        ;(setq ac-auto-start 2)
                                        ;(setq ac-ignore-case nil)
                                        ;(setq ac-delay 1)
                                        ;(ac-set-trigger-key "TAB")

;; isend-mode
(add-to-list 'load-path "/home/heitor/.emacs.d/isend-mode/")
(require 'isend)

;;; Note: commented out line :keymap '(([C-return ...
;;; because it could not be overridden

;;(defun my-isend-send-line ()
;;  (interactive)
;;  (set-mark (line-end-position))
;;  (beginning-of-line)
;;  (call-interactively 'isend-send)
;;  (end-of-line))

(defun my-isend-send-block ()
  (interactive)
  (set-mark (line-end-position))

  (save-excursion
    (let ((lines-of-block 0))
      (while (or (equal (line-beginning-position) 0) (not (line-emptyp)))
        (previous-line)
        (beginning-of-line)
        (set 'lines-of-block (+ 1 lines-of-block)))
      (beginning-of-line)
      (call-interactively 'isend-send)
      ;;(dotimes (i lines-of-block)
      ;;  (next-line))
      (end-of-line))))

(defun my-isend-send-paragraph ()
  (interactive)
  (save-excursion
    (mark-paragraph)
    (call-interactively 'isend-send)))

(defun my-isend-send-sexp ()
  (interactive)
  (save-excursion
    (backward-sexp)
    (mark-sexp)
    (call-interactively 'isend-send)))

(defun my-isend-send-buffer ()
  (interactive)
  (save-excursion
    (mark-whole-buffer)
    (call-interactively 'isend-send)
    (end-of-buffer)))

;;; set keys
(global-set-key (kbd "RET") 'newline-and-indent)

;;; custom functions
;;; (global-set-key "\M-n" 'add-letters)
;;; (global-set-key "\M-p" 'add-nums-in-brackets)
;;; (global-set-key (kbd "M-)") 'close-all-parentheses)

;; racket
(add-to-list 'auto-mode-alist '("\\.rkt\\'" . scheme-mode))

;;; (add-hook 'scheme-mode-hook
;;;          (lambda ()
;; (call-interactively 'auto-complete-mode)
;;;            (auto-complete-mode 1)
;;;            (isend-associate "*shell*")))

(add-hook 'web-mode-hook
          (lambda ()
            (setq web-mode-enable-auto-quoting nil)
            (setq web-mode-enable-auto-pairing nil)
            (setq web-mode-markup-indent-offset 4)
            (setq web-mode-code-indent-offset 4)
            (call-interactively 'auto-complete-mode)))

(add-hook 'lisp-mode-hook
          (lambda ()
            ;; (local-set-key [tab] 'slime-indent-and-complete-symbol)
            ;; (local-set-key [return] 'newline-and-indent)))
            (call-interactively 'auto-complete-mode)
            (set (make-local-variable lisp-indent-function)
                 'common-lisp-indent-function)
            ;; (local-set-key (kbd "C-]") 'close-all-parentheses)

            ;; (call-interactively 'convert-parens)
            
            ;;; (local-set-key [C-up] 'backward-up-list)
            ;;; (local-set-key [C-down] 'down-list)
            (local-set-key [M-left] 'backward-sexp)
            (local-set-key [M-right] 'forward-sexp)

            (local-set-key (kbd "M-k") 'kill-sexp)
            
            (local-set-key [S-return] 'lisp-eval-last-sexp)
            (local-set-key [M-return] 'my-lisp-send-paragraph)            
            (local-set-key [C-return] 'my-lisp-send-buffer)))

(add-hook 'clojure-mode-hook
          (lambda ()
            (isend-associate "*shell*")
            
            (local-set-key [M-left] 'backward-sexp)
            (local-set-key [M-right] 'forward-sexp)

            (local-set-key (kbd "M-k") 'kill-sexp)

            (local-set-key [S-return] 'my-isend-send-sexp)
            (local-set-key [M-return] 'my-isend-send-paragraph)
            (local-set-key [C-return] 'my-isend-send-buffer)))

(add-hook 'scheme-mode-hook
          (lambda ()

            ;; (keyboard-translate ?\[ ?\()
            ;; (keyboard-translate ?\] ?\))

            ;; (keyboard-translate ?\( ?\[)
            ;; (keyboard-translate ?\) ?\])
            ;; (keyboard-translate ?\{ ?\()
            ;; (keyboard-translate ?\} ?\))

            (local-set-key [C-return] 'my-scheme-send-buffer)
            (local-set-key [M-return] 'my-scheme-send-buffer)
            (local-set-key [S-return] 'scheme-send-last-sexp)))

(add-hook 'emacs-lisp-mode-hook
          (lambda ()
            (auto-complete-mode 1)

            (local-set-key (kbd "M-k") 'kill-sexp)
            (local-set-key [C-return] 'eval-buffer)
            (local-set-key [S-return] 'eval-last-sexp)))

(add-hook 'python-mode-hook
          (lambda ()
            (local-set-key [C-return] 'my-python-test-buffer)
            (local-set-key [S-return] 'my-python-send-paragraph)
            (local-set-key [M-return] 'my-python-send-buffer)))

(add-hook 'js-mode-hook
          (lambda ()
            (local-set-key (kbd "C-c n") 'node-suppress-undefined)
            (local-set-key (kbd "C-c c") 'js-send-buffer)
            (local-set-key [S-return] 'my-js-send-line)
            (local-set-key [C-return] 'my-js-send-block)
            (call-interactively 'node-suppress-undefined)))
;; ))

(add-hook 'sql-mode-hook
          (lambda ()
            (call-interactively 'auto-complete-mode)))

(add-hook 'fundamental-mode-hook
          (lambda ()
            ;;(call-interactively 'auto-complete-mode)))
            (auto-complete-mode 1)))


(add-hook 'isend-mode-hook
          (lambda ()
            ;;(local-set-key [S-return] 'my-isend-send-line)
            (local-set-key [S-return] 'my-isend-send-paragraph)
            (local-set-key [C-return] 'my-isend-send-buffer)
            (local-set-key [M-return] 'my-isend-send-buffer)))

(add-hook 'julia-mode-hook
          (lambda ()
            (auto-complete-mode 1)
            (isend-associate "*shell*")))

(add-hook 'inferior-scheme-mode-hook
          (lambda ()
            (auto-complete-mode 1)))

(add-hook 'inferior-lisp-mode-hook
          (lambda ()
            ;; (call-interactively 'convert-parens)
            (auto-complete-mode 1)))

(add-hook 'inferior-python-mode-hook
          (lambda ()
            (auto-complete-mode 1)))

;; change mode for Kivy files
(add-to-list 'auto-mode-alist '("\\.kv\\'" . text-mode))

;; change mode for TypeScript files
(add-to-list 'auto-mode-alist '("\\.ts\\'" . js-mode))

;; change mode for PHP files
;;; (add-to-list 'auto-mode-alist '("\\.php\\'" . java-mode))

;; text mode
(defun my-text-tabify ()
  (interactive)
  (save-excursion
    (mark-whole-buffer)
    (call-interactively 'tabify)
    (end-of-buffer))
  (newline))

(add-hook 'text-mode-hook
          (lambda ()
            (setq indent-tabs-mode nil)
            ;; (local-set-key [return] 'my-text-tabify)
            ;; (call-interactively 'auto-complete-mode)))
            (auto-complete-mode 1)))
(define-key text-mode-map (kbd "TAB") 'self-insert-command)
(define-key text-mode-map [backtab] 'indent-for-tab-command)
(put 'upcase-region 'disabled nil)

(defun datetime ()
  (interactive)
  (insert (current-time-string)))


;;;; New generation of custom functions

(defun cut-line ()
  (interactive)
  (beginning-of-line)
  (kill-line))

(defun copy-line ()
  (interactive)
  (beginning-of-line)
  (kill-line)
  (yank))

(global-set-key (kbd "C-x x") 'copy-line)

;;;; Python
;; http://stackoverflow.com/questions/243060/how-to-set-the-pythonpath-in-emacs
(setenv "PYTHONPATH" "/home/heitor/shared/python/my-modules/")

(setenv "PYTHONSTARTUP" "/home/heitor/shared/python/my-startup.py")

;;; https://www.emacswiki.org/emacs/IswitchBuffers
;; (require 'edmacro)
(defun iswitchb-local-keys ()
  (mapc (lambda (K) 
	      (let* ((key (car K)) (fun (cdr K)))
            (define-key iswitchb-mode-map (edmacro-parse-keys key) fun)))
	    '(("<right>" . iswitchb-next-match)
	      ("<left>"  . iswitchb-prev-match)
	      ("<up>"    . ignore             )
	      ("<down>"  . ignore             ))))
(add-hook 'iswitchb-define-mode-map-hook 'iswitchb-local-keys)

;;; Quail Gwoyeu Romatzyh
(add-to-list 'load-path "/home/heitor/chinese/gwoyeu-romatzyh-studies/")
(require 'gwoyeu-romatzyh-input)


(require 'package)
(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/"))

;; virtualenvwrapper
(require 'virtualenvwrapper)
(setq venv-location "/home/heitor/envs/")

;; escape html
;; http://shallowsky.com/blog/linux/editors/emacs-escape-html.html

(defun escape-html (start end)
  (interactive "r")
  (save-excursion
    (save-restriction
      (narrow-to-region start end)
      (goto-char (point-min))
      (replace-string "&" "&amp;")
      (goto-char (point-min))
      (replace-string "<" "&lt;")
      (goto-char (point-min))
      (replace-string ">" "&gt;"))))

(setq truncate-partial-width-windows nil)
