;; copy sidebars p. 144, p. 152
(define play-with-turns
  (lambda (game-state player computer-strategy)
    (display-game-state game-state)
    (cond ((over? game-state)
           (announce-winner player))
          ((equal? player 'human)
           (play-with-turns (human-move game-state) 'computer computer-strategy))
          ((equal? player 'noob)
           (play-with-turns (noob-move game-state) 'computer computer-strategy))
          ((equal? player 'computer)
           ;; (play-with-turns (computer-move game-state computer-strategy) 'human computer-strategy))
           (play-with-turns (computer-move game-state computer-strategy) 'noob computer-strategy))
          (else
           (error "Player unknown:" player)))))

(define computer-move
  (lambda (game-state strategy)
    ;; (let ((pile (if (> (size-of-pile game-state 1) 0)
    ;;                    1
    ;;                    2)))
    ;; (display "I take one coin from pile ")
    ;;  (display pile)
    ;;  (newline)
    ;;  (flush-output)
    ;; (remove-coins-from-pile game-state 1 pile))))
    ;;  (next-game-state game-state (make-move-instruction 1 pile)))))
    (prompt "Enter something to compute CPU strategy.")
    (next-game-state game-state (strategy game-state))))

(define noob-move
  (lambda (game-state)
    (prompt "Enter something for noob move.")
    (next-game-state game-state (take-one-from-random-pile game-state))))

(define prompt
  (lambda (prompt-string)
    (newline)
    (display prompt-string)
    (newline)
    (flush-output)
    (read)))

(define human-move
  (lambda (game-state)
    (let ((p (prompt "Which pile?")))
      (let ((n (prompt "How many coins?")))
        ;; (remove-coins-from-pile game-state n p)))))
        (next-game-state game-state (make-move-instruction n p))))))

(define over?
  (lambda (game-state)
    (= (total-size game-state) 0)))

(define announce-winner
  (lambda (player)
    (if (equal? player 'human)
        (display "Player 1 wins!")
        (display "Player 2 wins!"))
    (newline)
    (flush-output)))

(define make-game-state
  (lambda (n m) (cons n m)))

(define size-of-pile
  (lambda (game-state pile-number)
    (if (= pile-number 1)
        (car game-state)
        (cdr game-state))))

(define remove-coins-from-pile
  (lambda (game-state num-coins pile-number)
    (if (= pile-number 1)
        (make-game-state (- (size-of-pile game-state 1)
                            num-coins)
                         (size-of-pile game-state 2))
        (make-game-state (size-of-pile game-state 1)
                         (- (size-of-pile game-state 2)
                            num-coins)))))

(define display-game-state
  (lambda (game-state)
    (newline)
    (newline)
    (display "    Pile 1: ")
    (display (size-of-pile game-state 1))
    (newline)
    (display "    Pile 2: ")
    (display (size-of-pile game-state 2))
    (newline)
    (newline)
    (flush-output)))

(define total-size
  (lambda (game-state)
    (+ (size-of-pile game-state 1)
       (size-of-pile game-state 2))))

(define start-nim
  (lambda (game-state strategy)
    ;;(play-with-turns game-state 'human strategy)))
    (play-with-turns game-state 'noob strategy)))

;; (define noob-vs-cpu
;;  (lambda (game-state strategy)
;;    (

(define make-move-instruction
  (lambda (coins pile)
    (display "Remove ")
    (display coins)
    (display " coins from pile ")
    (display pile)
    (newline)
    (flush-output)
    (cons coins pile)))

(define coins-from-instruction
  (lambda (move-instr)
    (car move-instr)))

(define pile-from-instruction
  (lambda (move-instr)
    (cdr move-instr)))

(define println
  (lambda (str)
    (display str)
    (newline)
    (flush-output)))

(define next-game-state
  (lambda (game-state move-instr)
    (println "next-game-state")
    (remove-coins-from-pile game-state
                            (coins-from-instruction move-instr)
                            (pile-from-instruction move-instr))))

(define simple-strategy
  (lambda (game-state)
    (println "simple-strategy")
    (if (> (size-of-pile game-state 1) 0)
        (make-move-instruction 1 1)
        (make-move-instruction 1 2))))

(define all-your-coin-are-belong-to-us
  (lambda (game-state)
    (println "all-your-coin")
    (let ((size-of-pile-1 (size-of-pile game-state 1))
          (size-of-pile-2 (size-of-pile game-state 2)))
      (if (> size-of-pile-1 0)
          (make-move-instruction size-of-pile-1 1)
          (make-move-instruction size-of-pile-2 2)))))

(define take-one-from-random-pile
  (lambda (game-state)
    (println "random pile")
    (let ((pile (if (= (size-of-pile game-state 1) 0)
                    2
                    (if (= (size-of-pile game-state 2) 0)
                        1
                        (+ 1 (random 2))))))
      (make-move-instruction 1 pile))))

(define pwn-strategy
  (lambda (game-state)
    (println "i pwn j00")
    (let ((x (size-of-pile game-state 1))
          (y (size-of-pile game-state 2)))
      (if (= x y)
          (begin
            (println "o noes")
            (take-one-from-random-pile game-state))
          (make-move-instruction (abs (- x y)) (if (> x y)
                                                   1
                                                   2))))))
