import csv
# import pandas as pd

# Reading the CSV files and storing in a varibale for latesr testing the below functions

# problem1_construct_tree = pd.read_csv('/Users/vishnusaivardhanreddybasireddygari/Downloads/msml606_hw2_spring26/p1_construct_tree.csv')
# problem1_construct_tree.head()

# ---------- AI Usgae or external tools -----------------------------------------
#Problem 1: Did not used AI or any other external tools in this problem
#Problem 2.1: Did not used AI any other external tools in this problem
#Problem 2.2: Used AI to understand the logic because i made code but i was getting error, used AI to debug and how to handle paranthesis and made code by myself.
#problem 2.3: Did not used AI any other external tools in this problem
#Problem 3: Used AI to understand the how to to do evaluate because i did not know before that operations cannot be at the leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class HomeWork2:

    # Problem 1: Construct an expression tree (Binary Tree) from a postfix expression
    # input -> list of strings (e.g., [3,4,+,2,*])
    # this is parsed from p1_construct_tree.csv (check it out for clarification)

    # there are no duplicate numeric values in the input
    # support basic operators: +, -, *, /

    # output -> the root node of the expression tree. Here: [*,+,2,3,4,None,None]
    # Tree Node with * as root node, the tree should be as follows
    #         *
    #        / \
    #       +   2
    #      / \
    #     3   4

    def constructBinaryTree(self, input) -> TreeNode:
        #basically postfix - left,right,root
        #my logic i'm thinking i will reverse the input list & then make a stack and into it.
        # stack = []
        # n = len(input)
        # for i in range(n-1,-1,-1):
        #     stack.append(input[i])
        # print(input)
        # print(stack)
        # # print(reverse_input)
        # root_node = TreeNode(stack[0])
        # for i in range(1,len(stack)):
        #     curr_node = TreeNode()
        #     if i%3==0:
        #         root_node = curr_node
        #     if i%3==1:
        #         root_node.right = curr_node
        #     if i%3==2:
        #         root_node.left = curr_node
        # return root_node


        #edge case empty input
        if not input:
            return None
        stack = Stack()
        for value in input:
            if value in "+-*/":
                right = stack.pop()
                left = stack.pop()
                stack.add(TreeNode(value,left,right))
            else:
                stack.add(TreeNode(value))
        
        return stack.stack[0]
        
        # pass



    # Problem 2.1: Use pre-order traversal (root, left, right) to generate prefix notation
    # return an array of elements of a prefix expression
    # expected output for the tree from problem 1 is [*,+,3,4,2]
    # you can see the examples in p2_traversals.csv

    def prefixNotationPrint(self, head: TreeNode) -> list:
        # so basically prefix - root,left,right
        # edge cases will be like empty tree or tree with one node
        if not head:
            return None
        if head.left is None and head.right is None:
            return head.val
        stack = Stack() #intiating stack beacuse it will maintain the traversal 
        stack.add(head) # adding root, since it is prefix, first it will print root
        result = []
        while stack.stack:
            curr_node = stack.pop()
            result.append(curr_node.val)

            if curr_node.right:                #sicne it is stack we are appedning right before left because we wanna print left which pops before right value of that node
                stack.add(curr_node.right)
            if curr_node.left:
                stack.add(curr_node.left)
        return result


        # pass

    # Problem 2.2: Use in-order traversal (left, root, right) for infix notation with appropriate parentheses.
    # return an array of elements of an infix expression
    # expected output for the tree from problem 1 is [(,(,3,+,4,),*,2,)]
    # you can see the examples in p2_traversals.csv

    # don't forget to add parentheses to maintain correct sequence
    # even the outermost expression should be wrapped
    # treat parentheses as individual elements in the returned list (see output)

    def infixNotationPrint(self, head: TreeNode) -> list:
        #infix = left,root,right
        # edgae cases are empty, and 1 node 
        if head is None:
            return []
        if head.left is None and head.right is None:
            return ["(", str(head.val), ")"]
        
        result = []
        stack = Stack()
        stack.add((head,0))
        while stack.stack:
            node,state = stack.pop()
            if_leaf = (node.left is None and node.right is None)
            if if_leaf:
                result.append(str(node.val))
                continue
            if state == 0:
                result.append("(")
                stack.add((node,1))
                stack.add((node.left,0))
            elif state==1:
                result.append(node.val)
                stack.add((node,2))
                stack.add((node.right,0))
            else:
                result.append(")")
        
        return result

        # pass


    # Problem 2.3: Use post-order traversal (left, right, root) to generate postfix notation.
    # return an array of elements of a postfix expression
    # expected output for the tree from problem 1 is [3,4,+,2,*]
    # you can see the examples in p2_traversals.csv

    def postfixNotationPrint(self, head: TreeNode) -> list:
        # curr_node = head
        # stack = []
        # result = []
        # while curr_node.left.left:
        #     curr_node = curr_node.left

        #similarly it travers like left,right,root
        #edge cases will be empty tree and one node

        if head is None:
            return None
        if head.left is None and head.right is None:
            return head.val
        stack = Stack()
        result = []
        last_visited = None 
        curr_node = head

        while stack.stack or curr_node:
            if curr_node:
                stack.add(curr_node)
                curr_node = curr_node.left #adding all the left nodes first because we need to print first left,right,node 
            else:
                peek_node = stack.stack[-1]
                if peek_node.right and last_visited != peek_node.right:
                    curr_node = peek_node.right
                else:
                    result.append(peek_node.val)
                    last_visited = stack.pop()
        
        return result

        # pass


class Stack:
    # Implement your stack using either an array or a list
    # (i.e., implement the functions based on the Stack ADT we covered in class)
    # You may use Python's list structure as the underlying storage.
    # While you can use .append() to add elements, please ensure the implementation strictly follows the logic we discussed in class
    # (e.g., manually managing the "top" of the stack
    
    # Use your own stack implementation to solve problem 3

    def __init__(self):
        #so i'm using list to create and then poping using list inbuilt methods
        self.stack = []
        # TODO: initialize the stack
        pass
    def pop(self,):
        return self.stack.pop(-1)
    
    def add(self,val):
        return self.stack.append(val)
    

    # Problem 3: Write code to evaluate a postfix expression using stack and return the integer value
    # Use stack which you implemented above for this problem

    # input -> a postfix expression string. E.g.: "5 1 2 + 4 * + 3 -"
    # see the examples of test entries in p3_eval_postfix.csv
    # output -> integer value after evaluating the string. Here: 14

    # integers are positive and negative
    # support basic operators: +, -, *, /
    # handle division by zero appropriately

    # DO NOT USE EVAL function for evaluating the expression

    def evaluatePostfix(self,exp: str) -> int:

        if exp is None:
            return 0
        values = exp.split()
        operaions = "+-*/"
        for value in values:
            if value in operaions and len(value) ==1:

                if len(self.stack) < 2:
                    raise ValueError("Malformed postfix: insufficient operands before operator {}".format(value))

                right = int(self.pop()) #here order matters we are popping right first and then left
                left = int(self.pop())

                if value== "+":
                    self.add(left + right)
                elif value=="-":
                    self.add(left - right)
                elif value=="*":
                    self.add(left * right)
                elif value=="/":
                    if right==0: # here if the denominator is Zero in that case we will return without doing division
                        raise ZeroDivisionError('division by Zero')
                    self.add((left/right))
            else:
                try:
                    value = int(value) # If it's not an int and not a supported operator, it's invalid
                except ValueError:
                    if value in operaions:
                        raise ValueError('invalid Operation {}'.format(value))
                self.add(value)
        return self.pop()
        # TODO: implement this using your Stack class
        # pass


# Main Function. Do not edit the code below
if __name__ == "__main__":
    homework2 = HomeWork2()

    print("\nRUNNING TEST CASES FOR PROBLEM 1")
    testcases = []
    try:
        with open('p1_construct_tree.csv', 'r') as f:
            testcases = list(csv.reader(f))
    except FileNotFoundError:
        print("p1_construct_tree.csv not found")

    for i, (postfix_input,) in enumerate(testcases, 1):
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)
        output = homework2.postfixNotationPrint(root)

        assert output == postfix, f"P1 Test {i} failed: tree structure incorrect"
        print(f"P1 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 2")
    testcases = []
    with open('p2_traversals.csv', 'r') as f:
        testcases = list(csv.reader(f))

    for i, row in enumerate(testcases, 1):
        postfix_input, exp_pre, exp_in, exp_post = row
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)
        

        assert homework2.prefixNotationPrint(root) == exp_pre.split(","), f"P2-{i} prefix failed"
        assert homework2.infixNotationPrint(root) == exp_in.split(","), f"P2-{i} infix failed"
        assert homework2.postfixNotationPrint(root) == exp_post.split(","), f"P2-{i} postfix failed"

        print(f"P2 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 3")
    testcases = []
    try:
        with open('p3_eval_postfix.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                testcases.append(row)
    except FileNotFoundError:
        print("p3_eval_postfix.csv not found")

    for idx, row in enumerate(testcases, start=1):
        expr, expected = row

        try:
            s = Stack()
            result = s.evaluatePostfix(expr)
            if expected == "DIVZERO":
                print(f"Test {idx} failed (expected division by zero)")
            else:
                expected = int(expected)
                assert result == expected, f"Test {idx} failed: {result} != {expected}"
                print(f"Test case {idx} passed")

        except ZeroDivisionError:
            assert expected == "DIVZERO", f"Test {idx} unexpected division by zero"
            print(f"Test case {idx} passed (division by zero handled)")