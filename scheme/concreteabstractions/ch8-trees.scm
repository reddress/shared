;; trees p. 216

(define make-empty-tree
  (lambda () '()))

(define make-nonempty-tree
  (lambda (root left-subtree right-subtree)
    (list root left-subtree right-subtree)))

(define empty-tree? null?)

(define root car)

(define left-subtree cadr)

(define right-subtree caddr)

(define in?
  (lambda (value tree)
    (cond
     ((empty-tree? tree) #f)
     ((= value (root tree)) #t)
     ((< value (root tree)) (in? value (left-subtree tree)))
     (else (in? value (right-subtree tree))))))

(define sample-binary-tree
  (lambda ()
    (make-nonempty-tree
     4
     (make-nonempty-tree
      2
      (make-nonempty-tree
       1 (make-empty-tree) (make-empty-tree))
      (make-nonempty-tree
       3 (make-empty-tree) (make-empty-tree)))
     (make-nonempty-tree
      6
      (make-nonempty-tree
       5 (make-empty-tree) (make-empty-tree))
      (make-nonempty-tree
       7 (make-empty-tree) (make-empty-tree))))))

(define partial-binary-tree
  (lambda ()
    (make-nonempty-tree
     4
     (make-nonempty-tree
      2
      (make-nonempty-tree
       1 (make-empty-tree) (make-empty-tree))
      (make-nonempty-tree
       3 (make-empty-tree) (make-empty-tree)))
     (make-nonempty-tree
      6
      (make-nonempty-tree
       5 (make-empty-tree) (make-empty-tree))
      (make-empty-tree)))))

(partial-binary-tree)

;; ex. 8.1 p. 217
(define minimum
  (lambda (binary-tree)
    (if (empty-tree? (left-subtree binary-tree))
        (root binary-tree)
        (minimum (left-subtree binary-tree)))))
(minimum (sample-binary-tree))

;; ex. 8.2 p. 217
(define number-of-nodes
  (lambda (binary-tree)
    (if (empty-tree? binary-tree)
        0
        (+ 1 (number-of-nodes (left-subtree binary-tree))
           (number-of-nodes (right-subtree binary-tree))))))
(number-of-nodes (partial-binary-tree))

(define preorder
  (lambda (tree)
    (if (empty-tree? tree)
        '()
        (cons (root tree)
              (append (preorder (left-subtree tree))
                      (preorder (right-subtree tree)))))))

(preorder (partial-binary-tree))

(partial-binary-tree)

(define offset
  (lambda (amount)
    (if (< amount 0)
        (flush-output)
        (begin
          (display " ")
          (offset (- amount 1))))))

(define display-binary-tree
  (lambda (tree level current-offset)
    (if (empty-tree? tree)
        (flush-output)
        (begin
          (newline)
          (offset current-offset)
          (offset (/ 10 level))
          ;;(display level)
          ;;(display "Root: ")
          (display (root tree))
          (newline)

          (offset current-offset)
          ;;(display level)
          ;;(display "LEFT: ")
          (display-binary-tree (left-subtree tree) (+ 1 level) current-offset)
          ;;(newline)
          (offset current-offset)
          (offset (/ 6 level))
          ;;(display level)
          ;;(display "RIGHT: ")
          (display-binary-tree (right-subtree tree) (+ 1 level) (+ 10 current-offset))))))
(display-binary-tree (sample-binary-tree) 1 0)

(define preorder
  (lambda (tree)
    (preorder-onto tree '())))
(define preorder-onto
  (lambda (tree list)
    (if (empty-tree? tree)
        list
        (cons (root tree)
              (preorder-onto (left-subtree tree)
                             (preorder-onto (right-subtree tree)
                                            list))))))
(preorder (sample-binary-tree))

(define inorder
  (lambda (tree)
    (if (empty-tree? tree)
        '()
        (append (inorder (left-subtree tree))
                (cons (root tree)
                      (inorder (right-subtree tree)))))))
(inorder (partial-binary-tree))

;; ex. 8.4 p. 220
(define inorder-with-onto
  (lambda (tree)
    (inorder-onto tree '())))
(define inorder-onto
  (lambda (tree list)
    (if (empty-tree? tree)
        list
        (inorder-onto (left-subtree tree)
                      (cons (root tree)
                            (inorder-onto (right-subtree tree)
                                          list))))))
(inorder-with-onto (partial-binary-tree))

(sample-binary-tree)

;; ex. 8.6 p. 220
(define insert
  (lambda (value tree)
    (if (empty-tree? tree)
        (make-nonempty-tree value (make-empty-tree) (make-empty-tree))
        (cond ((and (< value (root tree)) (empty-tree? (left-subtree tree)))
               ;;(display "add to left subtree")
               (make-nonempty-tree (root tree)
                                   (make-nonempty-tree value
                                                       (make-empty-tree)
                                                       (make-empty-tree))
                                   (right-subtree tree)))
              ((and (>= value (root tree)) (empty-tree? (right-subtree tree)))
               ;;(display "add to right subtree")
               (make-nonempty-tree (root tree)
                                   (left-subtree tree)
                                   (make-nonempty-tree value
                                                       (make-empty-tree)
                                                       (make-empty-tree))))
              ((< value (root tree))
               (make-nonempty-tree (root tree)
                                   (insert value (left-subtree tree))
                                   (right-subtree tree)))
              ((>= value (root tree))
               (make-nonempty-tree (root tree)
                                   (left-subtree tree)
                                   (insert value (right-subtree tree))))
              (else (display "no condition matches"))))))
(insert 1 (insert 2 (insert 5 (insert 3 (make-empty-tree)))))
(insert 5 (insert 7 (insert 1 (insert 3 (insert 6 (insert 2 (insert 4 (make-empty-tree))))))))
(sample-binary-tree)

;; ex. 8.7 p. 220
(define list->bstree
  (lambda (lst)
    (if (null? lst)
        (make-empty-tree)
        (insert (car lst) (list->bstree (cdr lst))))))
(display-binary-tree (list->bstree '(1 2 3 4 5)) 1 0)
(display-binary-tree (list->bstree '(9 3 4 1 2)) 1 0)
(display-binary-tree (list->bstree '(3 8 2 9 4 10 1 5)) 1 0)
(list->bstree '(3 8 -2 9 4 10 1 5))
(minimum (list->bstree '(3 8 -2 9 4 10 1 5)))
(minimum (sample-binary-tree))

(define height
  (lambda (tree)
    (if (empty-tree? tree)
        -1
        (max (+ 1 (height (left-subtree tree)))
             (+ 1 (height (right-subtree tree)))))))
(height (sample-binary-tree))
(height (list->bstree '(1 2 3 4 5)))
(height (list->bstree '(3 8 2 9 4 10 1 5)))
(display-binary-tree (list->bstree '(3 8 2 9 4 10 1 5)) 1 0)
(list->bstree '(3 8 2 9 4 10 1 5))
(height (make-nonempty-tree 1 (make-nonempty-tree 2 '() '()) '()))

;; 8.3 expression trees p. 227
(define make-constant
  (lambda (x) x))

(define constant? number?)

(define make-expr
  (lambda (left-operand operator right-operand)
    (list left-operand operator right-operand)))

(define operator cadr)
(define left-operand car)
(define right-operand caddr)

(define evaluate
  (lambda (expr)
    (cond ((constant? expr) expr)
          (else ((look-up-value (operator expr))
                 (evaluate (left-operand expr))
                 (evaluate (right-operand expr)))))))
(define look-up-value
  (lambda (name)
    (cond ((equal? name '+) +)
          ((equal? name '*) *)
          ((equal? name '-) -)
          ((equal? name '/) /)
          ((equal? name 'plus) +)
          ((equal? name 'minus) -)
          ((equal? name '^) expt)
          (else (error "unrecognized name" name)))))

(evaluate '(2 ^ 3))
(evaluate '(1 plus (2 * (3 minus 5))))

(evaluate (make-expr 2 '- 9))

(define post-order
  (lambda (tree)
    (define post-order-onto
      (lambda (tree list)
        (if (constant? tree)
            (cons tree list)
            (post-order-onto (left-operand tree)
                             (post-order-onto
                              (right-operand tree)
                              (cons (operator tree) list))))))
    (post-order-onto tree '())))
(post-order '(1 + ((2 * 4) - 3)))
(evaluate '(1 + ((2 * 4) - 3)))

