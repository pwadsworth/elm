(ns bird-watcher)

(def last-week
  [0 2 5 3 7 8 4])

(defn today [birds]
  (birds 6))

(defn inc-bird [birds]
  (update birds 6 inc))

(defn day-without-birds? [birds]
  (< 0 (count (filter #(= 0 %1) birds))))

(defn n-days-count [birds n]
  (reduce + (take n birds)))

(defn busy-days [birds]
  (->> birds
       (map #(>= %1 5))
       (filter #(= %1 true))
       (count)))

(defn odd-week? [birds]
  (every? #{1 0} birds))

(day-without-birds? [4 9 5 7 8 8 2])