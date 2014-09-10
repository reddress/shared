(define elephant-file "C:/users/heitor/desktop/emacs-24.3/bin/shared/scheme/elephant/elephantdb.scm")

(define plaintext "C:/users/heitor/desktop/emacs-24.3/bin/shared/scheme/elephant/plain.txt")

(define elephant-list '())

(define write-elephant-list
  (lambda ()
    (with-output-to-file elephant-file
      (lambda ()
        (format #t "~s" elephant-list)))))

(define read-elephant-list
  (lambda ()
    (with-input-from-file elephant-file
      (lambda ()
        (read-line)))))

(define elephant-list (with-input-from-string (read-elephant-list)
                        (lambda () (eval (quote (read))))))

(define first car)

(define second
  (lambda (lst)
    (car (cdr lst))))

(define rest cdr)

(define length
  (lambda (lst)
    (if (null? lst)
        0
        (+ 1 (length (rest lst))))))

(define nth
  (lambda (lst i)
    (cond ((= i 0)
           (first lst))
          ((> i (- (length lst) 1))
           '())
          (else
           (nth (rest lst) (- i 1))))))

(define empty? null?)

(define (append-element-to-list elt lst)
  (if (empty? lst)
      (list elt)
      (cons (first lst) (append-element-to-list elt (rest lst)))))

(define new-entry
  (lambda (tags text)
    (cons tags text)))

(define add-entry
  (lambda (tags text)
    (set! elephant-list
      (append-element-to-list (new-entry tags text) elephant-list))))

(define empty-list
  (lambda ()
    (set! elephant-list '())))

(define show
  (lambda ()
    elephant-list))

(define element-in
  (lambda (elt lst)
    (cond ((empty? lst)
           #f)
          ((equal? elt (first lst))
           #t)
          (else
           (element-in elt (rest lst))))))

(define is-tagged
  (lambda (entry tag)
    (element-in tag entry)))

(define filter-match
  (lambda (lst tag)
    (if (empty? lst)
        '()
        (if (is-tagged (first lst) tag)
            (cons (first lst) (filter-match (rest lst) tag))
            (filter-match (rest lst) tag)))))

(define find-tagged
  (lambda (tag)
    (filter-match elephant-list tag)))
