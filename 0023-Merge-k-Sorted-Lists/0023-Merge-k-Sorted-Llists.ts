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

function getArrayOfListNode(lists: ListNode | null): Array<number> {
    let result: Array<number> = [];

    while (lists != null) {
        result.push(lists.val)
        lists = lists.next;
    }
    return result
}

function convertArrayToListNode(result: ListNode, tmpArray: Array<number>): boolean {
    let passed = false;
    for (let i = 0; i < tmpArray.length; ++i) {
        result.val = tmpArray[i]
        if (tmpArray.length - 1 != i ){
            result.next = new ListNode();
            result = result.next;
        }
        passed = true;
    }
    return passed
}

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    let result = new ListNode();
    let tmpArray = new Array();
    for (let i = 0; i < lists.length; ++i) {
        if (lists[i] != null) {
            tmpArray.push(...getArrayOfListNode(lists[i]));
        }
    }
    tmpArray.sort((a, b) => {return a - b});
    let passed = convertArrayToListNode(result, tmpArray);
    if (!passed) {
        return null
    }
    return result
};