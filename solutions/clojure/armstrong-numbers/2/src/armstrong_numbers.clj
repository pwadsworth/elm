(ns armstrong-numbers)

(defn num-digits [n]
  (count (.toString (bigint n))))

(defn digits [n]
  (mapv (comp #(Character/digit % 10) identity) (.toString (bigint n))))

(defn pow-bigint [base exp]
  (let [b (bigint base)]
    (loop [acc 1N, b b, e exp]
      (cond
        (zero? e) acc
        (odd? e)  (recur (* acc b) (* b b) (quot e 2))
        :else     (recur acc (* b b) (quot e 2))))))

(defn armstrong? [num]
  (let [n (bigint num)
        p (num-digits n)
        sum (reduce + (map #(pow-bigint % p) (digits n)))]
    (== n sum)))