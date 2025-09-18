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

