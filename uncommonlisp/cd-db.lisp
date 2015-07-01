(defvar *cd-db* nil)

(defparameter *working-directory* "c:/Users/Heitor/Desktop/emacs-24.3/bin/uncommonlisp/")

(defun dump-db ()
  (dolist (cd *cd-db*)
    (format t "~{~a:~10t~a~%~}~%" cd)))

(defun prompt-read (prompt)
  (format *query-io* "~a: " prompt)
  (force-output *query-io*)
  (read-line *query-io*))

(defun save-db (filename)
  (with-open-file (out (concatenate 'string *working-directory* filename)
                       :direction :output
                       :if-exists :supersede)
    (with-standard-io-syntax
      (print *cd-db* out))))

(defun load-db (filename)
  (with-open-file (in (concatenate 'string *working-directory* filename))
    (with-standard-io-syntax
      (setf *cd-db* (read in)))))

(defun make-cd (title artist rating ripped)
  (list :title title :artist artist :rating rating :ripped ripped))

(defun add-record (cd) (push cd *cd-db*))

;;; unused
(defun select-by-artist (artist)
  (remove-if-not 
   #'(lambda (cd) (equal (getf cd :artist) artist)) 
   *cd-db*))  

(defun select (selector-fn)
  (remove-if-not selector-fn *cd-db*))

(defun make-comparison-expr (field value)
  `(equal (getf cd ,field) ,value))

(defun make-comparisons-list (fields)
  (loop while fields
     collecting (make-comparison-expr (pop fields) (pop fields))))
                  
(defmacro where (&rest clauses)
  `#'(lambda (cd) (and ,@(make-comparisons-list clauses))))

;;;; Zomg 

(defun where-fn (&rest clauses)
  ;; will not work because cd is not a valid reference
  #'(lambda (cd) `(and ,@(make-comparisons-list clauses))))

(defun make-adder (n)
  ;; compiles a lexical closure
  #'(lambda (x) (+ n x)))

(funcall (make-adder 3) 9)
