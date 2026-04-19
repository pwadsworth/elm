(ns complex-numbers)

(defn real [[a _]]
  a)

(= 1 (real [1 2]))

(defn imaginary [[_ b]]
  b)

(= 2 (imaginary [1 2]))

(defn abs [[a b]]
  (Math/sqrt (+ (* a a) (* b b))))

(== 5 (abs [3 4]))

(defn conjugate [[a b]]
  [a (* -1 b)])

(= [1 -2] (conjugate [1 2]))

(defn add [[a b] [c d]]
  [(+ a c) (+ b d)])

(= [2 4] (add [1 2] [1 2]))

(defn sub [[a b] [c d]]
  [(- a c) (- b d)])

(= [1 4] (sub [2 6] [1 2]))

(defn mul [[a b] [c d]]
  [(- (* a c) (* b d))
   (+ (* b c) (* a d))])

(defn recip [[a b]]
  [(/ a (+ (* a a) (* b b)))
   (* -1 (/ b (+ (* a a) (* b b))))])


(defn div [[a b] [c d]] ;;
  (mul [a b] (recip [c d])))
