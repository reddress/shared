;; shortcut to save selection as new image

(define (script-fu-my-save-selection img drawable)

  (let* (
         (original-filename (car (gimp-image-get-filename img)))
         (filename-length (string-length original-filename))
         (filename-number (substring original-filename (- filename-length 7)
                                     (- filename-length 4))))

;;    (gimp-message original-filename)
    (gimp-edit-copy drawable)

    (let* (
           (new-image (car (gimp-edit-paste-as-new))))
      (gimp-image-set-filename new-image
                               (string-append "C:\\FOTOS_NAINAI\\NAINAI_PT_" filename-number "_" (apply string-append (map number->string (time))) ".jpg"))
      ;;(gimp-display-new new-image))
      (file-jpeg-save 1
                      new-image
                      (car (gimp-image-get-active-drawable new-image))
                      (string-append "C:\\FOTOS_NAINAI\\NAINAI_PT_" filename-number "_" (apply string-append (map number->string (time))) ".jpg")
                      (string-append "C:\\FOTOS_NAINAI\\NAINAI_PT_" filename-number "_" (apply string-append (map number->string (time))) ".jpg")
                      0.90
                      0.0
                      1
                      1
                      "Heitor White Belt Gimp Script-Fu"
                      0 1 0 0)  ;; subsampling as default found online
                      ;; 3 1 0 0)  ;; subsampling at other extreme
      )
    )
  )

(script-fu-register "script-fu-my-save-selection"
                    "Save Selection"
                    "Save selection as new image"
                    "Heitor Chang"
                    "Heitor Chang"
                    "2014-10-05"
                    "RGB*, GRAY*"
                    SF-IMAGE "Input image" 0
                    SF-DRAWABLE "Input drawable" 0)
(script-fu-menu-register "script-fu-my-save-selection"
                         "<Image>/Script-Fu/SaveSelection")
