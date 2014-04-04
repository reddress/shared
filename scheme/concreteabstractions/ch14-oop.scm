 (define working-folder "/home/heitor/shared/scheme/concreteabstractions/")

;; redefine for windows
(when (equal? (build-platform) 'mingw32)
      (define working-folder "C:/Users/Heitor/Desktop/emacs-24.3/bin/shared/scheme/concreteabstractions/"))

(define (my-load file)
  (load (string-append working-folder file)))

(my-load "library.scm")
(my-load "oops.scm")

(define-class
  'item-list  ;; name of the class 
  object-class ;; superclass
  '(item-vector num-items)  ;; instance variables
  '(add display total-price delete choose empty?  ;; public methods
        grow))  ;; private methods

(class/set-method!
 item-list-class 'empty?
 (lambda (this)
   (= (item-list/get-num-items this) 0)))

(class/set-method!
 item-list-class 'init
 (lambda (this)
   (item-list/set-item-vector! this (make-vector 10))
   (item-list/set-num-items! this 0)))

(define example-item-list (make-item-list))

(item-list/get-num-items example-item-list)

(object/describe example-item-list)

(class/set-method!
 item-list-class 'add
 (lambda (this item)
   (let ((num-items (item-list/get-num-items this))
         (item-vector (item-list/get-item-vector this)))
     (if (= num-items (vector-length item-vector))
         (begin (item-list/grow this)
                (item-list/add this item))
         (begin (vector-set! item-vector num-items item)
                (item-list/set-num-items! this (+ num-items 1))
                'added)))))

;; ex. 14.1 p. 496
;; when num-items equals vector length, the procedure enters an infinite loop

;; ex. 14.2 p. 497
