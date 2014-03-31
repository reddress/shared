 (define working-folder "/home/heitor/shared/scheme/concreteabstractions/")

;; redefine for windows
(when (equal? (build-platform) 'mingw32)
      (define working-folder "C:/Users/Heitor/Desktop/emacs-24.3/bin/shared/scheme/concreteabstractions/"))

(define (my-load file)
  (load (string-append working-folder file)))

(my-load "library.scm")
(my-load "movie.scm")

(define filter
  (lambda (ok? lst)
    (cond ((null? lst)
           '())
          ((ok? (car lst))
           (cons (car lst) (filter ok? (cdr lst))))
          (else
           (filter ok? (cdr lst))))))

(filter odd? (integers-from-to 1 15))

(define first-elements-of
  (lambda (n lst)
    (if (= n 0)
        '()
        (cons (car lst)
              (first-elements-of (- n 1) (cdr lst))))))

;; ex. 7.10 p. 176
(define my-list-tail
  (lambda (lst n)
    (if (= n 0)
        lst
        (my-list-tail (cdr lst) (- n 1)))))
(my-list-tail '(1 2 3 4 5) 2)

;; p. 176
(define interleave
  (lambda (lst1 lst2)
    (if (null? lst1)
        lst2
        (cons (car lst1)
              (interleave lst2 (cdr lst1))))))

(interleave '(1 2 3 4 5 6 7 8 9) '(a b c d e f))

(define shuffle
  (lambda (deck size)
    (let ((half (quotient (+ size 1) 2)))
      (interleave (first-elements-of half deck)
                  (list-tail deck half)))))

(define multiple-shuffle
  (lambda (deck size times)
    (if (= times 0)
        deck
        (multiple-shuffle (shuffle deck size) size (- times 1)))))
(multiple-shuffle (integers-from-to 1 52) 52 8)

;; ex. 7.11
(define in-order?
  (lambda (lst)
    (if (null? (cdr lst))
        #t
        (if (= (+ (car lst) 1) (car (cdr lst)))
            (in-order? (cdr lst))
            #f))))
(in-order? '(1 2 3 4))

(define shuffle-number
  (lambda (n)
    (let ((deck (integers-from-to 1 n)))
      (define count-shuffles
        (lambda (i)
          (if (in-order? (multiple-shuffle deck n i))
              i
              (count-shuffles (+ 1 i)))))
      (count-shuffles 1))))
(shuffle-number 9)

;; ex. 7.12
(define make-deck
  (lambda (lst n)
    (cons lst n)))
(define deck-list
  (lambda (deck)
    (car deck)))
(define deck-length
  (lambda (deck)
    (cdr deck)))
(deck-length (make-deck '(1 2 3) 3))
(deck-list (make-deck '(1 2 3) 3))

;; tag-map
(map shuffle-number (filter even? (integers-from-to 1 52)))

;; ex. 7.13
(define first-n-squares
  (lambda (n)
    (map (lambda (x) (* x x)) (integers-from-to 1 n))))
(first-n-squares 9)

(define first-n-of-fn
  (lambda (n fn)
    (map fn (integers-from-to 1 n))))

(define first-n-even
  (lambda (n)
    (first-n-of-fn n (lambda (x) (* 2 x)))))
(first-n-even 9)

(define repeat-7
  (lambda (n)
    (first-n-of-fn n (lambda (x) 7))))
(repeat-7 5)

(define list-of-lists
  (lambda (lst)
    (map (lambda (n) (integers-from-to 1 n)) lst)))
(list-of-lists '(1 5 3))

;; ex. 7.14
(define my-map
  (lambda (fn lst)
    (if (null? lst)
        '()
        (cons (fn (car lst)) (my-map fn (cdr lst))))))
(my-map (lambda (x) (+ x 10)) '(1 2 3))

(define add-to-end
  (lambda (lst elt)
    (if (null? lst)
        (cons elt '())
        (cons (car lst)
              (add-to-end (cdr lst)
                          elt)))))
(add-to-end '(1 2 3) 4)

(define slow-reverse
  (lambda (lst)
    (if (null? lst)
        '()
        (add-to-end (slow-reverse (cdr lst))
                    (car lst)))))
(slow-reverse '(1 2 3 4 5))

(define iter-reverse
  (lambda (lst)
    (define reverse-onto
      (lambda (from to)
        (if (null? from)
            to
            (reverse-onto (cdr from)
                          (cons (car from) to)))))
    (reverse-onto lst '())))
(iter-reverse '(1 2 3 4))

(define palindrome?
  (lambda (lst)
    (equal? lst (reverse lst))))
(palindrome? '(m a d a m i m a d a m))

(define merge-sort
  (lambda (lst)
    (cond ((null? lst)
           '())
          ((null? (cdr lst))
           lst)
          (else
           (merge (merge-sort (one-part lst))
                  (merge-sort (the-other-part lst)))))))

(define merge
  (lambda (lst1 lst2)
    (cond ((null? lst1) lst2)
          ((null? lst2) lst1)
          ((< (car lst1) (car lst2))
           (cons (car lst1) (merge (cdr lst1) lst2)))
          (else
           (cons (car lst2) (merge lst1 (cdr lst2)))))))

(merge '( 3 5 8 9) '(1 2 3 4 7))

(define odd-part
  (lambda (lst)
    (if (null? lst)
        '()
        (cons (car lst) (even-part (cdr lst))))))
(define even-part
  (lambda (lst)
    (if (null? lst)
        '()
        (odd-part (cdr lst)))))

(odd-part (odd-part '(1 2 3 4 5)))
(define one-part odd-part)
(define the-other-part even-part)

(merge-sort '( 4 28 1 4 2 19 33 129 3 29 45))

;; ex. 7.15 p. 186
(define count-combos
  (lambda (prize-list amount)
    (cond ((< amount 0)
           0)
          ((= amount 0)
           1)
          ((null? prize-list)
           0)
          (else
           (+ (count-combos prize-list (- amount (car prize-list)))
           (count-combos (cdr prize-list) amount))))))
(count-combos '(1 1 3 5) 4)

;; ex. 7.16, 7.17 p. 186
;; '((10 9) (9 3) (8 2) (7 4) (6 3) (5 4) (4 3) (3 3) (2 4) (1 2))
(define repeat
  (lambda (value times)
    (if (= 0 times)
        '()
        (cons value (repeat value (- times 1))))))

(define get-prize-list
  (lambda (table)
    (define build-list
      (lambda (result current-value-pair remaining-values)
        (if (and (null? remaining-values) (= 0 (cadr current-value-pair)))
            result
            (let ((current-value (car current-value-pair))
                  (current-value-number (cadr current-value-pair)))
              (if (= current-value-number 0)
                  (build-list result (car remaining-values)
                              (cdr remaining-values))
                  (build-list (cons current-value result)
                              (list current-value (- current-value-number 1))
                              remaining-values))))))
    (build-list '() (car table) (cdr table))))
(count-combos (get-prize-list '((10 9) (9 3) (8 2) (7 4) (6 3) (5 4) (4 3) (3 3) (2 4) (1 2))) 10)

;; ex. 7.23 p. 190
(define titles-of-movies-satisfying
  (lambda (db predicate)
    (map movie-title
         (filter predicate db))))

(titles-of-movies-satisfying our-movie-database
                             (lambda (movie)
                               (= (movie-year-made movie)
                                  1991)))

;; ex. 7.24 p. 190
(define movies-satisfying
  (lambda (db predicate selector)
    (map selector
         (filter predicate db))))
(movies-satisfying our-movie-database
                   (lambda (movie)
                     (member 'fellini (movie-director movie)))
                   (lambda (movie) (cons (movie-title movie) (movie-director movie))))

;; ex. 7.48 p. 207
(define sub1-each
  (lambda (nums)
    (define help
      (lambda (nums results)
        (if (null? nums)
            (reverse results)
            (help (cdr nums)
                  (cons (- (car nums) 1) results)))))
    (help nums '())))
(sub1-each '(3 6 9))

;; ex. 7.49 p. 208
(define all-are
  (lambda (predicate)
    (define tester
      (lambda (lst)
        (cond ((null? lst) #f)  ;; empty list
              ((null? (cdr lst))
               (predicate (car lst)))  ;; one element
              ((predicate (car lst))
               (tester (cdr lst)))
              (else #f))))
    tester))
((all-are even?) '(2 50 92 2))

