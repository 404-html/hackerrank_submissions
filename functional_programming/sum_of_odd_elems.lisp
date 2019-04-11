;; https://www.hackerrank.com/challenges/fp-sum-of-odd-elements

;; Copyright (C) 2019  Matthias Paulmier

;; This work is free. You can redistribute it and/or modify it under the
;; terms of the Do What The Fuck You Want To Public License, Version 2,
;; as published by Sam Hocevar. See the COPYING file for more details.

(defun read-list ()
  (let ((n (read *standard-input* nil)))
    (if (null n)
        nil
        (cons n (read-list)))))

(defun f (lst)
  (if (eql nil lst) 0
      (if (evenp (car lst)) (f (cdr lst))
          (+ (car lst) (f (cdr lst))))))

(format t "~d" (f (read-list)))
