;; p. 61

(defn xors [max-x max-y]
  (for [x (range max-x) y (range max-y)]
    [x y (bit-xor x y)]))

(def frame (java.awt.Frame.))
(.setVisible frame true)
(.setSize frame (java.awt.Dimension. 200 200))

(def gfx (.getGraphics frame))

;; (.fillRect gfx 100 100 50 20)

(doseq [[x y xor] (xors 200 200)]
  (.setColor gfx (java.awt.Color. (int (/ xor 3)) (int (/ xor (inc (int (rand 4))))) (int (/ xor 1))))
  (.fillRect gfx x y 1 1))
