# -*- coding: utf-8 -*-
"""stacks.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IkuNRP1ytykTj-FXWEk3x-ye-q9w0k3m
"""

stack = [1,2,3,4,5]

stack

stack.append(6)

stack

stack.pop()

stack

stack[-1]

class Stack:
  def __init__(self,size):
    self.size = size
    self.stack = [None] * self.size
    self.top = -1

  def push(self,value):
    if self.top == self.size - 1:
      return "Overflow"
    else:
      self.top += 1
      self.stack[self.top] = value

  def pop(self):
    if self.top == -1:
      return "Empty"
    else:
      data = self.stack[self.top]
      self.top -= 1
      print(data)

  def display(self):
    for i in range(self.top + 1):
      print(self.stack[i],end=' ')

S = Stack(4)

S.stack

S.display()

S.push(3)

S.pop()

"""**Easy**

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map:
            top_element = stack.pop()
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

print(isValid("({[]]})"))

"""**Hard**

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
"""

class Solution:
    def calculate(self, s: str) -> int:
        number = 0
        sign_value = 1
        result = 0
        operations_stack = []
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c in "+-":
                result += number * sign_value
                sign_value = -1 if c == '-' else 1
                number = 0
            elif c == '(':
                operations_stack.append(result)
                operations_stack.append(sign_value)
                result = 0
                sign_value = 1
            elif c == ')':
                result += sign_value * number
                result *= operations_stack.pop()
                result += operations_stack.pop()
                number = 0
        return result + number * sign_value

sol = Solution()
print(sol.calculate("27+2+(16-4)-6+(21-7+3)+10"))
print(sol.calculate("2+5+3-7-1+4"))