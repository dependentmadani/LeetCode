/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */
class ListNode {
        val: number
         next: ListNode | null
         constructor(val?: number, next?: ListNode | null) {
             this.val = (val===undefined ? 0 : val)
             this.next = (next===undefined ? null : next)
     }
 }

function nodeCounter(head: ListNode | null): number {
    let result = 0;
    while (head != null) {
        result += 1;
        head = head.next;
    }
    return result;
}

function swapHelper(head: ListNode | null, numberOfNode: number) {
    let numberOfTurns = Math.floor(numberOfNode / 2);
    let startingTurn = 0;
    while (startingTurn != numberOfTurns) {
        let tmp = head.val;
        head.val = head.next.val;
        head.next.val = tmp;
        head = head.next.next;
        startingTurn += 1;
    }
}

function swapPairs(head: ListNode | null): ListNode | null {
    let numberOfNode = nodeCounter(head);
    swapHelper(head, numberOfNode)
    return head;
};