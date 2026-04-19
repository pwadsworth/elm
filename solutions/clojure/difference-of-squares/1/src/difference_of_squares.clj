(ns difference-of-squares)

(defn sqr
  "Return the square of a number."
  [n]
  (* n n))

(= (sqr 4) 16)

(defn square-of-sum
  "Returns the square of the sum of the numbers up to N."
  [N]
  (->> (range (+ N 1))
       (reduce +)
       (sqr)))

(= (square-of-sum 10) 3025)

(defn sum-of-squares
  "Returns the sum of the squares of the numbers up to N."
  [N]
  (->> (range (+ N 1))
       (map sqr)
       (reduce +)))

(= (sum-of-squares 10) 385)

(defn difference
  "Returns the difference between the square of the sum
  and the sum of the squares of the numbers up to N."
  [N]
  (- (square-of-sum N) (sum-of-squares N)))

(= (difference 10) 2640)