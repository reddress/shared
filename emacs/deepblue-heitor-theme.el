(deftheme deepblue-heitor
  "Created 2020-10-15.")

(custom-theme-set-faces
 'deepblue-heitor
 '(default ((t (:family "ProggyTinyTTSZ" :foundry "unknown" :width normal :height 120 :weight normal :slant normal :underline nil :overline nil :strike-through nil :box nil :inverse-video nil :foreground "white" :background "#08302A" :stipple nil :inherit nil))))
 '(cursor ((t (:weight normal :underline nil :background "#209933"))))
 '(fixed-pitch ((t (:family "ProggyTinyTTSZ" :weight normal :underline nil))))
 '(variable-pitch ((t (:family "ProggyTinyTTSZ" :weight normal :underline nil))))
 '(escape-glyph ((t (:weight normal :underline nil :foreground "cyan"))))
 '(homoglyph ((t (:weight normal :underline nil :foreground "cyan"))))
 '(minibuffer-prompt ((t (:weight normal :underline nil :foreground "CadetBlue1"))))
 '(highlight ((t (:weight normal :underline nil :background "purple"))))
 '(region ((t (:background "sky blue" :foreground "dark blue" :inverse-video nil :underline nil :weight normal))))
 '(shadow ((t (:weight normal :underline nil :foreground "grey70"))))
 '(secondary-selection ((t (:weight normal :underline nil :background "SkyBlue4"))))
 '(trailing-whitespace ((t (:weight normal :underline nil :background "red1"))))
 '(font-lock-builtin-face ((t (:weight normal :underline nil :foreground "LightCoral"))))
 '(font-lock-comment-delimiter-face ((t (:weight normal :underline nil :foreground "gray64"))))
 '(font-lock-comment-face ((t (:weight normal :underline nil :foreground "gray64"))))
 '(font-lock-constant-face ((t (:weight normal :underline nil :foreground "DarkOliveGreen3"))))
 '(font-lock-doc-face ((t (:weight normal :underline nil :foreground "moccasin"))))
 '(font-lock-function-name-face ((t (:weight normal :underline nil :foreground "goldenrod"))))
 '(font-lock-keyword-face ((t (:weight normal :underline nil :foreground "DeepSkyBlue1"))))
 '(font-lock-negation-char-face ((t (:weight normal :underline nil))))
 '(font-lock-preprocessor-face ((t (:weight normal :underline nil :foreground "gold"))))
 '(font-lock-regexp-grouping-backslash ((t (:weight normal :underline nil))))
 '(font-lock-regexp-grouping-construct ((t (:weight normal :underline nil))))
 '(font-lock-string-face ((t (:weight normal :underline nil :foreground "burlywood"))))
 '(font-lock-type-face ((t (:weight normal :underline nil :foreground "CadetBlue1"))))
 '(font-lock-variable-name-face ((t (:weight normal :underline nil :foreground "SeaGreen2"))))
 '(font-lock-warning-face ((t (:weight normal :underline nil :inherit (error)))))
 '(button ((t (:weight normal :underline nil :inherit (link)))))
 '(link ((t (:weight normal :underline nil :foreground "cyan1"))))
 '(link-visited ((t (:weight normal :underline nil :foreground "violet" :inherit (link)))))
 '(fringe ((t (:weight normal :underline nil :background "black"))))
 '(header-line ((t (:weight normal :underline nil :box nil :foreground "grey90" :background "grey20" :inherit (mode-line)))))
 '(tooltip ((t (:family "ProggyTinyTTSZ" :weight normal :underline nil :foreground "black" :background "lightyellow" :inherit (variable-pitch)))))
 '(mode-line ((t (:weight normal :underline nil :box (:line-width 1 :color nil :style released-button) :foreground "black" :background "gray75"))))
 '(mode-line-buffer-id ((t (:weight normal :underline nil :foreground "black"))))
 '(mode-line-emphasis ((t (:weight normal :underline nil))))
 '(mode-line-highlight ((t (:weight normal :underline nil :box (:line-width 2 :color "grey40" :style released-button)))))
 '(mode-line-inactive ((t (:weight normal :underline nil :box (:line-width 1 :color "gray40" :style nil) :foreground "black" :background "gray40"))))
 '(isearch ((t (:weight normal :underline nil :foreground "white" :background "coral2"))))
 '(isearch-fail ((t (:weight normal :underline nil :background "red4"))))
 '(lazy-highlight ((t (:weight normal :underline nil :foreground "white" :background "cadetblue"))))
 '(match ((t (:weight normal :underline nil :background "DeepPink4"))))
 '(next-error ((t (:weight normal :underline nil :inherit (region)))))
 '(query-replace ((t (:weight normal :underline nil :inherit (isearch))))))

(provide-theme 'deepblue-heitor)