;; estimate pi by inscribing polygons with number of sides that are powers of 2

(define (square x) (* x x))

(define (pow base n)
  (if (= n 0)
      1
      (* base (pow base (- n 1)))))

(define (estimate-pi steps)
  (iterate-side (sqrt 2) (/ (sqrt 2) 2) 2 steps))

(define (iterate-side s c iterations steps)
  (cond ((= steps 0)
         (list (* (pow 2 (- iterations 1)) s) s c))
        (else
         (let ((s1 (sqrt (+ (square (- 1 c)) (square (/ s 2))))))
           (iterate-side s1
                         (sqrt (- 1 (/ (square s1) 4)))
                         (+ 1 iterations) (- steps 1))))))
