# def yrange(n):
#     i=0
#     while i<n:
#         yield i
#         i+=1
# y=yrange(4)
# # print y
# print y.next()
# print y.next()
# print y.next()
# print y.next()
# print y.next()


def myCustomerGenerator():
    print("Start Generator")
    i=0
    while(i<10):
        yield i
        i+=1

m=myCustomerGenerator()

for i in m:
    print i