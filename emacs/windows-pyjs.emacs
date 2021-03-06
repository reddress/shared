;; dot emacs

(setq inhibit-startup-message t)
(setq default-directory "C:/Users/Heitor/Desktop/code/")

;; window position
(setq initial-frame-alist '((top . 0) (left . 0) (width . 74) (height . 82)))

;; MELPA
;; https://melpa.org/#/getting-started

(require 'package)
(let* ((no-ssl (and (memq system-type '(windows-nt ms-dos))
                    (not (gnutls-available-p))))
       (proto (if no-ssl "http" "https")))

  ;; Comment/uncomment these two lines to enable/disable MELPA and MELPA Stable as desired
  (add-to-list 'package-archives (cons "melpa" (concat proto "://melpa.org/packages/")) t)
  ;;(add-to-list 'package-archives (cons "melpa-stable" (concat proto "://stable.melpa.org/packages/")) t)
  (when (< emacs-major-version 24)
    ;; For important compatibility libraries like cl-lib
    (add-to-list 'package-archives (cons "gnu" (concat proto "://elpa.gnu.org/packages/")))))
(package-initialize)

;; Inferior Python and testing
;; https://github.com/heitorchang/code-practice/tree/master/codefights
(setq python-shell-interpreter "C:/Users/Heitor/AppData/Local/Programs/Python/Python37-32/python.exe")

(setenv "PYTHONPATH" "C:/Users/Heitor/Desktop/code/shared/python/my-modules/;C:/users/heitor/desktop/code/reading-list/interactive-py/oct2018/")
(setenv "PYTHONSTARTUP" "C:/Users/Heitor/Desktop/code/shared/python/mystartup.py")

(defun trim-string (string)
  "Remove white spaces in beginning and ending of STRING.
White space here is any of: space, tab, emacs newline (line feed, ASCII 10)."
  (replace-regexp-in-string "\\`[ \t\n]*" "" (replace-regexp-in-string "[ \t\n]*\\'" "" string)))

(defun my-python-test-buffer ()
  (interactive)
  (save-excursion
    (python-shell-send-string (trim-string (buffer-string)))))
    ;; (python-shell-send-string (concat "print('')\n" "test()"))))


(defun my-python-send-buffer ()
  (interactive)
  (save-excursion
    (python-shell-send-string (concat "print('''" (trim-string (buffer-string)) "''')"))
    (python-shell-send-string (concat "print('')\n" (trim-string (buffer-string))))))


;; Custom

;; Added by Package.el.  This must come before configurations of
;; installed packages.  Don't delete this line.  If you don't want it,
;; just comment it out by adding a semicolon to the start of the line.
;; You may delete these explanatory comments.
(package-initialize)

(custom-set-variables
 '(ansi-color-names-vector ["black" "red" "green" "yellow" "blue" "magenta" "cyan" "white"])
 '(js-indent-level 2)
 '(c-basic-offset 4)
 '(c-default-style "linux")
 '(column-number-mode t)
 '(default-tab-width 4 t)
 '(fill-column 72)
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

;; globals
(setq ring-bell-function 'ignore)

(setq-default frame-title-format "%f")

(set-language-environment "UTF-8")
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

(global-set-key (kbd "C-x p") 'my-previous-window)
(global-set-key (kbd "C-<") 'previous-buffer)
(global-set-key (kbd "C->") 'next-buffer)
(global-set-key (kbd "C-'") 'switch-to-buffer)

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

(global-set-key (kbd "<M-up>") 'other-window)
(global-set-key (kbd "<M-down>") 'other-window)

(global-set-key (kbd "M-p") 'other-window)

(global-set-key (kbd "C-c C-e") 'electric-indent-mode)
(global-set-key (kbd "C-c i") 'my-indent-whole-buffer)

(global-set-key (kbd "C-c i") 'my-indent-whole-buffer)
(global-set-key (kbd "C-c l") 'my-insert-console-log)

(global-set-key (kbd "M-e") 'kill-ring-save)
(global-set-key (kbd "M-w") 'kill-ring-save)
(global-set-key (kbd "M-u") 'undo)

(global-set-key (kbd "RET") 'newline-and-indent)

;; WASD cursor movement
;; (global-set-key (kbd "M-w") 'previous-line)
;; (global-set-key (kbd "M-a") 'backward-char)
;; (global-set-key (kbd "M-s") 'next-line)
;; (global-set-key (kbd "M-d") 'forward-char)

;; (global-set-key (kbd "C-p") 'scroll-down-command)

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

(electric-indent-mode t)
(add-hook 'python-mode-hook
          (lambda () (set (make-local-variable 'electric-indent-mode) nil)))  ; disable electric indent for python

;; custom functions
;; general

;; (defun hide-eol ()
;;   (interactive)
;;   (setq buffer-display-table (make-display-table))
;;   (aset buffer-display-table ?\^M []))

(defun copy-line ()
  (interactive)
  (beginning-of-line)
  (kill-line)
  (yank))

(global-set-key (kbd "C-x x") 'copy-line)


;; Python
(setenv "PYTHONUNBUFFERED" "x")

(defun line-emptyp ()
  (= (line-beginning-position) (line-end-position)))

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

;; javascript
;; (require 'js-comint)
;;;(setq inferior-js-program-command "java -jar c:/Users/heitor/Desktop/programming/js/rhino1_7R4/js.jar")
(setq inferior-js-program-command "node.exe -i")

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
    ;; (python-shell-send-string "\n")
    ;; (python-shell-send-string "; print(end=\"\")")
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

(defun node-suppress-undefined ()
  (interactive)
  (comint-send-string inferior-js-buffer "module.exports.repl.ignoreUndefined = true;"))

(global-set-key (kbd "C-c j") 'javascript-mode)
(global-set-key (kbd "C-c h") 'html-mode)

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

(add-hook 'python-mode-hook
          (lambda ()
            (local-set-key (kbd "C-c c") 'comment-region)
            (local-set-key (kbd "C-c u") 'uncomment-region)
            
            (local-set-key [S-return] 'my-python-send-statement)
            (local-set-key [M-return] 'my-python-send-buffer)
            (local-set-key [C-return] 'my-python-test-buffer)))

(add-hook 'js-mode-hook
          (lambda ()
            (local-set-key (kbd "C-c c") 'js-send-buffer)
            (local-set-key (kbd "C-c n") 'node-suppress-undefined)
            (local-set-key [S-return] 'my-js-send-line)
            (local-set-key [C-return] 'my-js-send-block)
            (call-interactively 'node-suppress-undefined)))

(add-hook 'inferior-python-mode-hook
          (lambda ()
            (auto-complete-mode 1)))

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
            (setq indent-tabs-mode t)
            ;; (local-set-key [return] 'my-text-tabify)
            (call-interactively 'auto-complete-mode)))

(define-key text-mode-map (kbd "TAB") 'self-insert-command)
(define-key text-mode-map [backtab] 'indent-for-tab-command)

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
  ; (previous-line)
  (let ((lines-of-block 0))
    (while (or (equal (line-beginning-position) 0) (not (line-emptyp)))
      (previous-line)
      (beginning-of-line)
      (set 'lines-of-block (+ 1 lines-of-block)))
    (beginning-of-line)
    (call-interactively 'isend-send)
    ;;(dotimes (i lines-of-block)
    ;;  (next-line))
    (end-of-line)))

(defun my-isend-send-buffer ()
  (interactive)
  (mark-whole-buffer)
  (call-interactively 'isend-send)
  (end-of-buffer))

(add-hook 'isend-mode-hook
          (lambda ()
            (local-set-key [S-return] 'my-isend-send-line)
            (local-set-key [C-return] 'my-isend-send-block)
            (local-set-key [M-return] 'my-isend-send-buffer)))

(put 'upcase-region 'disabled nil)

;; suppress Python shell warning
(setq python-shell-completion-native-disabled-interpreters '("python"))
