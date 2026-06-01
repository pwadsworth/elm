(ns pangram)

(defn pangram? [s]
  (let [letters (set (map #(Character/toLowerCase %) (filter #(Character/isLetter %) s)))]
    (every? letters (map char (range (int \a) (inc (int \z)))))))
