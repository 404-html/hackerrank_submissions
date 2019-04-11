;; https://www.hackerrank.com/challenges/fp-list-replication

;; Copyright (C) 2019  Matthias Paulmier

;; This work is free. You can redistribute it and/or modify it under the
;; terms of the Do What The Fuck You Want To Public License, Version 2,
;; as published by Sam Hocevar. See the COPYING file for more details.

(defun f (n lst &optional ini)
  (or ini (setq ini n))
  (cond ((eql lst nil) nil)
        ((eql 0 n) (f ini (cdr lst) ini))
        (t (cons (car lst) (f (1- n) lst ini)))))

(defun read-list ()
  (let ((n (read *standard-input* nil)))
    (if (null n)
        nil
        (cons n (read-list)))))

(format t "~{~d~%~}" (f (read) (read-list)))
