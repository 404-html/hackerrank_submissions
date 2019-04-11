;; https://www.hackerrank.com/challenges/fp-array-of-n-elements

;; Copyright (C) 2019  Matthias Paulmier

;; This work is free. You can redistribute it and/or modify it under the
;; terms of the Do What The Fuck You Want To Public License, Version 2,
;; as published by Sam Hocevar. See the COPYING file for more details.

(defun f (n &optional (num 0))
  (if (eq 0 n) nil
      (cons n (f (1- n) (1+ num)))))
