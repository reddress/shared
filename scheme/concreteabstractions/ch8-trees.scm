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
    (if (and (empty-tree? (left-subtree binary-tree))
             (empty-tree? (right-subtree binary-tree)))
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

(define inorder
  (lambda (tree)
    (if (empty-tree? tree)
        '()
        (append (inorder (left-subtree tree))
                (cons (root tree)
                      (inorder (right-subtree tree)))))))
(inorder (partial-binary-tree))
