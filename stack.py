# from collections import deque

# class stack:
#     def __init__(self):
#         self.que = deque()
#     def push(self,key):
#         return self.que.append(key)

#     def pop(self):
#         return self.que.pop()

#     def show(self):
#         print(self.que)

#     def peek(self):
#         print(self.que[-1])

#     def get_length(self):
#         return len(self.que)

#     def is_empty(self):
#         return len(self.que)==0

# def reverse_string(string):
#     Stack = stack()
#     for cha in string:
#         Stack.push(cha)
#     rstr = ""
#     while Stack.get_length()!=0:
#         rstr+=Stack.pop()

#     print(rstr)

# def is_match(ch1,ch2):
#     disctionary = {
#         ')':'(',
#         ']':'[',
#         '}':'{'  
#     }

#     return disctionary[ch1] == ch2

# def is_balanced(s):
#     sstack = stack()
#     for cha  in s:
#         if '{' == cha or '[' == cha or '('==cha:
#             sstack.push(cha)
#         if '}' == cha or ']' == cha or ')'==cha:
#             if sstack.get_length() == 0:
#                 return False
#             if not is_match(cha,sstack.pop()):
#                 return False

#     return sstack.get_length ==0
    
# print(is_balanced("([[a]]"))


# main.py

