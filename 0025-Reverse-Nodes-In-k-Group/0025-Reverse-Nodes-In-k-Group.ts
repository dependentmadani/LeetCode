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
function storeAsArrays(head: ListNode|null, numberOfElements: number): Array<number> {
    let storage = [];
    let tmp = [];
    while (head != null) {
        tmp.push(head.val);
        if (tmp.length == numberOfElements) {
            storage.push(...tmp.reverse());
            tmp = [];
        }
        head = head.next;
    }
    if (tmp.length != 0) {
        storage.push(...tmp);
    }
    return storage;
}

function reverseHelper(head: ListNode| null, resultArray: Array<number>) {
    for (let i = 0; i < resultArray.length; ++i) {
        head.val = resultArray[i];
        head = head.next;
    }
}

function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    let result = storeAsArrays(head, k);
    reverseHelper(head, result);
    return head;
};