;; ex. 10.1 p. 283
(define keyword?
  (lambda (sym)
    (member sym '(lambda quote if))))

(define name?
  (lambda (sym)
    (and (symbol? sym) (not (keyword? sym)))))
(name? 'iff)

;; see file micro-scheme.scm
