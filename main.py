import numpy as np
import os
from ProgramProfiler import *

np.set_printoptions(threshold=np.inf)
testf = open(r'student2.txt').read().split("\n") #testfile

programMatrices = createProgramMatrices()
print(1)
progProf = toProgramProfile(programMatrices)
print(2)

testMat = curToMatrix(testf,138)
print(3)
FrobNorm(progProf,testMat)









