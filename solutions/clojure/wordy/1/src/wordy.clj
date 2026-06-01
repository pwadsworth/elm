(ns wordy
  (:require [clojure.string :as str]))

(def operations
  {"plus" +
   "minus" -
   "divided" /
   "multiplied" *})

(defn syntax-error []
  (throw (IllegalArgumentException. "syntax error")))

(defn parse-token [token]
  (or (parse-long token)
      (get operations token)
      (throw (IllegalArgumentException. "unknown operation"))))

(defn valid-expression? [tokens]
  (and (seq tokens)
       (number? (first tokens))
       (odd? (count tokens))
       (every? identity
               (map-indexed
                (fn [i token]
                  (if (even? i)
                    (number? token)
                    (ifn? token)))
                tokens))))

(defn execute-tokens [tokens]
  (when-not (valid-expression? tokens)
    (syntax-error))

  (reduce (fn [acc [op n]]
            (op acc n))
          (first tokens)
          (partition 2 (rest tokens))))

(defn tokens-from-question [s]
  (-> s
      (str/replace #"\?" "")
      str/lower-case
      (str/split #"\s+")
      (->> (drop 2)
           (remove #{"by" ""}))))

(defn evaluate [s]
  (if (str/starts-with? s "What is")
    (->> s
         tokens-from-question
         (map parse-token)
         execute-tokens)
    (syntax-error)))