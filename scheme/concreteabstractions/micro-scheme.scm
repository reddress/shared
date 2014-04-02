;; This file contains excerpts from the textbook Concrete
;; Abstractions: An Introduction to Computer Science Using Scheme, by
;; Max Hailperin, Barbara Kaiser, and Karl Knight, Copyright (c) 1998
;; by the authors. Full text is available for free at
;; http://www.gustavus.edu/+max/concrete-abstractions.html

;; Before this version of micro-scheme will work, you need to do the
;; following:
;;
;;  (1) Enhance matches? and write substitutions-in-to-match as described
;;      in Section 7.6.
;;
;;  (2) Write all-are from Review Problem 7.49.
;;
;;  (3) Write name? (and keyword?) from Exercise 10.1.

;; Chapter 7: Lists

;; 7.6  An Application: A Movie Query System

(define make-pattern/action
  (lambda (pattern action)
    (cons pattern action)))

(define pattern car)
(define action cdr)

;; The definition of matches? given below (the second one in Chapter 7)
;; will not work for micro-scheme -- you still need to add the _ wildcard,
;; as described in Exercise 7.29.

(define matches?
  (lambda (pattern question)
    (cond ((null? pattern)  (null? question))
          ((null? question) #f)
          ((list? (car pattern))
           (if (member (car question) (car pattern))
               (matches? (cdr pattern)
                         (cdr question))
               #f))
          ((equal? (car pattern) '...) #t)
          ((equal? (car pattern) '_)
           (matches? (cdr pattern) (cdr question)))
          ((equal? (car pattern) (car question))
           (matches? (cdr pattern)
                     (cdr question)))
          (else #f))))
(matches? '(who is the _ _ of _) '(who is the lead actor of casablanca))

(define substitutions-in-to-match
  (lambda (pattern question)
    (define build-substitution-list
      (lambda (pattern question result)
        (if (null? pattern)
            result
            (cond ((equal? (car pattern) '...)
                   (append result (list question)))
                  ((equal? (car pattern) '_)
                   (build-substitution-list (cdr pattern) (cdr question) (append result (list (car question)))))
                  (else
                   (build-substitution-list (cdr pattern) (cdr question) result))))))
    (build-substitution-list pattern question '())))
(substitutions-in-to-match '(foo _ ...) '(foo bar baz bat))

;; Review Problems

(define all-are
  (lambda (predicate)
    (define tester
      (lambda (lst)
        (if (or (null? lst) (not (predicate (car lst))))
            #f
            (if (null? (cdr lst))
                (predicate (car lst))
                (tester (cdr lst))))))
    tester))
((all-are positive?) '(1 2 -3 4 2))
((all-are even?) '(2 4 3 6))


;; Chapter 8: Trees

;; 8.3  Expression Trees

(define look-up-value
  (lambda (name)
    (cond ((equal? name '+) +)
          ((equal? name '*) *)
          ((equal? name '-) -)
          ((equal? name '/) /)
          (else (error "Unrecognized name" name)))))

;; Chapter 10: Implementing Programming Languages

;; 10.2  Syntax


(define keyword?
  (lambda (sym)
    (member sym '(lambda quote if))))

(define name?
  (lambda (sym)
    (and (symbol? sym) (not (keyword? sym)))))
(name? 'iff)


(define syntax-ok?
  (lambda (pmse)
    (define loop
      (lambda (p/a-list)
        (cond ((null? p/a-list) #f)
              ((matches? (pattern (car p/a-list)) pmse)
               (apply (action (car p/a-list))
                      (substitutions-in-to-match (pattern (car p/a-list))
                                                 pmse)))
              (else (loop (cdr p/a-list))))))
    (cond ((or (number? pmse)
               (string? pmse)
               (boolean? pmse))
           #t)
          ((name? pmse) #t)
          ((list? pmse)
           (loop micro-scheme-syntax-ok?-p/a-list))
          (else #f))))

(define micro-scheme-syntax-ok?-p/a-list
  (list
   (make-pattern/action '(if _ _ _)
                        (lambda (test if-true if-false)
                          (and (syntax-ok? test)
                               (syntax-ok? if-true)
                               (syntax-ok? if-false))))
   (make-pattern/action '(lambda _ _)
                        (lambda (parameters body)
                          (and (list? parameters)
                               ((all-are name?) parameters)
                               (syntax-ok? body))))
   (make-pattern/action '(quote _)
                        (lambda (datum) #t))
   (make-pattern/action '(...)  ;; must come last
                        (lambda (pmses)
                          ((all-are syntax-ok?) pmses)))))

(syntax-ok? '())

;; 10.3  Micro-Scheme

(define read-eval-print-loop
  (lambda ()
    (display ";Enter Micro-Scheme expression:")
    (newline)
    (flush-output)
    (let ((expression (read)))
      (let ((value (evaluate (parse expression))))
        (display ";Micro-Scheme value: ")
        (write value)
        (newline)
        (flush-output)))
    (read-eval-print-loop)))

(define parse
  (lambda (expression)
    (define loop
      (lambda (p/a-list)
        (cond ((null? p/a-list)
               (error "invalid expression in p/a list" expression))
              ((matches? (pattern (car p/a-list)) expression)
               (apply (action (car p/a-list))
                      (substitutions-in-to-match
                       (pattern (car p/a-list))
                       expression)))
              (else (loop (cdr p/a-list)))))) ;end of loop
    (cond ((name? expression) ;start of main parse procedure
           (make-name-ast expression))
          ((or (number? expression)
               (string? expression)
               (boolean? expression))
           (make-constant-ast expression))
          ((list? expression)
           (loop micro-scheme-parsing-p/a-list))
          (else (error "invalid expression in main parse" expression)))))
	   
(define micro-scheme-parsing-p/a-list
  (list
   (make-pattern/action '(if _ _ _)
                        (lambda (test if-true if-false)
                          (make-conditional-ast (parse test)
                                                (parse if-true)
                                                (parse if-false))))
   (make-pattern/action '(lambda _ _)
                        (lambda (parameters body)
                          (if (and (list? parameters)
                                   ((all-are name?) parameters))  
                              (make-abstraction-ast parameters
                                                    (parse body))
                              (error "invalid expression"
                                     (list 'lambda
                                           parameters body)))))
   (make-pattern/action '(quote _)
                        (lambda (value)
                          (make-constant-ast value)))
   (make-pattern/action '(...)   ; note that this *must* come last
                        (lambda (operator&operands)
                          (let ((asts (map parse
                                           operator&operands)))
                            (make-application-ast (car asts)
                                                  (cdr asts)))))))

(define evaluate
  (lambda (ast)
    (ast 'evaluate)))

(define substitute-for-in
  (lambda (value name ast)
    ((ast 'substitute-for) value name)))

(define make-name-ast
  (lambda (name)
    (define the-ast
      (lambda (message)
        (cond ((equal? message 'evaluate) (look-up-value name))
              ((equal? message 'substitute-for)
               (lambda (value name-to-substitute-for)
                 (if (equal? name name-to-substitute-for)
                     (make-constant-ast value)
                     the-ast)))
              (else (error "unknown operation on a name AST"
                           message)))))
    the-ast))

(define make-constant-ast
  (lambda (value)
    (define the-ast
      (lambda (message)
        (cond ((equal? message 'evaluate) value)
              ((equal? message 'substitute-for)
               (lambda (value name)
                 the-ast))
              (else (error "unknown operation on a constant AST"
                           message)))))
    the-ast))

(define make-conditional-ast
  (lambda (test-ast if-true-ast if-false-ast)
    (lambda (message)
      (cond ((equal? message 'evaluate)
             (if (evaluate test-ast)
                 (evaluate if-true-ast)
                 (evaluate if-false-ast)))
            ((equal? message 'substitute-for)
             (lambda (value name)
               (make-conditional-ast
                (substitute-for-in value name test-ast)
                (substitute-for-in value name if-true-ast)
                (substitute-for-in value name if-false-ast))))
            (else (error "unknown operation on a conditional AST"
                         message))))))

(define make-application-ast
  (lambda (operator-ast operand-asts)
    (lambda (message)
      (cond ((equal? message 'evaluate)
             (let ((procedure (evaluate operator-ast))
                   (arguments (map evaluate operand-asts)))
               (apply procedure arguments)))
            ((equal? message 'substitute-for)
             (lambda (value name)
               (make-application-ast
                (substitute-for-in value name operator-ast)
                (map (lambda (operand-ast)
                       (substitute-for-in value name operand-ast))
                     operand-asts))))
            (else (error "unknown operation on an application AST"
                         message))))))

(define make-abstraction-ast
  (lambda (parameters body-ast)
    (define the-ast
      (lambda (message)
        (cond ((equal? message 'evaluate)
               (make-procedure parameters body-ast))
              ((equal? message 'substitute-for)
               (lambda (value name)
                 (if (member name parameters)
                     the-ast
                     (make-abstraction-ast
                      parameters
                      (substitute-for-in value name body-ast)))))
              (else (error "unknown operation on an abstraction AST"
                           message)))))
    the-ast))

(define make-procedure
  (lambda (parameters body-ast)
    (lambda arguments
      (define loop
        (lambda (parameters arguments body-ast)
          (cond ((null? parameters)
                 (if (null? arguments)
                     (evaluate body-ast)
                     (error "too many arguments")))
                ((null? arguments)
                 (error "too few arguments"))
                (else
                 (loop (cdr parameters) (cdr arguments)
                       (substitute-for-in (car arguments)
                                          (car parameters)
                                          body-ast))))))
      (loop parameters arguments body-ast))))

(read-eval-print-loop)
