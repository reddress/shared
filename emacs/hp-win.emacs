;; dot emacs
;; location: c:/Users/Tok/AppData/Roaming/

;; window position

;; for large fonts
;; (setq initial-frame-alist '((top . 0) (left . 0) (width . 79) (height . 38)))

;; for Proggy Font
(setq initial-frame-alist '((top . 10) (left . 40) (width . 90) (height . 68)))

(setq inhibit-startup-message t)
(setq backup-inhibited t)
(setq auto-save-default nil)
(setq make-backup-files nil)
(setq create-lockfiles nil)
(setq ring-bell-function 'ignore)
(set-language-environment "UTF-8")
(setq-default frame-title-format "%f")
(delete-selection-mode t)
(menu-bar-mode -1)

(setq default-directory "C:/Users/heitor/Desktop/code/")
(setenv "HOME" "c:/Users/heitor/")

(setq default-input-method "portuguese-prefix")

(require 'package)
(let* ((no-ssl (and (memq system-type '(windows-nt ms-dos))
                    (not (gnutls-available-p))))
       (proto (if no-ssl "http" "https")))
  (when no-ssl
    (warn "\
Your version of Emacs does not support SSL connections,
which is unsafe because it allows man-in-the-middle attacks.
There are two things you can do about this warning:
1. Install an Emacs version that does support SSL and be safe.
2. Remove this warning from your init file so you won't see it again."))
  ;; Comment/uncomment these two lines to enable/disable MELPA and MELPA Stable as desired
  (add-to-list 'package-archives (cons "melpa" (concat proto "://melpa.org/packages/")) t)
  (add-to-list 'package-archives (cons "melpa-stable" (concat proto "://stable.melpa.org/packages/")) t)
  (when (< emacs-major-version 24)
    ;; For important compatibility libraries like cl-lib
    (add-to-list 'package-archives (cons "gnu" (concat proto "://elpa.gnu.org/packages/")))))

(package-initialize)

(defun trim-string (string)
  "Remove white spaces in beginning and ending of STRING.
White space here is any of: space, tab, emacs newline (line feed, ASCII 10)."
  (replace-regexp-in-string "\\`[ \t\n]*" "" (replace-regexp-in-string "[ \t\n]*\\'" "" string)))


;; Custom

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-names-vector
   ["black" "red" "green" "yellow" "blue" "magenta" "cyan" "white"])
 '(c-basic-offset 4)
 '(c-default-style "linux")
 '(column-number-mode t)
 '(custom-enabled-themes (quote (tango)))
 '(default-tab-width 2 t)
 '(fill-column 72)
 '(global-visual-line-mode nil)
 '(indent-tabs-mode nil)
 '(ispell-personal-dictionary (expand-file-name "~/.aspell"))
 '(iswitchb-mode t)
 '(js-indent-level 2)
 '(package-selected-packages
   (quote
    (racket-mode isend-mode cider clojure-mode web-mode vue-html-mode ssass-mode pyvenv mmm-mode edit-indirect auto-complete)))
 '(py-closing-list-dedents-bos t)
 '(py-indent-list-style (quote line-up-with-first-element))
 '(py-install-directory "C:/Users/Heitor/Desktop/code/")
 '(py-separator-char "/")
 '(scroll-conservatively 100)
 '(scroll-preserve-screen-position t)
 '(scroll-step 1)
 '(sql-db2-login-params nil)
 '(tool-bar-mode nil)
 '(web-mode-auto-close-style 1)
 '(web-mode-auto-quote-style 1)
 '(web-mode-enable-auto-closing t)
 '(web-mode-enable-auto-opening nil)
 '(web-mode-enable-auto-pairing nil)
 '(web-mode-enable-auto-quoting nil)
 '(yas/prompt-functions
   (quote
    (yas/ido-prompt yas/x-prompt yas/completing-prompt yas/no-prompt))))

(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:inherit nil :stipple nil :background "white" :foreground "black" :inverse-video nil :box nil :strike-through nil :overline nil :underline nil :slant normal :weight normal :height 120 :width normal :foundry "outline" :family "ProggyTinyTTSZ")))))


;; Fonts

;; larger display font
;; '(default ((t (:inherit nil :stipple nil :background "white" :foreground "black" :inverse-video nil :box nil :strike-through nil :overline nil :underline nil :slant normal :weight normal :height 100 :width normal :foundry "outline" :family "Liberation Mono")))))


;; auto-complete-mode
(require 'auto-complete-config)

(setq-default ac-sources (add-to-list 'ac-sources 'ac-source-dictionary))
(setq ac-disable-faces nil)

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


;; globals
(defun my-indent-whole-buffer ()
  (interactive)
  (save-excursion
    (mark-whole-buffer)
    (call-interactively 'indent-region)))

(defun load-diary ()
  (interactive)
  (find-file "c:/Users/Heitor/Desktop/code/heitor-general/diary.txt"))


;; C-<backspace> does not add to kill ring
(defun backward-delete-word (arg)
  (interactive "p")
  (delete-region (point) (progn (backward-word arg) (point))))

;; set keys
(global-set-key (kbd "C-<backspace>") 'backward-delete-word) 

(global-set-key (kbd "C-t") 'yank)
(global-set-key (kbd "M-t") 'yank-pop)
(global-set-key (kbd "M-o") 'other-window)

(global-set-key (kbd "RET") 'newline-and-indent)

(global-set-key (kbd "C-<") 'previous-buffer)
(global-set-key (kbd "C->") 'next-buffer)
(global-set-key (kbd "C-'") 'switch-to-buffer)

(global-set-key (kbd "C-c C-a") 'auto-complete-mode)

(global-set-key (kbd "<f2>") 'run-lisp)
(global-set-key (kbd "<f3>") 'isearch-forward)
(define-key isearch-mode-map (kbd "<f3>") 'isearch-repeat-forward)

(global-set-key (kbd "<f4>") 'load-diary)

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

(global-set-key (kbd "M-p") 'other-window)

(global-set-key (kbd "C-c C-e") 'electric-indent-mode)
(global-set-key (kbd "C-c i") 'my-indent-whole-buffer)

(global-set-key (kbd "M-w") 'kill-ring-save)
(global-set-key (kbd "M-u") 'undo)

(global-set-key (kbd "C-x x") 'copy-line)

;; cursor
(blink-cursor-mode -1)
(set-default 'cursor-type 'bar)
(set-cursor-color "#53A960")

;; force regular font 
(defun disable-bold ()
  (interactive)
  (mapc (lambda (face) (set-face-attribute face nil :weight 'normal :underline nil)) (face-list)))
(call-interactively 'disable-bold)

(electric-indent-mode t)
(add-hook 'python-mode-hook
          (lambda () (set (make-local-variable 'electric-indent-mode) nil)))  ; disable electric indent for python

;; custom functions
;; general
(defun line-emptyp ()
  (= (line-beginning-position) (line-end-position)))

(defun copy-line ()
  (interactive)
  (beginning-of-line)
  (kill-line)
  (yank))

;; Python
;; Inferior Python and testing
(setq python-shell-interpreter "c:/Users/Heitor/AppData/Local/Programs/Python/Python39/python.exe")

(setenv "PYTHONPATH" "C:/Users/Heitor/Desktop/code/shared/python/my-modules/")
(setenv "PYTHONSTARTUP" "C:/Users/Heitor/Desktop/code/shared/python/mystartup.py")
(setenv "PYTHONUNBUFFERED" "x")
(setenv "PYTHONIOENCODING" "utf8")

;; suppress Python shell warning
(setq python-shell-completion-native-disabled-interpreters '("python"))

;; closing bracket after multi-line definition should line up with original
;; https://stackoverflow.com/questions/4293074/in-emacs-python-mode-customize-multi-line-statement-indentation

(defadvice python-calculate-indentation (around outdent-closing-brackets)
  "Handle lines beginning with a closing bracket and indent them so that
they line up with the line containing the corresponding opening bracket."
  (save-excursion
    (beginning-of-line)
    (let ((syntax (syntax-ppss)))
      (if (and (not (eq 'string (syntax-ppss-context syntax)))
               (python-continuation-line-p)
               (cadr syntax)
               (skip-syntax-forward "-")
               (looking-at "\\s)"))
          (progn
            (forward-char 1)
            (ignore-errors (backward-sexp))
            (setq ad-return-value (current-indentation)))
        ad-do-it))))
(ad-activate 'python-calculate-indentation)

(defun my-python-send-buffer ()
  (interactive)
  (save-excursion
    (python-shell-send-string (trim-string (buffer-string)))))

(defun my-python-print-and-send-buffer ()
  (interactive)
  (save-excursion
    (python-shell-send-string (concat "print('''" (trim-string (buffer-string)) "''')"))
    (python-shell-send-string (concat "print('')\n" (trim-string (buffer-string))))))

(defun my-python-send-statement ()
  (interactive)
  ;; (local-set-key [S-return] 'my-python-send-statement)
  (python-shell-send-string (thing-at-point 'line))
  (python-shell-send-string "\n")
  (move-end-of-line nil))

(defun my-python-send-block ()
  (interactive)
  ;; (local-set-key [C-return] 'my-python-send-block)
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
    ;;    (python-shell-send-string "; print(end=\"\")")
    (dotimes (i lines-of-block)
      (next-line))
    (end-of-line)))


(defun my-js-send-block ()
  (interactive)
  (set-mark (line-end-position))
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

;; isend-mode
(defun my-isend-send-sexp ()
  (interactive)
  (save-excursion
    (backward-sexp)
    (mark-sexp)
    ;; (kill-ring-save)
    (call-interactively 'isend-send-buffer)))

(defun my-isend-send-line ()
  (interactive)
  (set-mark (line-end-position))
  (beginning-of-line)
  (call-interactively 'isend-send)
  ;; (previous-line)
  (end-of-line))

(defun my-isend-send-block ()
  (interactive)
  (set-mark (line-end-position))
  (let ((lines-of-block 0))
    (while (or (equal (line-beginning-position) 0) (not (line-emptyp)))
      (previous-line)
      (beginning-of-line)
      (set 'lines-of-block (+ 1 lines-of-block)))
    (beginning-of-line)
    (call-interactively 'isend-send)
    (end-of-line)))


(defun my-cider-save-and-compile-buffer ()
  (interactive)
  (call-interactively 'save-buffer)
  (call-interactively 'cider-load-buffer))


;; Racket
(setq scheme-program-name "C:/Progra~1/Racket/racket.exe")

;; Common LISP
(setq inferior-lisp-program "c:/sbcl2/sbcl.exe")
;; (setq inferior-lisp-program "c:/clisp/clisp.exe")

(defun my-lisp-send-buffer ()
  (interactive)
  (save-excursion
    (mark-whole-buffer)
    (call-interactively 'lisp-eval-region)
    (deactivate-mark)
    (end-of-buffer)))

(defun my-scheme-send-buffer ()
  (interactive)
  (save-excursion
    (mark-whole-buffer)
    (call-interactively 'scheme-send-region)
    (deactivate-mark)
    (end-of-buffer)))

(add-hook 'lisp-mode-hook
          (lambda ()
            (local-set-key [S-return] 'lisp-eval-last-sexp)
            (local-set-key [C-return] 'my-lisp-send-buffer)))

(add-hook 'scheme-mode-hook
          (lambda ()
            (local-set-key [C-return] 'my-scheme-send-buffer)
            (local-set-key [S-return] 'scheme-send-last-sexp)))

(add-hook 'mhtml-mode-hook
          (lambda ()
            (auto-complete-mode 1)
            (define-key mhtml-mode-map (kbd "C-/") 'sgml-close-tag)))

(add-hook 'clojure-mode-hook
          (lambda ()
            (auto-complete-mode 1)
            (define-key clojure-mode-map (kbd "<M-left>") 'backward-sexp)
            (define-key clojure-mode-map (kbd "<M-right>") 'forward-sexp)
            (define-key clojure-mode-map (kbd "<C-return>") 'my-cider-save-and-compile-buffer)
            (local-set-key (kbd "<S-return>") 'cider-eval-last-sexp)))

(add-hook 'python-mode-hook
          (lambda ()
            (local-set-key (kbd "C-c c") 'comment-region)
            (local-set-key (kbd "C-c u") 'uncomment-region)
            (local-set-key (kbd "RET") 'newline-and-indent)
            
            (local-set-key [S-return] 'my-python-send-statement)
            (local-set-key [C-return] 'my-python-send-buffer)))

(add-hook 'js-mode-hook
          (lambda ()
            (local-set-key (kbd "C-c c") 'js-send-buffer)
            (local-set-key [S-return] 'my-js-send-line)
            (local-set-key [C-return] 'my-js-send-block)))

(add-to-list 'auto-mode-alist '("\\.php\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.vue\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.html\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.js\\'" . web-mode))

;; text mode
(add-hook 'text-mode-hook
          (lambda ()
            (setq indent-tabs-mode t)
            (auto-complete-mode 1)))

(define-key text-mode-map (kbd "TAB") 'self-insert-command)
(define-key text-mode-map [backtab] 'indent-for-tab-command)

(add-hook 'inferior-python-mode-hook
          (lambda ()
            (auto-complete-mode 1)))

(add-hook 'inferior-scheme-mode-hook
          (lambda ()
            (auto-complete-mode 1)))

(add-hook 'cider-repl-mode-hook
          (lambda ()
            (auto-complete-mode 1)))

(put 'upcase-region 'disabled nil)


;; Foreign languages input
(defun get-greek-entry ()
  (interactive)

  (activate-input-method "portuguese-prefix")
  (insert 
   (read-string "Portugues: " nil nil nil t))

  (insert "\n")
  (activate-input-method "greek")
  (insert 
   (read-string "ELLINIKA: " nil nil nil t))

  (insert "\n\n")
  (get-greek-entry))

;; swap input methods in buffer
(defun my-greek-swap-input-methods ()
  (interactive)
  (if (equal current-input-method "greek")
      (activate-input-method "portuguese-prefix")
    (activate-input-method "greek")))


;; Custom insert strings
(defun insert-my-custom-string ()
  (interactive)
  (insert "My custom string"))
