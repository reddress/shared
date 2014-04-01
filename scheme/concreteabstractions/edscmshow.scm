;; This file contains an definition of the show procedure, specific to
;; EdScheme (version 5.0 for Windows and 4.0 for the Macintosh) for use with
;; section 9.4 (An Application: Computer Graphics) of Concrete
;; Abstractions: An Introduction to Computer Science Using Scheme by
;; Max Hailperin, Barbara Kaiser, and Karl Knight.

(define show
  (let ((counter 0)
        (make-size-legal
         (lambda (size)
           (min 3000
                (max 20
                     (inexact->exact (round size)))))))
    (lambda (image)
      (let ((w (make-size-legal (width image)))
            (h (make-size-legal (height image))))
        (let ((x-coord (lambda (p) (- (x-coord p) (/ w 2))))
              (y-coord (lambda (p) (- (y-coord p) (/ h 2)))))
          (set! counter (add1 counter))
          (let ((title (number->string counter)))
            (let ((win (make-graphics-window (list w h))))
              (turtle-hide  win)
              (window-set-title title win)
              (clean win)
              (draw-on image
                       (lambda (op)     ; the drawing medium
                         (cond ((equal? op 'draw-line)
                                (lambda (point0 point1)
                                  (polygon (list (list (x-coord point0)
                                                       (y-coord point0))
                                                 (list (x-coord point1)
                                                       (y-coord point1)))
                                           win)))
                               ((equal? op 'draw-filled-triangle)
                                (lambda (point0 point1 point2)
                                  (polygon-paint (list (list (x-coord point0)
                                                             (y-coord point0))
                                                       (list (x-coord point1)
                                                             (y-coord point1))
                                                       (list (x-coord point2)
                                                             (y-coord point2)
                                                             )))))
                               (else (error
                                      "unknown operation on drawing medium"
                                      op)))))
              counter)))))))