;; Prog Cloj 2nd p. 12

(println "Hello world")

(defn hello [name]
  (str "Hello, " name))

(def visitors (atom #{}))

(swap! visitors conj "Stu")
