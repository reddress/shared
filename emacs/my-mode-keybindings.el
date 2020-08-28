;; set keys

;; https://emacs.stackexchange.com/questions/352/how-to-override-major-mode-bindings/358#358
;; my-mode


(defvar my-mode-map (make-sparse-keymap)
  "Keymap for `my-mode'.")

;;;###autoload
(define-minor-mode my-mode
  "A minor mode so that my key settings override annoying major modes."
  ;; If init-value is not set to t, this mode does not get enabled in
  ;; `fundamental-mode' buffers even after doing \"(global-my-mode 1)\".
  ;; More info: http://emacs.stackexchange.com/q/16693/115
  :init-value t
  :lighter " my-mode"
  :keymap my-mode-map)

;;;###autoload
(define-globalized-minor-mode global-my-mode my-mode my-mode)

;; https://github.com/jwiegley/use-package/blob/master/bind-key.el
;; The keymaps in `emulation-mode-map-alists' take precedence over
;; `minor-mode-map-alist'
(add-to-list 'emulation-mode-map-alists `((my-mode . ,my-mode-map)))

;; Turn off the minor mode in the minibuffer
(defun turn-off-my-mode ()
  "Turn off my-mode."
  (my-mode -1))
(add-hook 'minibuffer-setup-hook #'turn-off-my-mode)

;; (provide 'my-mode)


;; C-j, k, l, i
;; left-char right-char
;; previous-line next-line

;; C-k kill-line
;; C-l recenter-top-bottom

;; M-j, k, l, i
;; left-word right-word
;; backward-paragraph forward-paragraph

;; (define-key my-mode-map (kbd "C-j") #'left-char)
;; (define-key my-mode-map (kbd "C-k") #'next-line)
;; (define-key my-mode-map (kbd "C-l") #'right-char)
;; (define-key my-mode-map (kbd "C-i") #'previous-line)
;; (define-key my-mode-map (kbd "C-u") #'kill-line)
;; (define-key my-mode-map (kbd "C-o") #'recenter-top-bottom)
;; (define-key my-mode-map (kbd "<tab>") #'indent-for-tab-command)
;; (define-key my-mode-map (kbd "<C-tab>") #'indent-for-tab-command)

;; (define-key my-mode-map (kbd "M-j") #'left-word)
;; (define-key my-mode-map (kbd "M-k") #'forward-paragraph)
;; (define-key my-mode-map (kbd "M-l") #'right-word)
;; (define-key my-mode-map (kbd "M-i") #'backward-paragraph)

