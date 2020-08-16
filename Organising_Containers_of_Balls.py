POSSIBLE= "Possible"
IMPOSSIBLE="Impossible"

def organizingContainers(container):
    print(container)
    
    countByType=[0]* len(container[0])
    countByContainer=[sum(x) for x in container]
    print(countByContainer)
    for Ci in container: 
        print ("Ci=", Ci)
        for j in range(len(Ci)):
            print(" j=",j)
            countByType[j]+=Ci[j]

    countByContainer.sort()
    countByType.sort()
    print('Count By Types:',countByType)
    print('Count By Container:',countByContainer)
    return POSSIBLE if countByContainer==countByType else IMPOSSIBLE

print(organizingContainers([[1,1],[2,2]]))