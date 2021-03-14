#Playing with the copy function
import unittest
x=[[1,2,3],[4,5]]
import copy
def CopyX(x):  
    y= copy.copy(x)
    z= copy.copy(x)
    y[0][1]=6
    z[1] = 6
    return [y,z]
y=CopyX(x)[0]
z=CopyX(x)[1]
print("This is testing and experimenting with the copy function.")
print(x)
print(y)
print(z)
print("")
class CopyTest(unittest.TestCase):
    def test(self):
        test_x= test_x=[[1,8,3],[2,4]]
        self.assertEqual(CopyX(test_x)[0],[[1,6,3],[2,4]])
        self.assertEqual(CopyX(test_x)[1],[[1,6,3],6])
if __name__=='__main__':
     unittest.main()

#Using the data set I made before for itertools operations
#Part one: using intertools.cycle
print("Testing intertools.cycle:")
import unittest
import itertools
def cycle_x(num):
    counter = 0
    cyclelist = []
    for i in itertools.cycle(num):
        cyclelist.append(i),
        counter = counter+1
        if counter>5:
            return cyclelist
            break
            
cycle_x(x)
print("")
print("Test Answer:")
class CycleTest(unittest.TestCase):
    def test(self):
        test_x= [[1,5,7],[4,9]]
        self.assertEqual(cycle_x(test_x),[[1,5,7],[4,9],[1,5,7],[4,9],[1,5,7],[4,9]])
        
if __name__=='__main__':
     unittest.main()
#Part two: using itertools.repeat
print("Testing intertools.repeat:")
import itertools
import unittest
def repeat_x(x):
    result = list(itertools.repeat(x,3))
    return result
repeat_x(x)
class RepeatTest(unittest.TestCase):
    def test(self):
        test_x= [[1,5,7],[4,9]]
        self.assertEqual(repeat_x(test_x), [[[1,5,7],[4,9]],[[1,5,7],[4,9]],[[1,5,7],[4,9]]])
if __name__=='__main__':
     unittest.main()        
     

