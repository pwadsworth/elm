(ns raindrops)
(defn convert [n]
  (let [s (str (when (zero? (mod n 3)) "Pling")
               (when (zero? (mod n 5)) "Plang")
               (when (zero? (mod n 7)) "Plong"))]
    (if (empty? s) (str n) s)))