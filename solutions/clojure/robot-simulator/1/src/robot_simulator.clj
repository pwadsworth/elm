(ns robot-simulator)

(defn- advance [state]
  (cond (= :north (get-in state [:bearing])) (update-in state [:coordinates :y] inc)
        (= :south (get-in state [:bearing])) (update-in state [:coordinates :y] dec)
        (= :east  (get-in state [:bearing])) (update-in state [:coordinates :x] inc)
        (= :west  (get-in state [:bearing])) (update-in state [:coordinates :x] dec)
        :else state))

(defn- turn-right [state]
  (cond (= :north (get-in state [:bearing])) (assoc state :bearing :east)
        (= :south (get-in state [:bearing])) (assoc state :bearing :west)
        (= :east  (get-in state [:bearing])) (assoc state :bearing :south)
        (= :west  (get-in state [:bearing])) (assoc state :bearing :north)
        :else state))

(defn- turn-left [state]
  (cond (= :north (get-in state [:bearing])) (assoc state :bearing :west)
        (= :south (get-in state [:bearing])) (assoc state :bearing :east)
        (= :east  (get-in state [:bearing])) (assoc state :bearing :north)
        (= :west  (get-in state [:bearing])) (assoc state :bearing :south)
        :else state))

(defn- update-state [state ltr]
  (cond (= ltr "A") (advance state)
        (= ltr "R") (turn-right state)
        (= ltr "L") (turn-left state)))

(defn robot [coordinates direction]
  {:bearing direction :coordinates coordinates})

(defn simulate [instructions robot-state]
  (reduce (fn [s i] (update-state s i))
          robot-state
          (mapv str instructions)))
