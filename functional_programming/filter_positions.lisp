;; https://www.hackerrank.com/challenges/fp-filter-positions-in-a-list

;; Copyright (C) 2019  Matthias Paulmier

;; This work is free. You can redistribute it and/or modify it under the
;; terms of the Do What The Fuck You Want To Public License, Version 2,
;; as published by Sam Hocevar. See the COPYING file for more details.

(defun f (lst &optional (parity 1))
  (cond ((eql lst nil) nil)
        ((eql parity 0) (f (cdr lst)))
        (t (cons (car lst) (f (cdr lst) (abs (1- parity)))))))

(defun read-list ()
  (let ((n (read *standard-input* nil)))
    (if (null n)
        nil
        (cons n (read-list)))))
(read)
(format t "~{~d~%~}" (f (read-list)))
