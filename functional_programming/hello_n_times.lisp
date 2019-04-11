;; https://www.hackerrank.com/challenges/fp-list-replication

;; Copyright (C) 2019  Matthias Paulmier

;; This work is free. You can redistribute it and/or modify it under the
;; terms of the Do What The Fuck You Want To Public License, Version 2,
;; as published by Sam Hocevar. See the COPYING file for more details.

(defun f (n)
  (if (eql 0 n)
      nil
      (progn
        (format t "Hello World~C" #\linefeed)
        (f (1- n)))))

(f (read))
