(defn myrev [s]
  (stack s ""))

(defn stack [nxt s]
  (if (empty? nxt)
    s
    (stack (rest nxt) (str (first nxt) s))))

(stack "hello" "")

(myrev "aman")
