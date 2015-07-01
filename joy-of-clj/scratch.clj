;; prog cloj 2nd p. 3

(defn blank? [str]
  (every? #(Character/isWhitespace %) str))

;; p. 4
(defrecord Person [first last])

(def foo (->Person "Aaron" "Bedra"))

