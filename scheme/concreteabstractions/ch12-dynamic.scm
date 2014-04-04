(define walk-count
  (lambda (feet)
    (cond ((= feet 0) 1)
          ((= feet 1) 1)
          (else (+ (walk-count (- feet 1))
                   (walk-count (- feet 2)))))))

(define walk-count
  (lambda (n)
    (cond ((= n 0) 1)
          ((= n 1) 1)
          (else (+ (walk-count-subproblem (- n 1))
                   (walk-count-subproblem (- n 2)))))))

(define memoized-walk-count
  (lambda (n)
    (let ((table (make-vector n)))
      (vector-fill! table #f)
      (define ensure-in-table!
        (lambda (n)
          (if (vector-ref table n)
              'done
              (store-into-table! n))))
      (define store-into-table!
        (lambda (n)
          (vector-set! table n (walk-count n))))
      (define walk-count-subproblem
        (lambda (n)
          (ensure-in-table! n)
          (vector-ref table n)))
      (define walk-count
        (lambda (n)
          (cond ((= n 0) 1)
                ((= n 1) 1)
                (else (+ (walk-count-subproblem (- n 1))
                         (walk-count-subproblem (- n 2)))))))
      (walk-count n))))
(memoized-walk-count 30)

;; ex. 12.1 p. 385
(define my-vector-fill!
  (lambda (vec val)
    (define set-current-index
      (lambda (i)
        (if (< i (vector-length vec))
            (begin
              (vector-set! vec i val)
              (set-current-index (+ 1 i))))))
    (set-current-index 0)))
(define v (make-vector 5))
(my-vector-fill! v 9)
v

(define dp-walk-count
  (lambda (n)
    (let ((table (make-vector n)))
      (define walk-count
        (lambda (n)
          (cond ((= n 0) 1)
                ((= n 1) 1)
                (else (+ (walk-count-subproblem (- n 1))
                         (walk-count-subproblem (- n 2)))))))
      (define walk-count-subproblem
        (lambda (n)
          (vector-ref table n)))
      (define store-into-table!
        (lambda (n)
          (vector-set! table n (walk-count n))))
      (define store-into-table-from!
        (lambda (start)
          (if (= start n)
              'done
              (begin
                (store-into-table! start)
                (store-into-table-from! (+ start 1))))))
      (store-into-table-from! 0)
      (walk-count n))))
(dp-walk-count 30)
;; key observation: storing the values into the vector is very much like the
;; procedure my-vector-fill!

(define from-to-do
  (lambda (start stop body)
    (if (> start stop)
        'done
        (begin (body start)
               (from-to-do (+ 1 start) stop body)))))
(define dp-walk-count-2
  (lambda (n)
    (let ((table (make-vector n)))
      (define walk-count
        (lambda (n)
          (cond ((= n 0) 1)
                ((= n 1) 1)
                (else (+ (walk-count-subproblem (- n 1))
                         (walk-count-subproblem (- n 2)))))))
      (define walk-count-subproblem
        (lambda (n)
          (vector-ref table n)))
      (define store-into-table!
        (lambda (n)
          (vector-set! table n (walk-count n))))
      (from-to-do 0 (- n 1) store-into-table!)
      (walk-count n))))
(dp-walk-count-2 30)

(define choose
  (lambda (n k)
    (cond ((= n k) 1)
          ((= k 0) 1)
          (else (+ (choose (- n 1) (- k 1))
                   (choose (- n 1) k))))))
(choose 3 3)

(define make-chocolate
  (lambda (filling covering weight desirability)
    (list filling covering weight desirability)))
(define chocolate-filling car)
(define chocolate-covering cadr)
(define chocolate-weight caddr)
(define chocolate-desirability cadddr)

(define make-empty-box
  (lambda ()
    (list '() 0 0)))
(define box-chocolates car)
(define box-weight cadr)
(define box-desirability caddr)

(define add-chocolate-to-box
  (lambda (choc box)
    (list (cons choc (box-chocolates box))
          (+ (chocolate-weight choc)
             (box-weight box))
          (+ (chocolate-desirability choc)
             (box-desirability box)))))

;; ex. 12.9 p. 395
(define better-box
  (lambda (my-box your-box)
    (if (> (box-desirability my-box) (box-desirability your-box))
        my-box
        your-box)))
(better-box (add-chocolate-to-box (make-chocolate 'f 'c 1 14) (make-empty-box))
            (add-chocolate-to-box (make-chocolate 'f 'c 1 20) (make-empty-box)))

(define pick-chocolates
  (lambda (chocolates weight-limit)
    (cond ((null? chocolates) (make-empty-box))
          ((= weight-limit 0) (make-empty-box))
          ((> (chocolate-weight (car chocolates)) ; first too heavy
              weight-limit)
           (pick-chocolates (cdr chocolates) weight-limit))
          (else
           (better-box
            (pick-chocolates (cdr chocolates) ; none of the first kind
                             weight-limit)
            (add-chocolate-to-box
             (car chocolates)  ; at least one of the first kind
             (pick-chocolates chocolates
                              (- weight-limit
                                 (chocolate-weight (car chocolates))))))))))
