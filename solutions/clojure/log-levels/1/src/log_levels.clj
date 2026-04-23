(ns log-levels
  (:require [clojure.string :as str]))

(defn message [s]
  (->> (second (str/split s #"\]: "))
       (str/trim)))

(defn log-level [s]
  (->> (second (str/split s #"\[|\]"))
       (str/lower-case)))

(defn reformat [s]
  (str (message s) " (" (log-level s) ")"))