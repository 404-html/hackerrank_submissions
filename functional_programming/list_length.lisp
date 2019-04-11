;; https://www.hackerrank.com/challenges/fp-list-length

;; Copyright (C) 2019  Matthias Paulmier

;; This work is free. You can redistribute it and/or modify it under the
;; terms of the Do What The Fuck You Want To Public License, Version 2,
;; as published by Sam Hocevar. See the COPYING file for more details.

(defun read-list ()
  (let ((n (read *standard-input* nil)))
    (if (null n)
        nil
        (cons n (read-list)))))

(prin1 (list-length (read-list)))
