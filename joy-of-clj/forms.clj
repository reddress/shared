;; what is a form, trebek

(+) ; 0
(/) ; exception
(*) ; 1
(-) ; exception

;; false due to inexact representation
(= 0.3 (+ 0.1 0.1 0.1))

;; big decimal avoids errors due to inexact representation
(= 0.3M (+ 0.1M 0.1M 0.1M))  ; true

;; warning: all arguments must be BigDecimal
(= 0.3M (+ 0.1M 0.1 0.1))  ; false

;; the only thing that is "true?" is true itself
(true? 1) ; false

(true? true)

;; other than false and nil, everything else is boolean true
(if nil 'nil-is-true 'nil-is-false)  ; false

;; however, false? returns true only for false
(false? nil) ; also false

(if false 'true 'false) ; false

(true? ()) ; false

(false? ()) ; false 

(false? false) ; true


;; nil is the same as Java's "null"
