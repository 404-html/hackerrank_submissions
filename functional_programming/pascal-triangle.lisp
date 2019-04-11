;; https://www.hackerrank.com/challenges/pascals-triangle/

;; Copyright (C) 2019  Matthias Paulmier

;; This work is free. You can redistribute it and/or modify it under the
;; terms of the Do What The Fuck You Want To Public License, Version 2,
;; as published by Sam Hocevar. See the COPYING file for more details.


(defun pascal (n)
  "Build the pascal triangle"
  (triangle '(1) n))

(defun triangle (row n)
  "Recursive helper function for building the triangle"
  (if (< 0 n)
      (cons row (triangle (cons 1 (build-row row)) (1- n)))
      nil))

(defun build-row (row)
  "Helper function for building a row of the triangle"
  (if (> 2 (length row))
      '(1)
      (cons (+ (car row) (cadr row)) (build-row (cdr row)))))

(defun pp-pascal (pt)
  "Pretty print the triangle"
  (format t "~{~{~a ~}~%~}" pt))

(pp-pascal (pascal (read)))
