from stack_sample import Stack
import logging


sl = ( 
   "{(foo)(bar)}[hello](((this)is)a)test", 
   "{(foo)(bar)}[hello](((this)is)atest", 
   "{(foo)(bar)}[hello](((this)is)a)test))" 
) 

def check_match_brackets(stmt):
    stack = Stack()
    for ch in stmt:
        if ch in ['(','{','[']:
            stack.push(ch)
        if ch in [')','}',']']:
            pop = stack.pop()
            if ch == ')' and pop == '(':
                continue
            elif ch is '}' and pop is '{':
                continue
            elif ch is ']' and pop is '[':
                continue
            else:
                # print('**{}{}'.format(pop, ch))
                return False

    if stack.count > 0: 
        return False 
    else: 
        return True 


for row in sl:
    print('No Mismatch') if check_match_brackets(row) else print('{} ** Mismatch ***'.format(row))
