import numpy as np
import os
from ProgramProfiler import *

np.set_printoptions(threshold=np.inf)
testf = open(r'student.txt').read().split("\n") #testfile

programMatrices = createProgramMatrices()
progProf = toProgramProfile(programMatrices)

testMat = curToMatrix(testf,138)
FrobNorm(progProf,testMat)









