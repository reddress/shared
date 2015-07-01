;;; generate 3x3 magic squares that add to 15

;;; return a list with elt removed
(defun remainder (lst elt)
  (if (null lst)
      '()
      (if (equal elt (car lst))
          (remainder (cdr lst) elt)
          (cons (car lst) (remainder (cdr lst) elt)))))

;;; return a list of lists of permutations
(defun permute (lst)
  (cond ((null (cdr lst)) (list lst))  ; base case, a list of one element
        (t (let ((result nil))
             (dolist (fixed-element lst)  ; loop through single elements
               ;; for each of the fixed elements, append it to
               ;; each of the remainder's permutations
               (let ((remainder-permuted (permute (remainder lst fixed-element))))
                 (dolist (remainder-permutation remainder-permuted)
                   (push (cons fixed-element remainder-permutation)
                         result))))
             result))))

;;; represent a 3x3 square as a list of nine elements
;;; A B C
;;; D E F
;;; G H I
;;; as (A B C D E F G H I)

(defun elements-of-ms (indices magic-square)
  (let ((result '()))
    (dolist (index indices)
      (push (nth index magic-square) result))
    result))

(defun check-sums (magic-square sum)
  (and (= sum (apply #'+ (elements-of-ms '(0 1 2) magic-square)))  ; horiz
       (= sum (apply #'+ (elements-of-ms '(3 4 5) magic-square)))
       (= sum (apply #'+ (elements-of-ms '(6 7 8) magic-square)))
       
       (= sum (apply #'+ (elements-of-ms '(0 3 6) magic-square)))  ; vertical
       (= sum (apply #'+ (elements-of-ms '(1 4 7) magic-square)))
       (= sum (apply #'+ (elements-of-ms '(2 5 8) magic-square)))
       
       (= sum (apply #'+ (elements-of-ms '(0 4 8) magic-square)))  ; diagonals
       (= sum (apply #'+ (elements-of-ms '(2 4 6) magic-square)))))

(defun pprint-square (magic-square)
  (format t "~a ~a ~a~%" (nth 0 magic-square) (nth 1 magic-square) (nth 2 magic-square))
  (format t "~a ~a ~a~%" (nth 3 magic-square) (nth 4 magic-square) (nth 5 magic-square))
  (format t "~a ~a ~a~%~%" (nth 6 magic-square) (nth 7 magic-square) (nth 8 magic-square)))

(defun check-sums-4x4 (magic-square sum)
  (and (= sum (apply #'+ (elements-of-ms '(0 1 2 3) magic-square)))  ; horiz
       (= sum (apply #'+ (elements-of-ms '(4 5 6 7) magic-square)))
       (= sum (apply #'+ (elements-of-ms '(8 9 10 11) magic-square)))
       (= sum (apply #'+ (elements-of-ms '(12 13 14 15) magic-square)))
       
       (= sum (apply #'+ (elements-of-ms '(0 4 8 12) magic-square)))  ; vertical
       (= sum (apply #'+ (elements-of-ms '(1 5 9 13) magic-square)))
       (= sum (apply #'+ (elements-of-ms '(2 6 10 14) magic-square)))
       (= sum (apply #'+ (elements-of-ms '(3 7 11 15) magic-square)))
       
       (= sum (apply #'+ (elements-of-ms '(0 5 10 15) magic-square)))  ; diagonals
       (= sum (apply #'+ (elements-of-ms '(3 6 9 12) magic-square)))))

(defun pprint-magic-square-4x4 (magic-square)
  (format t "~a ~a ~a ~a~%" (nth 0 magic-square) (nth 1 magic-square) (nth 2 magic-square) (nth 3 magic-square))
  (format t "~a ~a ~a ~a~%" (nth 4 magic-square) (nth 5 magic-square) (nth 6 magic-square) (nth 7 magic-square))
  (format t "~a ~a ~a ~a~%" (nth 8 magic-square) (nth 9 magic-square) (nth 10 magic-square) (nth 11 magic-square))
  (format t "~a ~a ~a ~a~%~%" (nth 12 magic-square) (nth 13 magic-square) (nth 14 magic-square) (nth 15 magic-square)))

;;; brute force solutions
(defun brute-force-magic-squares ()
  (let ((combinations (permute '(1 2 3 4 5 6 7 8 9))))
    (dolist (square combinations)
      (when (check-sums square 15)
        (pprint-square square)))
    'END--BRUTE-FORCE-MAGIC-SQUARES))

;;; too many combinations
;; (defun brute-force-4x4 ()
;;  (let ((combinations (permute '(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16))))
;;    (dolist (magic-square combinations)
;;      (when (check-sums-4x4 magic-square 34)
;;        (pprint-magic-square-4x4 magic-square)))))

;;; https://en.wikipedia.org/?title=Magic_square
;;; indian Parshvanath Jain temple
(check-sums-4x4 '(7 12 1 14
                  2 13 8 11
                  16 3 10 5
                  9 6 15 4) 34)

;;; Durer 
(check-sums-4x4 '(16 3 2 13
                  5 10 11 8
                  9 6 7 12
                  4 15 14 1) 34)

;;; Sagrada Familia, 14 and 10 repeated
(check-sums-4x4 '(1 14 14 4
                  11 7 6 9
                  8 10 10 5
                  13 2 3 15) 33)
