#Project 3
#Andrew Blanchard

#Imports queues from the standard python library.
from collections import deque

#This creates the queue.
q = deque()

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Optional: for efficient adding to end

    def add_to_end(self, data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

# ---------------------------------------------------------------------------------------------------------------
#Check this code:

    def delete_specific_node(self, head_node, node_to_delete):
        if head_node == node_to_delete:
            return head_node.next_node

        curr = head_node
        while curr.next_node and curr.next_node != node_to_delete:
            curr = curr.next_node

        if curr.next_node is None:
            return head_node

        curr.next_node = curr.next_node.next_node

        return head_node

#new_head_node = delete_specific_node(head_node, B)
#display(new_head_node)
    
# ----------------------------------------------------------------------------------------------------------------

    def display_all_values(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next_node
    


    def count_recursive(self, node):
        # Base case: If the node is None, we've reached the end of the list
        if (node == None):
            return 0
        # Recursive step: Count the current node and add the count of the rest of the list
        return 1 + self.count_recursive(node.next_node)

    def get_count_recursive(self):
        # Start the recursive counting from the head of the list
        return self.count_recursive(self.head)

myLinkedList = LinkedList()

#-----------------------------------------------------------------------------------------------------------------------------
satiesfied_customer = None
orderNumber = 1

def new_order(value):
    value += 1
    orderName = input("\n\tCustomer name. Enter HERE: ")
    orderProduct = input("\n\tProduct name. Enter HERE: ")

    q.append(f"Order {orderNumber}, from {orderName}, has requested the item: {orderProduct}.")
    print("This new item has been added to the order list.")
    return value


def complete_next_node_order():
    if q:
        satiesfied_customer = q.popleft()
        myLinkedList.add_to_end(f"Order completed: {satiesfied_customer}\n")
        print(f"{satiesfied_customer} They received their order, so the line moves up.")
        return satiesfied_customer
    else:
        print("There are no more people waiting in line.")


def undo_last_order(satiesfied_customer):
    if(satiesfied_customer is not None):
        q.appendleft(satiesfied_customer)
        satiesfied_customer = myLinkedList.delete_specific_node(myLinkedList.head, satiesfied_customer)
        print(f"Last order re-added to queue: {str(satiesfied_customer)}")
        return satiesfied_customer
    else:
        print("There is no previous order")
        return


def display_current_order_queue():
    if q:
        print(q)
    else:
        print("There are no more people waiting in line.")


def display_all_orders_ever_done():
    myLinkedList.display_all_values()


def count_number_total_orders_ever():
    TotalCompletedInLinkedList = myLinkedList.get_count_recursive()
    print(f"There have been a total of {TotalCompletedInLinkedList} tasks completed")
    pass

#-----------------------------------------------------------------------------------------------------------------------------
#The main menu:
name = input("\n\tEnter username to enter business order client queue. Enter HERE: ")
while(True):
    print(f"\nHello {name}! This is the client queue: \n-------------------------------------------------------------------------------------------- \nPress 1 to *Add a new order to the queue.* \tPress 2 to *Complete the next_node order.* \nPress 3 to *Undo the last order* \t\tPress 4 to *Display the queue of current orders.* \nPress 5 to *Display all the orders ever done.* \tPress 6 to *Count the number of total orders ever.* \nPress 7 to *Exit the program.*")
    value = int(input("\n\tEnter HERE: "))
    if(value <= 7 and value >= 1):
        #Calls on the functions depending on what number was input.
        if(value == 1):
            orderNumber = new_order(orderNumber)
        elif(value == 2):
            satiesfied_customer = complete_next_node_order()
        elif(value == 3):
            satiesfied_customer = undo_last_order(satiesfied_customer)
        elif(value == 4):
            display_current_order_queue()
        elif(value == 5):
            display_all_orders_ever_done()
        elif(value == 6):
            count_number_total_orders_ever()
        elif(value == 7):
            value2 = input("\n\tAre you sure you want to quit? Y or N. Enter HERE: ")
            if(value2 == "Y"):
                print("\nLeaving Program, thank you!\n-------------------------------")
                break
            else:
                print("\nDidn't type uppercase Y. Program resuming.")
    else:
        print("\nTry Again, invalid selection")