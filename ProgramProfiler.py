import numpy as np
import os
from numpy import linalg as LA
from scipy.interpolate import CubicSpline

keys = { #key words point to key concepts. if/else/elif all have values of 4 as they are all conditionals.
    "def __init": 0,
    "def": 1,
    "import": 2,
    "while": 3,
    "for": 3,
    "if": 4,
    "else": 4,
    "elif": 4,
    "@property": 5,
    "print": 6,
    "class": 7,
    "#": 8,
    ".setter": 9,
    "=":10
}

def FrobNorm(programProfile, newProg): #from norm, aka euclidean distance. A way of measuring similarity between matrices
    profileNorm = LA.norm(programProfile)  
    programNorm = LA.norm(newProg)
    print("The profile's norm: {}".format(profileNorm))
    print("The current program's norm:{}".format(programNorm))
    print("Comparison value: {}".format(abs(profileNorm-programNorm))) #the differences in the norms tells us how close in similarity they are to each other. 0 is the closest similarity.

def interp_matrix(matrix, max_length): #Add values to matrix to assure its length is the int given by "max_length"
    indices = np.arange(matrix.shape[0])
    spline = [CubicSpline(indices,matrix[:,i]) for i in range(matrix.shape[1])] 
    new_indices = np.linspace(0,indices[-1], max_length)
    interpolated_matrix = np.vstack([interp(new_indices) for interp in spline])
    return(interpolated_matrix)

def createProgramMatrices():
    os.chdir(r'folder')
    allMatrices = []
    for file in os.listdir(): #iterate through each file in folder
        studentFile = open(file).read().split("\n")
        indivMatrix = np.zeros((len(studentFile),11)) #n by m matrix, n = numLines; m=num of key programming practices as defined by keys
        StudentSimplified = []
        lineArr = []
        lineNum = 0
        for line in studentFile:
            line = line.strip()
            line = line.lower()
            hadKey = False
            for key in keys: 
                if key in line: #when a line of code is using one of the predefined keywords, change entry at row lineNum, col key from 0 to 1
                        indivMatrix[lineNum][keys[key]] = 1
            lineNum+=1
            StudentSimplified.append(lineArr)
            lineArr = []
        np.set_printoptions(threshold=np.inf)
        allMatrices.append(indivMatrix)
    return allMatrices #returns a list of each program transformed to a matrix

def toProgramProfile(programMatrices): #converts a list of program matrices into a single matrix, or a "program profile"
    max_program_length = max(matrix.shape[0] for matrix in programMatrices) #find longest prog
    for matrixIndex in range(len(programMatrices)): #interpolate them to each be the length of the longest program
        programMatrices[matrixIndex] = interp_matrix(programMatrices[matrixIndex],max_program_length)
    numMatrices = len(programMatrices)
    overall_matrix_weighted = np.divide(programMatrices[0], numMatrices) #weigh each matrix by the number of files in the folder and sum them
    for matrixIndex in range(1,len(programMatrices)):
        overall_matrix_weighted = np.add(overall_matrix_weighted, np.divide(programMatrices[matrixIndex],numMatrices))

    return(overall_matrix_weighted) #returns a single numpy matrix, or the "program profile"
    
def curToMatrix(file,maxLines=None): #converts a single file into a program matrix
    testMat = np.zeros((len(file),len(keys)))
    StudentSimplified = []
    lineArr = []
    lineNum = 0
    for line in file:
        line = line.strip()
        line = line.lower()
        for key in keys:
            if key in line:
                    testMat[lineNum][keys[key]] = 1
        lineNum+=1
        StudentSimplified.append(lineArr)
        lineArr = []
    if maxLines == None: 
        return(testMat)
    else: #will be used if user wants to add this program to the program profile.
        testMatInterp = interp_matrix(testMat,maxLines) 
        return(testMatInterp)
