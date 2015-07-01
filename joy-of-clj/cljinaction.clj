;; p. 63

(defn basic-item-total [price quantity]
  (* price quantity))

(defn with-line-item-conditions [f price quantity]
  {:pre [(> price 0) (> quantity 0)]
   :post [(> % 1)]}
  (apply f (list price quantity)))

(with-line-item-conditions basic-item-total 0.1 200)
