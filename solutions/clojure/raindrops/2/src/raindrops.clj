(ns raindrops)

(defn convert
  ([num] (convert num {} ""))
  ([num divBy msg]
   (cond
     (and (= 0 (mod num 3))
          (not (contains? divBy :3)))
     (recur num (assoc divBy :3 1) (str msg "Pling"))
     (and (= 0 (mod num 5))
          (not (contains? divBy :5)))
     (recur num (assoc divBy :5 1) (str msg "Plang"))
     (and (= 0 (mod num 7))
          (not (contains? divBy :7)))
     (recur num (assoc divBy :7 1) (str msg "Plong"))
     (or (contains? divBy :3) (contains? divBy :5) (contains? divBy :7))
     msg
     :else (str num))))