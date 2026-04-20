(ns collatz-conjecture)

(defn collatz
  "Returns the number of steps for num to reach 1
  according to the Collatz Conjecture."
  ([num] (collatz num 0))
  ([num steps] (cond
                 (= 1 num) steps
                 (even? num) (collatz (/ num 2) (inc steps))
                 :else (collatz (inc (* num 3)) (inc steps)))))