;; COPIED TO GIT REPO "SHARED"

;; count how many 50s, 20s, 10s, 5s, 2s bills and 1 coins are needed
;; to pay everyone's salary

(def bills [50 20 10 5 2 1])

(defn largest-for [amount denominations]
  (if (<= (first denominations) amount)
    (first denominations)
    (largest-for amount (rest denominations))))

(largest-for 100 bills)  ;; should return 50

(largest-for 39 bills) ;; should return 20


(defn bills-for-amount [amount bill-count]
  (if (= amount 0)
    bill-count
    (let [largest (largest-for amount bills)]
      (bills-for-amount (- amount largest) (cons largest bill-count)))))


;; should return {:50 2, :20 1, :10 0, :5 1, :2 2, :1 0}
(bills-for-amount 129 ())

(defn bills-for-group [amount-list bill-count]
  (if (empty? amount-list)
    (flatten bill-count)
    (bills-for-group (rest amount-list) (cons (bills-for-amount (first amount-list) ()) bill-count))))

;; should return [50 50 20 5 2 2 20 10 5]: 50 x2, 20 x2, 10 x1, 5 x2, 2 x2
(bills-for-group [129 35] ())

(defn consolidate
  "Given a list of bills, create a histogram counting how many of each
  bill is needed"
  [bill-list bill-map]
  (if (empty? bill-list)
    bill-map
    ;; while there are items in the bill list, increase the map's count
    (consolidate (rest bill-list) (assoc bill-map (first bill-list) (+ 1 (bill-map (first bill-list)))))))
