#lang racket

; Define a linked list node as a pair (cons cell)
(define-struct node (val next))

; Helper to build a linked list from a Racket list
(define (build-list lst)
  (if (null? lst)
      null
      (make-node (car lst) (build-list (cdr lst)))))

; Helper to print linked list
(define (print-list head)
  (cond
    [(null? head) (newline)]
    [else (begin
            (display (node-val head))
            (display " ")
            (print-list (node-next head)))]))

; Main function to remove Nth node from end
(define (remove-nth-from-end head n)
  ; Helper function returns two values: new list and length
  (define (helper node)
    (if (null? node)
        (values null 0)
        (let-values ([(new-next len) (helper (node-next node))])
          (if (= (+ 1 len) n)
              ; Skip current node
              (values new-next (+ 1 len))
              (values (make-node (node-val node) new-next) (+ 1 len))))))
  (define-values (new-head _) (helper head))
  new-head)

; Example usage
(define head (build-list '(1 2 3 4 5)))
(define new-head (remove-nth-from-end head 2))
(print-list new-head) ; Output: 1 2 3 5
