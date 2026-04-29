(ns card-games)

(defn rounds  [n]
  (list n (+ 1 n) (+ 2 n)))

(defn concat-rounds [l1 l2]
  (concat l1 l2))

(defn contains-round? [l n]
  (contains? (set l) n))


(defn card-average [hand]
  (/ (reduce + hand) (double (count hand))))

(defn middle [s]
  (when (seq s)
    (nth s (quot (dec (count s)) 2))))

(defn approx-average? [hand]
  (let [avg (card-average hand)]
    (or (== avg (/ (+ (last hand) (first hand)) 2))
        (== avg (middle hand)))))

(defn average-even-odd? [hand]
  (== (card-average (take-nth 2 hand))
      (card-average (take-nth 2 (rest hand)))))

(defn maybe-double-last
  [hand]
  (if (= 11 (last hand))
    (concat (drop-last 1 hand) `(22))
    hand))