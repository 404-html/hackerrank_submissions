;; https://www.hackerrank.com/challenges/coin-change

;; Copyright (C) 2019  Matthias Paulmier

;; This work is free. You can redistribute it and/or modify it under the
;; terms of the Do What The Fuck You Want To Public License, Version 2,
;; as published by Sam Hocevar. See the COPYING file for more details.


;; This solution is not accepted as it takes too much time for
;; hackerrank I need to find a better one even though my python
;; solution with the same algorithm works perfectly

(defun count-parts (val poss &key (memo (make-hash-table :test 'equal)))
  (cond ((eql val 0) 1)
        ((null poss) 0)
        (t
         (progn
           (if (gethash (format nil "~d_~d" val (length poss)) memo)
               (gethash (format nil "~d_~d" val (length poss)) memo)
               (let ((total 0)
                     (ways 0))
                 (loop while (<= total val)
                    do (let ((rest (- val total)))
                         (setf ways (+ ways (count-parts rest (cdr poss))))
                         (setf total (+ total (car poss)))))
                 (setf (gethash (format nil "~d_~d" val (length poss)) memo) ways)))))))

(defun read-list ()
  (let ((n (read *standard-input* nil)))
    (if (null n)
        nil
        (cons n (read-list)))))

(defparameter *n* (read))
(read)
(defparameter test 0)
(format t "~d" (count-parts *n* (read-list)))
