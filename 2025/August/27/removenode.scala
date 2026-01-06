// Definition for singly-linked list
class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def removeNthFromEnd(head: ListNode, n: Int): ListNode = {
    val dummy = new ListNode(0, head)
    var slow: ListNode = dummy
    var fast: ListNode = dummy

    // Move fast ahead by n+1 steps
    for (_ <- 0 to n) {
      fast = fast.next
    }

    // Move slow and fast together
    while (fast != null) {
      slow = slow.next
      fast = fast.next
    }

    // Remove nth node
    slow.next = slow.next.next

    dummy.next
  }

  // Helper: build list from Scala List
  def buildList(arr: List[Int]): ListNode = {
    val dummy = new ListNode()
    var curr = dummy
    for (v <- arr) {
      curr.next = new ListNode(v)
      curr = curr.next
    }
    dummy.next
  }

  // Helper: print list
  def printList(head: ListNode): Unit = {
    var curr = head
    while (curr != null) {
      print(curr.x + " ")
      curr = curr.next
    }
    println()
  }

  def main(args: Array[String]): Unit = {
    val head = buildList(List(1, 2, 3, 4, 5))
    val newHead = removeNthFromEnd(head, 2)
    printList(newHead) // Output: 1 2 3 5
  }
}
