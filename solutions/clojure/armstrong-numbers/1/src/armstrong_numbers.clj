(ns armstrong-numbers)


(defn numDigits [n]
  (count (str n)))

(defn digits [n]
  (map int (mapv (comp #(Character/digit % 10) identity) (str (Math/abs n)))))

(defn armstrong? [num]
  (== num (reduce + (map #(Math/pow %1 (numDigits num)) (digits num)))))
