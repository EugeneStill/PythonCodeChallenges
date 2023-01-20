import helpers.node as nd

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        # always start at head in ll
        current = self.head
        # if head exists go through all nodes then add new node to end of ll
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        # if no head exists yet then set it
        else:
            self.head = new_node
        return

    def delete(self, value):
        current = self.head
        # if head has the value to be removed then set new head as the node that old head pointed to
        if current.value == value:
            self.head = current.next
        # else go through nodes until value is found
        else:
            while current:
                if current.value == value:
                    break
                # this is going through the nodes, moving prev and current up 1 space at a time
                prev = current
                current = current.next
            # if node not found then return
            if current is None:
                return
            # if node found then update prev pointer to point to the node after the node being removed
            prev.next = current.next
            # current = None
        return

    def insert(self, new_node, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        count = 1
        current = self.head
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            while current:
                if count + 1 == position:
                    new_node.next = current.next
                    current.next = new_node
                    return
                else:
                    count += 1
                    current = current.next
        return

    def create_linked_list(self, vals):
        for v in vals:
            new_node = nd.Node(v)
            self.append(new_node)
        return

    def get_list_from_linked_list(self):
        new_list = [self.head.value]
        current = self.head
        while current.next:
            new_list.append(current.next.value)
            current = current.next
        return new_list


    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
        return
