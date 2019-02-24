#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    n = DoublyLinkedListNode(data)

    if head == None:
        return n;    
    
    if (data < head.data):
        n.next  = head
        head.prev = n
        return n
    else:
        n1 = None
        n2 = head
        while n2 != None and n2.data < data:
                n1 = n2
                n2 = n2.next

        if n2 == None:
            n1.next = n
            n.prev = n1
        else:
            n1.next = n
            n2.prev = n
            n.prev = n1
            n.next = n2
      
        return head;
  
 


if __name__ == '__main__':
