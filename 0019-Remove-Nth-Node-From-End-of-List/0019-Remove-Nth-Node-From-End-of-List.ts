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

function getSizeListNode(head: ListNode | null): number {
    let result = 0;

    while (head != null) {
        result += 1
        head = head.next;
    }
    return result
}

function removalHelper(head: ListNode | null, position: number) {
    let notDone = true;
    let starter = 0;
    let catcher = head;
    if (head != null)
        head = head.next;
    while (notDone) {
        if (position - 1 === starter) {
            if (head != null) {
                catcher.next = head.next;
            } else {
                catcher.next = null;
            }
            notDone = false;
        } else {
            catcher = head;
        }
        if (head != null) {
            head = head.next;
        } else {
            notDone = false;
        }
        starter += 1;
    }
}

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let sizeList = getSizeListNode(head);
    let positionToRemove = sizeList - n;
    if (sizeList == 1) {
        head = null;
        return null;
    }
    if (positionToRemove === 0) {
        head = head.next;
        return head;
    }
    removalHelper(head, positionToRemove);
    return head;
};