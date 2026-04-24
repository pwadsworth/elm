(ns bob
  (:require [clojure.string :as str]))

(defn- isYelling? [s]
  (let [letters (filter #(or (Character/isLetter %) (= "?" %)) s)]
    (and (seq letters)
         (every? #(Character/isUpperCase %) letters))))

(defn- isQuestion? [s]
  (= "?" (str (last (seq (str/trim s))))))

(defn- isSilence [s]
  (every? #(Character/isSpace %) (seq s)))

(defn response-for [s]
  (cond
    (and (isYelling? s) (isQuestion? s)) "Calm down, I know what I'm doing!"
    (isQuestion? s) "Sure."
    (isYelling? s) "Whoa, chill out!"
    (isSilence s) "Fine. Be that way!"
    :else "Whatever."))