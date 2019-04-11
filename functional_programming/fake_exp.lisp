;; https://www.hackerrank.com/challenges/eval-ex/

;; Copyright (C) 2019  Matthias Paulmier

;; This work is free. You can redistribute it and/or modify it under the
;; terms of the Do What The Fuck You Want To Public License, Version 2,
;; as published by Sam Hocevar. See the COPYING file for more details.

(setq *read-default-float-format* 'double-float)

(defun fake-exp (x &optional (n 9))
  (if (eql n 0)
      1
      (+ (/ (expt x n) (fact n)) (fake-exp x (1- n)))))

(defun fact (x)
  (if (eql 0 x)
      1
      (* x (fact (1- x)))))

(defun print-fake-exp (n)
  (format t "~,4f~%" (fake-exp n)))

(defun read-list ()
  (let ((n (read *standard-input* nil)))
    (if (null n)
        nil
        (cons n (read-list)))))

(read)
(mapcar #'print-fake-exp (read-list))
