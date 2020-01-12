# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    sizeOfQueue = int(input())
    queueArray = list(map(int,input().split()))
    #print(sizeOfQueue, *queueArray)
    bribe = 0
    result = ''
    position = sizeOfQueue
    #for x in range(sizeOfQueue -1,-1,-1):
        #print(x,queueArray[x],queueArray[x-1])
        #if (queueArray[x]  - (x + 1) )  > 2:
            #result='Too chaotic'
            #break
        #for i in range(x):
            #print(x,i,queueArray[i],queueArray[x])
            #if queueArray[i] > queueArray[x]:
                #bribe += 1
    queue = [p - 1 for p in queueArray]

    for i,P in enumerate(queue):
        if P - i >2:
            result = 'Too chaotic'
        for j in range(max(P-1,0),i):
            if queue[j] > P:
                bribe += 1

    if result == 'Too chaotic':
        print('Too chaotic')
    else:
        print(bribe)
        
