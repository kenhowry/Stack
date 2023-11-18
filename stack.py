class Node:
    def __init__(self, v, n):
        """
            Description of Function:
                initializes an empty node
            Parameters:
                v: value of node
                n: reference to next node
            Return:
                None
        """
        self.value = v
        self.next = n
    
    def __eq__(self, other):
        """
            Description of Function:
                determines if the node is equivalent to another
            Parameters:
                other: another node
            Return:
                bool
        """
        return self.value == other.value

    def __str__(self):
        """
            Description of Function: 
                returns a string representing the node
            Parameters: 
                None
            Return: 
                str
        """
        return str(self.value)

class SinglyLinkedList:
    def __init__(self):
        """
            Description of Function:
                initializes an empty list
            Parameters:
                None
            Return:
                None
        """
        self.head = None
        self.size = 0
    
    def __str__(self):
        """
            Description of Function:
                returns a string representing the values of all items in the list
            Parameters:
                None
            Return:
                str
        """
        #if the list is empty
        if self.head is None:
            return '[]'
        
        result = '['

        #create a reference to the head and advance it instead of head
        #advancing head removes nodes

        temp_node = self.head

        while temp_node.next is not None:
            result += str(temp_node) + " "
            temp_node = temp_node.next
        
        return result + str(temp_node) + ']'
    
    def get_size(self):
        """
            Description of Function:
                returns the number of nodes in the list
            Parameters:
                None
            Return:
                int
        """
        return self.size

    def is_empty(self):
        """
            Description of Function:
                returns True if the list is empty, False if otherwise
            Parameters:
                None
            Return:
                bool
        """
        return self.head is None
    
    #inserts a new node with the parameter as the new first element
    def add_first(self, value): 
        """
            Description of Function:
                inserts a new node with the parameter as the new first element
            Parameters:
                value: the value of the new node
            Return:
                None
        """   
        #step 1: create a node with value and the head as next ref
        new_node = Node(value, self.head)

        #step 2: make head point to new node
        self.head = new_node

        #step 3:incremenet size
        self.size += 1

    #appends a new node with the parameters as the last element
    def add_last(self, value):
        """
            Description of Function:
                appends a new node with the parameters as the last element
            Parameters:
                value: the value of the new node
            Return:
                None
        """
        #step 1: create a node with value and None as ref
        new_node = Node(value, None)

        #step 2: make the old end point to the new end
            #special case: the list is initially empty

        if self.head is None:
            self.head = new_node

        else:
            temp_node = self.head

            while temp_node.next is not None:
                temp_node = temp_node.next
            
            temp_node.next = new_node

        #step 3: increment size
        self.size += 1
        
    #remove the first node, return its associated value
    def remove_first(self):
        """
            Description of Function:
                remove the first node, returning its associated value
            Parameters:
                None
            Return:
                the generic type E of the node
        """
        if self.head is None:
            raise ValueError("List is empty.")
        
        #step 1: store the head value
        return_value = self.head.value

        #step 2: advance the head reference
        self.head = self.head.next

        #step 3: decrement size
        self.size -=1

        return return_value
    
    #remove the last node, return its associated value
    def remove_last(self):
        """
            Description of Function:
                remove the last node, returning its associated value
            Parameters:
                None
            Return:
                the generic type E of the node
        """
        #if the list is empty, calling the method should raise an error
        if self.head is None:
            raise ValueError("List is empty.")          

        return_value = None

        #if the list has only one element, return the value of that element and set the head to null
        if self.head.next is None:
                return_value = self.head.value
                self.head = None
        else: 
            temp_node = self.head
            while temp_node.next.next is not None:
                temp_node = temp_node.next          

            return_value = temp_node.next.value
            temp_node.next = None

        self.size -= 1   

        return return_value
    
    #return the value stored at the given index position
    def get(self, index):
        """
            Description of Function:
                return the value stored at the given index position
            Parameters:
                index: the index desired
            Return:
                the generic type E of the node
        """
        #IndexError
        if index >= self.size:
            raise IndexError("Index is out of range.")
        
        #step 1: create variable to track the index
        idx_value = 0

        #step 2: create a second variable to traverse the list 
        temp_node = self.head

        #step 3: traverse list until the given index and return value
        while True:
            if idx_value == index:
                return temp_node.value
            temp_node = temp_node.next
            idx_value += 1
    
    #removes the node at index [i] from the list, returning its associated value
    def remove_at_index(self, index: int):
        """
            Description of Function:
                removes the node at index [i] from the list, returning its associated value
            Parameters:
                index: the index desired
            Return:
                the generic type E of the node
        """
        #ValueError
        if self.head is None:
            raise ValueError("List is empty.")  
        
        #IndexError
        if index >= self.size:
            raise IndexError("Index is out of range.")
        
        #decrement size
        self.size -= 1

        #step 1: create variables to track the index and traverse list
        idx_value = 0
        current_node = self.head

        #step 2: traverse list until the given index and deletes node
        while idx_value <= index:
            node_before = current_node
            current_node = current_node.next
            idx_value += 1
            if index == 0:
                deleted_value = self.head.value
                self.head = self.head.next
                return deleted_value
            elif idx_value == index:
                deleted_value = current_node.value
                node_before.next = current_node.next
                return deleted_value
    
    #finds the minimum value in the list and returns the value
    def find_minimum(self):
        """
            Description of Function:
                finds the minimum value in the list and returns the value
            Parameters:
                None
            Return:
                the generic type E of the node
        """
        #list is empty; raising a ValueError
        if self.head is None:
            raise ValueError("List is empty.")
        
        #creating variable
        min_value = None

        #if the list has only one element, return the value of that element
        if self.head.next is None:
            min_value = self.head.value

        else:
        #step 1: store the head value as starting value
            temp_node = self.head
            min_value = self.head.value

        #step 2: transverse the list comparing the values and changing the value of the variable accordingly
            while temp_node is not None:
                if min_value > temp_node.value:
                    min_value = temp_node.value
                
                #increment
                temp_node = temp_node.next

        #step 3: return the minimum value
        print(min_value)   

    #returns the value of the first node in the list
    def first(self):
        """
            Description of Function:
                returns the value of the first node in the list
            Parameters:
                None
            Return:
                the generic type E of node
        """
        return self.head.value
    
class Stack:
    #top is at head of the list
    def __init__(self):
        """
            Description of Function:
                initializes an empty singly-linked list for the stack
            Parameters:
                None
            Return:
                None
        """
        self.the_stack = SinglyLinkedList()
    
    def push(self, e):
        """
            Description of Function:
                adds a node to the top of the stack
            Parameters:
                e: the value of the node
            Return:
                None
        """
        self.the_stack.add_first(e)

    def pop(self):
        """
            Description of Function:
                remove and return value of top element of the stack
            Parameters:
                None
            Return:
                the generic type E of the top element
        """
        return self.the_stack.remove_first()

    def top(self):
        """
            Description of Function:
                returns the value of the top element of the stack, 
                without removing it from the stack
            Parameters:
                None
            Return:
                the generic type E of the top element
        """
        return self.the_stack.first()

    def get_size(self):
        """
            Description of Function:
                return number elements in the stack
            Parameters:
                None
            Return:
                int
        """
        return self.the_stack.get_size()

    def is_empty(self):
        """
            Description of Function:
                return True is the stack is empty, False otherwise
            Parameters:
                None
            Return:
                bool
        """
        return self.the_stack.is_empty()
    
def  is_balanced(some_str: str) -> bool:
    """
        Description of Function:
            determines if the parentheses, square brackets and curly braces 
            are properly balanced (matched)
        Parameters:
            some_str: a user input string
        Return:
            bool
    """
    #intiatilizing an empty list
    just_brackets = []

    #creating a list of valid characters
    valid_characters = ["(", "[", "{", ")", "]", "}"]

    #iterating through the string to isolate the brackets
    for char in some_str:
        if char in valid_characters:
            just_brackets.append(char)

    #creating a variable using the Stack class
    some_stack = Stack()

    #iterate through the list of brackets
    for char in just_brackets:
        #if the character is an opening bracket,
        #push it onto the stack
        if char in ["(", "[", "{"]:
            some_stack.push(char)

        else:
            #if the stack is empty at this point,
            #it is not balanced
            if some_stack.is_empty() == True:
                return False
            
            #popping the the values in the stack
            opening_bracket = some_stack.pop()

            #checking if the popped value has a mate
            if opening_bracket == "(":
                if char != ")":
                    return False
            elif opening_bracket == "[":
                if char != "]":
                    return False
            elif opening_bracket == "{":
                if char != "}":
                    return False
    
    #checking to seeing if the stack is empty
    if some_stack.is_empty() == False:
        return False
    
    #returning True if it all tests are passed
    return True

#driver      
if __name__=='__main__':
    example_string = input('What string would you like to test? ')
    print(is_balanced(example_string))
