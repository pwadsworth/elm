(ns anagram
  (:require [clojure.string :as str]))

(defn is-anagram? [norm-wrd candidate]
  (let [norm-candidate (str/lower-case candidate)]
    (and (= (sort norm-wrd) (sort norm-candidate))
         (not= norm-wrd norm-candidate))))

(defn anagrams-for [word candidates]
  (let [norm-wrd (str/lower-case word)]
    (filter #(is-anagram? norm-wrd %) candidates)))
