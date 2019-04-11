;; https://www.hackerrank.com/challenges/fp-filter-array/

;; Copyright (C) 2019  Matthias Paulmier

;; This work is free. You can redistribute it and/or modify it under the
;; terms of the Do What The Fuck You Want To Public License, Version 2,
;; as published by Sam Hocevar. See the COPYING file for more details.

(defun filter-array (filter lst)
  (cond ((null lst) nil)
        ((> filter (car lst)) (cons (car lst) (filter-array filter (cdr lst))))
        (t (filter-array filter (cdr lst)))))

(defun read-list ()
  (let ((n (read *standard-input* nil)))
    (if (null n)
        nil
        (cons n (read-list)))))

(format t "~{~a~%~}" (filter-array (read) (read-list)))
