;;;; Copy and save changes to c:/Users/Heitor/ccl-init.lisp

(defun my-first-util ()
  (format t "My first util"))

;;; On Lisp p. 47
(defun filter (fn lst)
  (let ((acc nil))
    (dolist (x lst)
      (let ((val (funcall fn x)))
        (if val (push val acc))))
    (nreverse acc)))

;;; On Lisp p. 47
(defun group (source n)
  (if (zerop n) (error "n cannot be of zero length"))
  (labels ((rec (source acc)
             (let ((rest (nthcdr n source)))
               (if (consp rest)
                   (rec rest (cons (subseq source 0 n) acc))
                   (nreverse (cons source acc))))))
    (if source (rec source nil) nil)))

;;; p. 49
(defun flatten (x)
  (labels ((rec (x acc)
             (cond ((null x) acc)
                   ((atom x) (cons x acc))
                   (t (rec (car x) (rec (cdr x) acc))))))
    (rec x nil)))

(defun my-flatten (input)
  (labels ((rec (lst acc)
             (if (null lst)
                 (nreverse acc)
                 (if (atom (car lst))
                     (rec (cdr lst) (cons (car lst) acc))
                     (rec (append (car lst) (cdr lst)) acc)))))
    (rec input '())))

(defun my-flatten2 (input)
  (labels ((rec (lst acc)
             (cond ((null lst) (nreverse acc))
                   ;; remove occurrences of the empty list
                   ((and (atom (car lst)) (not (null (car lst))))
                    (rec (cdr lst) (cons (car lst) acc)))
                   (t (rec (append (car lst) (cdr lst)) acc)))))
    (rec input '())))

(defun prune (test tree)
  (labels ((rec (tree acc)
             (cond ((null tree) (nreverse acc))
                   ((consp (car tree))
                    (rec (cdr tree)
                         (cons (rec (car tree) nil) acc)))
                   (t (rec (cdr tree)
                           (if (funcall test (car tree))
                               acc
                               (cons (car tree) acc)))))))
    (rec tree nil)))

;;; repeat an element n times
(defun repeat (elt n)
  (if (< n 1)
      '()
      (cons elt (repeat elt (- n 1)))))

;;; range from a (included) to b (not included), like Python
(defun range-py (a b)
  (if (>= a b)
      '()
      (cons a (range-py (+ 1 a) b))))

;;; range from a (included) to b (included)
(defun range-ab-incl (a b)
  (if (> a b)
      '()
      (cons a (range-ab-incl (+ 1 a) b))))
