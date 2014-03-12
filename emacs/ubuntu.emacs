;; Custom
(custom-set-variables
 '(ansi-color-names-vector ["black" "red" "green" "yellow" "DodgerBlue1" "magenta" "cyan" "white"])
 '(c-basic-offset 4)
 '(js-indent-level 2)
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

;; globals
(add-to-list 'load-path "~/.emacs.d")

(setq backup-inhibited t)
(delete-selection-mode t)
(menu-bar-mode -1)

;; cursor
(blink-cursor-mode -1)
(set-default 'cursor-type 'bar)
(set-cursor-color "#338833")

;; force regular font
(mapc (lambda (face) (set-face-attribute face nil :weight 'normal :underline nil)) (face-list))

(electric-indent-mode t)
(add-hook 'python-mode-hook
          (lambda () (set (make-local-variable 'electric-indent-mode) nil)))  ; disable electric indent for python

;; window position
(when window-system
  (set-frame-size (selected-frame) 79 55)
  (set-frame-position (selected-frame) 0 0))

;; custom functions
;; general
(defun kill-all-buffers ()
  (interactive)
  (mapc 'kill-buffer (buffer-list)))

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

;; Scheme
(defun my-scheme-send-buffer ()
  (interactive)
  (mark-whole-buffer)
  (call-interactively 'scheme-send-region)
  (end-of-buffer))

;; Python
(defun line-emptyp ()
  (= (line-beginning-position) (line-end-position)))

(defun my-python-send-statement ()
  (interactive)
  (local-set-key [S-return] 'my-python-send-statement)
  (end-of-line)
  (set-mark (line-beginning-position))
  (call-interactively 'python-shell-send-region)
;  (python-shell-send-string "; print(end=\"\")"))
  (python-shell-send-string "\n"))

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

;; auto-complete-mode
(require 'auto-complete-config)
(add-to-list 'ac-dictionary-directories "c:/Users/Heitor/Desktop/LispCabinetHome/.emacs.d/dict")
(setq-default ac-sources (add-to-list 'ac-sources 'ac-source-dictionary))

(global-auto-complete-mode t)
(setq ac-ignore-case nil)
(define-key ac-completing-map "\r" nil)  ; remove completion with RET
(setq ac-auto-start 2)
;; prevent pop-up on arrow keys
(define-key ac-completing-map (kbd "<down>") nil)
(define-key ac-completing-map (kbd "<up>") nil)
(setq ac-delay 0.001)

;; settings for not immediately completing
;(global-auto-complete-mode t)
;(setq ac-auto-start 2)
;(setq ac-ignore-case nil)
;(setq ac-delay 1)
;(ac-set-trigger-key "TAB")

;; set keys
(global-set-key (kbd "RET") 'newline-and-indent)
(global-set-key "\M-p" 'add-nums-in-brackets)

(add-hook 'scheme-mode-hook
          (lambda ()
            (local-set-key [C-return] 'my-scheme-send-buffer)
;            (local-set-key [tab] 'scheme-complete-or-indent)
            (local-set-key [S-return] 'scheme-send-last-sexp)
            (local-set-key [return] 'newline-and-indent)))

(add-hook 'inferior-scheme-mode-hook
          (lambda ()
            (local-set-key [tab] 'scheme-complete-or-indent)))

(add-hook 'lisp-mode-hook
          (lambda ()
            ; (local-set-key [tab] 'slime-indent-and-complete-symbol)
            (local-set-key [tab] 'scheme-complete-or-indent)
            (local-set-key [S-return] 'lisp-eval-last-sexp)
            (local-set-key [return] 'newline-and-indent)))

(add-hook 'clojure-mode-hook
          (lambda ()
            (local-set-key [S-return] 'cider-eval-last-expression)))
;            (local-set-key [tab] 'slime-indent-and-complete-symbol)
;            (local-set-key [return] 'newline-and-indent)))

(add-hook 'python-mode-hook
          (lambda ()
            (local-set-key [S-return] 'my-python-send-statement)
            (local-set-key [C-return] 'my-python-send-block)))

;; obsolete
;; (autoload 'scheme-smart-complete "scheme-complete" nil t)
;;(load "~/scheme/scheme-complete")
;;(eval-after-load 'scheme
;;  '(define-key scheme-mode-map "\e\t" 'scheme-smart-complete))
