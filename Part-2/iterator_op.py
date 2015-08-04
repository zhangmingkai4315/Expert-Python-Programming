# class MyIterator(object):
#     def __init__(self,step):
#         self.step=step
#     def next(self):
#         if self.step==0:
#             raise StopIteration
#         self.step-=1
#         return self.step
#     def __iter__(self):
#         return self
# for el in MyIterator(4):
#     print el


# class yrange(object):
#     def __init__(self,n):
#         self.i=0
#         self.n=n
#     def __iter__(self):
#         return self
#     def next(self):
#         if(self.i<self.n):
#             i=self.i
#             self.i+=1
#             return i;
#         else:
#             raise StopIteration()
#
# y=yrange(10)
# for i in yrange(10):
#     print i
#
# # return null because same object
# list(y)



def readFile(filename):
    for line in open(filename):
        yield line
def printline(lines):
    for line in lines:
        print line

for line in readFile("list_op.py"):
    print "yield"
    print(line)



