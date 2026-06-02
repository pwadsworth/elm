(ns isogram
  (:require [clojure.string :as str]))

(defn isogram? [s]
  (let [norm (-> (str/lower-case s)
                 (str/replace #"[ \-]" "")
                 (seq))]
    (= (count norm) (count (set norm)))))
