
'''
Main Program for the program profiler
replace 'student.txt' with whichever program you choose to comparet to the program profile
add a folder of past student's work the main directory
main.py will output the distance between the program profile produced by the folder and the test file
'''
import numpy as np
import os
from ProgramProfiler import *

testf = open(r'student.txt').read().split("\n") #The file you are choosing to compare replaces "student.txt"

programMatrices = createProgramMatrices() #converts contents of folder to a list of matrices
progProf = toProgramProfile(programMatrices) #converts list of matrices to program profile

testMat = curToMatrix(testf) #convert single test file into a matrix
FrobNorm(progProf,testMat) #compare the norms 









