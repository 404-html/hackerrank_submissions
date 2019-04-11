;; https://www.hackerrank.com/challenges/fp-reverse-a-list

;; Copyright (C) 2019  Matthias Paulmier

;; This work is free. You can redistribute it and/or modify it under the
;; terms of the Do What The Fuck You Want To Public License, Version 2,
;; as published by Sam Hocevar. See the COPYING file for more details.

(defun f (lst)
  (if (eql nil lst) nil
      (append (f (cdr lst)) (cons (car lst) nil))))

(defun read-list ()
  (let ((n (read *standard-input* nil)))
    (if (null n)
        nil
        (cons n (read-list)))))

(format t "~{~d~%~}" (f (read-list)))
