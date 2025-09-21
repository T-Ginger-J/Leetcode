#lang racket

(define (merge-intervals intervals)
  (define sorted-intervals (sort intervals < #:key first))
  (define result '())
  (for ([iv sorted-intervals])
    (if (null? result)
        (set! result (list iv))
        (let* ([last (last result)]
               [ls (first last)] [le (second last)]
               [cs (first iv)]   [ce (second iv)])
          (if (<= cs le)
              (set! result (append (drop-right result 1)
                                   (list (list ls (max le ce)))))
              (set! result (append result (list iv)))))))
  result)

;; ---- Example Uses ----
(displayln (merge-intervals '((1 3) (2 6) (8 10) (15 18))))
; => '((1 6) (8 10) (15 18))

(displayln (merge-intervals '((1 4) (4 5))))
; => '((1 5))

(displayln (merge-intervals '((1 2) (3 4) (5 6))))
; => '((1 2) (3 4) (5 6))

(displayln (merge-intervals '((1 10) (2 3) (4 5) (6 7))))
; => '((1 10))
