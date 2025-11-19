#Project 3
#Andrew Blanchard

#Imports queues from the standard python library.
from collections import deque

#This creates the queue.
q = deque()

#This first class defines how the node data would work, now I looked this up since I am shaky on how to code it myself.
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

#This class uses both it's own structure and the Node class to preform it's task of making a singly linked list.
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
#This is the main code for number 3. It is quite buggy. I don't blame ya if it fails.

    def delete_specific_node(self, head_node, node_to_delete):
        if head_node == node_to_delete:
            return head_node.next_node

        curr = head_node
        while curr.next_node and curr.next_node != node_to_delete:
            curr = curr.next_node

        if curr.next_node is None:
            return head_node

        curr.next_node = curr.next_node.next_node

        return node_to_delete

#new_head_node = delete_specific_node(head_node, B)
#display(new_head_node)
    
# ----------------------------------------------------------------------------------------------------------------

    #Displays all values of the linked list.
    def display_all_values(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next_node
    
    #Counts all values of the linked list.
    def count_recursive(self, node):
        # Base case: If the node is None, we've reached the end of the list
        if (node == None):
            return 0
        # Recursive step: Count the current node and add the count of the rest of the list
        return 1 + self.count_recursive(node.next_node)

    #Uses the function above to return the final value.
    def get_count_recursive(self):
        # Start the recursive counting from the head of the list
        return self.count_recursive(self.head)

myLinkedList = LinkedList()

#-----------------------------------------------------------------------------------------------------------------------------
satiesfied_customer = None
orderNumber = 1

#This creates a new order.
def new_order(value):
    value += 1
    orderName = input("\n\tCustomer name. Enter HERE: ")
    orderProduct = input("\n\tProduct name. Enter HERE: ")

    q.append(f"Order {orderNumber}, from {orderName}, has requested the item: {orderProduct}.")
    print("This new item has been added to the order list.")
    return value

#Completes the next order in the queue, really simple.
def complete_next_node_order():
    if q:
        satiesfied_customer = q.popleft()
        myLinkedList.add_to_end(f"Order completed: {satiesfied_customer}\n")
        print(f"{satiesfied_customer} They received their order, so the line moves up.")
        return satiesfied_customer
    else:
        print("There are no more people waiting in line.")

#It does undo the last order, but also runs into issues with options 5 and 6
def undo_last_order(satiesfied_customer):
    if(satiesfied_customer is not None):
        q.appendleft(satiesfied_customer)
        satiesfied_customer = myLinkedList.delete_specific_node(myLinkedList.head, satiesfied_customer)
        print(f"Last order re-added to queue: {str(satiesfied_customer)}")
        return satiesfied_customer
    else:
        print("There is no previous order")
        return

#Desplays the current orders in the queue.
def display_current_order_queue():
    if q:
        print(q)
    else:
        print("There are no more people waiting in line.")

#This displays all orders completed for the most part unless option 3 is used unfortunately.
def display_all_orders_ever_done():
    myLinkedList.display_all_values()

#This counts the values in the completed order in the linked list. Has an issue with option 3 sadly.
def count_number_total_orders_ever():
    TotalCompletedInLinkedList = myLinkedList.get_count_recursive()
    print(f"There have been a total of {TotalCompletedInLinkedList} tasks completed")
    pass

#-----------------------------------------------------------------------------------------------------------------------------
#The main menu code, this code loops to create the ability to submit items into a queue and track them.
name = input("\n\tEnter username to enter business order client queue. Enter HERE: ")
while(True):
    print(f"\nHello {name}! This is the client queue: \n-------------------------------------------------------------------------------------------- \nPress 1 to *Add a new order to the queue.* \tPress 2 to *Complete the next_node order.* \n[BROKEN]Press 3 to *Undo the last order* \t\tPress 4 to *Display the queue of current orders.* \nPress 5 to *Display all the orders ever done.* \tPress 6 to *Count the number of total orders ever.* \nPress 7 to *Exit the program.*")
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
        #This code below exits the function.
        elif(value == 7):
            value2 = input("\n\tAre you sure you want to quit? Y or N. Enter HERE: ")
            if(value2 == "Y"):
                print("\nLeaving Program, thank you!\n-------------------------------")
                break
            else:
                print("\nDidn't type uppercase Y. Program resuming.")
    else:
        print("\nTry Again, invalid selection")