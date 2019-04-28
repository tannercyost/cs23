import sys
import subprocess
import timeit
import math

n0 = 1024
n1 = 4096
programName = sys.argv[1]
#Here I have some growth constants I obtained experimentally
#n1 is 4 times as large as n0 so these constants are based off of that.
#i.e. for each of these growth patterns, if you increase your n by a factor of 4, your time to execute will increase by a factor of these constants
#I based this around making the linear constant a 1.00 because it made the numbers look nice
constant = 0.00
log = 0.10
linear = 1.00
linearithmic = 1.35
quadratic = 4.67
cubic = 20.00
#later in the program I have timeit run 2 tests, but to keep the execution time shorter this makes it so if it is testing cubic times it only runs it once.
#the cubic constant is so large that you do not really need to run it twice to see that it is a cubic, and I account for this with large tolerances at the end.
if(programName == "cs23_as10_cubic"):
    x = 1
else:
    x = 2

def callFunction(programName, nValue):
    subprocess.call([programName, str(nValue)])

time1 = timeit.timeit(stmt='callFunction(programName, n0)', setup="from __main__ import callFunction, programName, n0", number=x)/x
time2 = timeit.timeit(stmt='callFunction(programName, n1)', setup="from __main__ import callFunction, programName, n1", number=x)/x
diff = abs(round(time2 - time1, 2))

constDiff = abs(constant - diff)
logDiff = abs(log - diff)
linearDiff = abs(linear - diff)
linearithmicDiff = abs(linearithmic - diff)
quadraticDiff = abs(quadratic - diff)
cubicDiff = abs(cubic - diff)
print(linearDiff)
#for larger n's your tolerance can be greater.
#see that for cubic, the tolerance is 1. For quadratic, it is .1.
if(math.isclose(constDiff, 0, rel_tol=1e-5)):
    print("O(1)")
elif(math.isclose(logDiff, 0, abs_tol=0.05)):
    print("O(log n)")
elif(math.isclose(linearDiff, 0, abs_tol=0.15)):
    print("O(n)")
elif(math.isclose(linearithmicDiff, 0, abs_tol=0.0999)):
    print("O(n log n)")
elif(math.isclose(quadraticDiff, 0, abs_tol=0.1)):
    print("O(n^2)")
elif(math.isclose(cubicDiff, 0, abs_tol=1.00)):
    print("O(n^3)")
