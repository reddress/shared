;; user-defined functions

(defn greeting
  "Returns a greeting addressed to the given name"
  [username]
  (str "Hello, " username))

(greeting "Joe")

;; p. 49

(defn indexed [coll] (map-indexed vector coll))

(indexed "abcde")

(defn index-filter [pred coll]
  (when pred
    (for [[idx elt] (indexed coll) :when (pred elt)] idx)))

(index-filter #(= % \d) "abcde")

(index-filter #{\a \b} "abcde")

(index-filter #{\z} "abcde")
