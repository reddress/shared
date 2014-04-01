;; This file contains excerpts from the textbook Concrete
;; Abstractions: An Introduction to Computer Science Using Scheme, by
;; Max Hailperin, Barbara Kaiser, and Karl Knight, Copyright (c) 1998
;; by the authors. Full text is available for free at
;; http://www.gustavus.edu/+max/concrete-abstractions.html

;; Note that system-specific versions of the show procedure are also
;; available from the Concrete Abstractions supporting materials web
;; site -- look in the section of "Information on using various Scheme
;; implementations with the text".

;; Chapter 9: Generic Operations

;; 9.4  An Application: Computer Graphics

(define make-point cons)

(define x-coord car)

(define y-coord cdr)

;; Interface to image operations

(define width
  (lambda (image)
    (image 'width)))

(define height
  (lambda (image)
    (image 'height)))

(define draw-on
  (lambda (image medium)
    ((image 'draw-on) medium)))

;; Interface to drawing medium operations

(define draw-line-on
  (lambda (point0 point1 medium)
    ((medium 'draw-line) point0 point1)))

(define draw-filled-triangle-on
  (lambda (point0 point1 point2 medium)
    ((medium 'draw-filled-triangle) point0 point1 point2)))

(define basic-image-size 100)

(define transform-point ; from -1 to 1 into 0 to basic-image-size
  (lambda (point)
    (define transform-coord
      (lambda (coord)
        (* (/ (+ coord 1) 2)  ; fraction of the way to top or right
           basic-image-size)))
    (make-point (transform-coord (x-coord point))
                (transform-coord (y-coord point)))))

(define make-line
  (lambda (point0 point1)
    (lambda (op)
      (cond
       ((equal? op 'width) basic-image-size)
       ((equal? op 'height) basic-image-size)
       ((equal? op 'draw-on)
        (lambda (medium)
          (draw-line-on (transform-point point0)
                        (transform-point point1)
                        medium)))
       (else (error "unknown operation on line" op))))))

(define make-overlaid-image
  (lambda (image1 image2)
    (if (not (and (= (width image1) (width image2))
                  (= (height image1) (height image2))))
        (error "can't overlay images of different sizes")
        (lambda (op)
          (cond ((equal? op 'width) (width image1))
                ((equal? op 'height) (height image1))
                ((equal? op 'draw-on)
                 (lambda (medium)
                   (draw-on image1 medium)
                   (draw-on image2 medium)))
                (else
                 (error "unknown operation on overlaid image"
                        op)))))))

(define c-curve
  (lambda (x0 y0 x1 y1 level)
    (if (= level 0)
        (make-line (make-point x0 y0) (make-point x1 y1))
        (let ((xmid (/ (+ x0 x1) 2))
              (ymid (/ (+ y0 y1) 2))
              (dx (- x1 x0))
              (dy (- y1 y0)))
          (let ((xa (- xmid (/ dy 2)))
                (ya (+ ymid (/ dx 2))))
            (make-overlaid-image
             (c-curve x0 y0 xa ya (- level 1))
             (c-curve xa ya x1 y1 (- level 1))))))))

(define make-transformed-medium
  (lambda (transform base-medium)
    (lambda (op)
      (cond
       ((equal? op 'draw-line)
        (lambda (point0 point1)
          (draw-line-on (transform point0) (transform point1)
                        base-medium)))
       ((equal? op 'draw-filled-triangle)
        (lambda (point0 point1 point2)
          (draw-filled-triangle-on (transform point0)
                                   (transform point1)
                                   (transform point2)
                                   base-medium)))
       (else
        (error "unknown operation on transformed medium"
               op))))))

(define make-turned-image  ; quarter turn to the right
  (lambda (base-image)
    (define turn-point
      (lambda (point)
        ;; y becomes x, and the old width minus x becomes y
        (make-point (y-coord point)
                    (- (width base-image) (x-coord point)))))
    (lambda (op)
      (cond
       ((equal? op 'width) (height base-image))
       ((equal? op 'height) (width base-image))
       ((equal? op 'draw-on)
        (lambda (medium)
          (draw-on base-image
                   (make-transformed-medium turn-point medium))))
       (else (error "unknown operation on turned image" op))))))

;; The definitions below of test-bb and nova-bb won't work until you
;; have defined make-filled-triangle.  Therefore, we commented them
;; out with semicolons.  Once you have defined make-filled-triangle,
;; you can delete the semicolons.

;(define test-bb
;  (make-filled-triangle (make-point 0 1)
;                        (make-point 0 -1)
;                        (make-point 1 -1)))

;(define nova-bb
;  (make-overlaid-image
;   (make-filled-triangle (make-point 0 1)
;                         (make-point 0 0)
;                         (make-point -1/2 0))
;   (make-filled-triangle (make-point 0 0)
;                         (make-point 0 1/2)
;                         (make-point 1 0))))

(define pinwheel
  (lambda (image)
    (let ((turned (make-turned-image image)))
      (let ((half (make-turned-image (make-stacked-image turned
                                                         image))))
        (make-stacked-image half
                            (make-turned-image
                             (make-turned-image half)))))))

(define image->eps
  (lambda (image filename)
    (with-output-to-file filename
      (lambda ()
        (display "%!PS-Adobe-3.0 EPSF-3.0")
        (newline)
        (display "%%BoundingBox: 0 0 ")
        ;; We need to make sure the bounding box is expressed
        ;; using only exact integers, as required by PostScript.
        ;; Therefore we process the width and height of the
        ;; image using round and then inexact->exact. The
        ;; round procedure would convert 10.8 into the inexact
        ;; integer 11., which the inexact->exact then converts
        ;; to the exact integer 11
        (display (inexact->exact (round (width image))))
        (display " ")
        (display (inexact->exact (round (height image))))
        (newline)
        ;; Now do the drawing
        (draw-on image eps-medium)))))

(define eps-medium
  (lambda (op)
    (cond ((equal? op 'draw-line)
           (lambda (point0 point1)
             (display-eps-point point0)
             (display "moveto")
             (display-eps-point point1)
             (display "lineto stroke")
             (newline)))
          ((equal? op 'draw-filled-triangle)
           (lambda (point0 point1 point2)
             (display-eps-point point0)
             (display "moveto")
             (display-eps-point point1)
             (display "lineto")
             (display-eps-point point2)
             (display "lineto closepath fill")
             (newline)))
          (else
           (error "unknown operation on EPS medium"
                  op)))))

(define display-eps-point
  (lambda (point)
    (define display-coord
      (lambda (coord)
        (if (integer? coord)
            (display coord)
            (display (exact->inexact coord)))))
    (display " ")
    (display-coord (x-coord point))
    (display " ")
    (display-coord (y-coord point))
    (display " ")))
