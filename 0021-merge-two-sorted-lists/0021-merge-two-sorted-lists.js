/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */

function insert(root, value) {
    var temp = new ListNode();
    var ptr;

    temp.val = value;
    temp.next = null;
    if (root == null) {
        root = temp;
    }
    else {
        ptr = root;
        while (ptr.next != null) {
            ptr = ptr.next;
        }
        ptr.next = temp;
    }
    return root;
}

var mergeTwoLists = function(list1, list2) {
    var result = [];
    var result_linked_list = null;
    
    while ( list1 != null || list2 != null) {
        if (list1 != null) {
            result.push(list1.val);
            list1 = list1.next;
        }
        if (list2 != null) {
            result.push(list2.val);
            list2 = list2.next;
        }
    }
    function compare(a, b) {
        return a - b ;
    }
    result.sort(compare);
    for (let i = 0; i < result.length; ++i) {
        result_linked_list = insert(result_linked_list, result[i]);
    }
    return result_linked_list;
};