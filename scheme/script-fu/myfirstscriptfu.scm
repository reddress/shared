(define (script-fu-text-box
         inText inFont inFontSize inTextColor)
  (let*
      (
       (theImageWidth 10)
       (theImageHeight 10)
       (theImage (car
                  (gimp-image-new
                   theImageWidth
                   theImageHeight
                   RGB)))
       (theText)

       (theLayer
        (car
         (gimp-layer-new
          theImage
          theImageWidth
          theImageHeight
          RGB-IMAGE
          "layer 1"
          100
          NORMAL
          )
         )
        )
       )
    (gimp-image-add-layer theImage theLayer 0)
    ;; (gimp-display-new theImage)))

    (gimp-context-set-background '(255 255 255))
    (gimp-context-set-foreground inTextColor)

    (gimp-drawable-fill theLayer BACKGROUND-FILL)

    (set! theText
          (car (gimp-text-fontname
                theImage theLayer
                0 0
                inText
                0
                TRUE
                inFontSize PIXELS
                "Sans")
               ))
    (set! theImageWidth (car (gimp-drawable-width theText)))
    (set! theImageHeight (car (gimp-drawable-height theText)))

    (gimp-image-resize theImage theImageWidth theImageHeight 0 0)
    (gimp-layer-resize theLayer theImageWidth theImageHeight 0 0)

    (gimp-display-new theImage)))

(script-fu-register
 "script-fu-text-box"
 "My Text Box"
 "Create simple text box"
 "Michael Terry"
 "(C) 1997"
 "October 27, 1997"
 ""
 SF-STRING "Text" "Text Box"
 SF-FONT "Font" "Charter"
 SF-ADJUSTMENT "Font size"  '(50 1 1000 1 10 0 1)
 SF-COLOR "Color" '(0 0 0)
 )

(script-fu-menu-register "script-fu-text-box" "<Image>/File/Create/Text")
