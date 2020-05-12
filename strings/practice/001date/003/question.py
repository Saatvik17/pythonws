for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    print("Case #"+str(_+1)+": ",end="")
    answer = 0
    for i in range(1,n-1):
        if l1[i] > l1[i-1] and l1[i] > l1[i+1]:
            answer +=1
    print(answer)