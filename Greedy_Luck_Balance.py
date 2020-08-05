def luckBalance(k, contests):
    contests.sort(key = lambda x: [x[1],x[0]], reverse = True) 
    print(contests)
    luck = 0
    count = 0
    for i in contests: 
        if i[1] == 1 and count < k:
            luck += i[0]
            count += 1
        elif i[1] == 1 and count >= k:
            luck -= i[0]
        elif i[1] == 0:
            luck += i[0] 


luckBalance(3,[[5,1],[2,1],[1,1],[8,1],[10,0],[5,0]])