package merge_two_sorted_lists;

import java.util.ArrayList;
import java.util.Collections;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

public class Solution 
{
    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) 
    {
        ArrayList<Integer> list = new ArrayList<>();

        while (list1 != null)
        {
            list.add(list1.val);
            list1 = list1.next;
        }

        while (list2 != null)
        {
            list.add(list2.val);
            list2 = list2.next;
        }

        Collections.sort(list);

        ListNode temp = new ListNode(-200);
        ListNode head = temp;

        for (int value : list)
        {
            temp.next = new ListNode(value);
            temp = temp.next;
        }

        head = head.next;
        return head;
    }

    public static void main(String[] args) 
    {
        ListNode a = new ListNode(2);
        a.next = new ListNode(4);
        a.next.next = new ListNode(8);
        a.next.next.next = new ListNode(9);

        // Create another hard-coded linked list:
        // 1 -> 3 -> 8 -> 10
        ListNode b = new ListNode(1);
        b.next = new ListNode(3);
        b.next.next = new ListNode(8);
        b.next.next.next = new ListNode(10);

        ListNode res = mergeTwoLists(a, b);

        ListNode aux = res;
        do
        {
            System.out.println(aux.val);
            aux = aux.next;
        }
        while(aux != null);
    }
}
