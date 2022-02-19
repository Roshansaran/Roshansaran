#bubble sort
#first we have list create and input
list=[2,4,5,6,7,8,78,46,67,32,43]
for i in range(0,len(list)):
    print(list[i])
  
for j in range(0,len(list)):
    for i in range(0,len(list)-1):
        if(list[i]>list[i+1]):
            list[i],list[i+1]=list[i+1],list[i]
            print(list[i],list[i+1])
for i in range(0,len(list)):
    print(list[i])
    