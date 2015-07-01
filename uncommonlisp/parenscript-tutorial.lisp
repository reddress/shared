(load "C:/users/heitor/quicklisp/setup.lisp")

(push :hunchentoot-no-ssl *features*)

(dolist (x '(:hunchentoot :cl-who :parenscript :cl-fad))
  (ql:quickload x))

(defpackage :ps-tutorial
  (:use :common-lisp :hunchentoot :cl-who :parenscript :cl-fad))

(in-package :ps-tutorial)

(setf *js-string-delimiter* #\")

(start (make-instance 'easy-acceptor :port 8083))

(define-easy-handler (tutorial :uri "/tutorial1") ()
  (with-html-output-to-string (s)
    (:html
     (:head (:title "Parenscript tutorial 1"))
     (:body (:h2 "tutorial")
            "click the link" :br
            (:a :href "#" :onclick (ps (alert "Hello"))
                "Hello world")))))
