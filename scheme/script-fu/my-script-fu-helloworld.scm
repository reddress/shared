(define (script-fu-hello-world img drawable)
  (gimp-undo-push-group-start img)
  (set! text-float (car (gimp-text-fontname img
                                            drawable
                                            10 10
                                            (car (gimp-image-get-filename img))
                                            0 1 50 0
                                            "Sans")))

  (gimp-floating-sel-anchor text-float)

  (gimp-undo-push-group-end img)
  (gimp-displays-flush))

(script-fu-register "script-fu-hello-world"
                    "Hello World"
                    "write hello world"
                    "Dov Grobgeld"
                    "Dov G"
                    "2002"
                    "RGB*, GRAY*"
                    SF-IMAGE "Input image" 0
                    SF-DRAWABLE "Input drawable" 0)
(script-fu-menu-register "script-fu-hello-world"
                         "<Image>/Script-Fu/Tutorials")
