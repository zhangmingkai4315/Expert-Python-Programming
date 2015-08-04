# number=range(10000)
# size=len(number)
# events=[]
# i=0
# while i<size:
#     if(i%2==0):
#         events.append(i)
#     i=i+1
# events[100]
# [Finished in 1.001s]


# events=[i for i in range(10000) if i%2==0]
# print events[100]

seq=["one","two","three"]
for i ,element in enumerate(seq):
    print "%d is %s"%(i,element)

