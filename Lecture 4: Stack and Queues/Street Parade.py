while True:
    #take the input
    n = int(input())
    if n == 0:
        break
    trucks = list(map(int, input().split()))
    #initiate stack structure
    stack = []
    #initiate a temporary value for checking
    order = 1
    i = 0

    #loop through the input array
    while i < n:
        #if the truck match with the order we need
        if trucks[i] == order:
            #increase to get to the next needed order
            order += 1
            #continue the loop
            i += 1
        #else if the one we need is in the stack
        #check if stack not empty and the end value is the order we need
        elif stack and stack[-1] == order:
            #increse to get to the next needed order
            order += 1
            #pop the element from the stack
            stack.pop()
        #else we add the current truck into the stack
        else:
            stack.append(trucks[i])
            i += 1
    #After finish, we check what is left in the stack if they satisfy the order we need
    while stack and stack[-1] == order:
        order += 1
        stack.pop()
    #if order reaches n+1 then we're good (since we initite order = 1 instead of 0)
    print('yes' if order == n+1 else 'no')




