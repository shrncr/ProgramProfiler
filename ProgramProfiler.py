import numpy as np
import os
from numpy import linalg as LA
from scipy.interpolate import CubicSpline

keys = { #key words
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

def FrobNorm(programProfile, newProg):
    #maybe add a shape check to make sure rows = 14
    #wait i might not need that
    profileNorm = LA.norm(programProfile)
    programNorm = LA.norm(newProg)
    print("The profile's norm: {}".format(profileNorm))
    print("The current program's norm:{}".format(programNorm))
    print("Comparison value: {}".format(abs(profileNorm-programNorm)))

def interp_matrix(matrix, max_length): #change size of matrix
    indices = np.arange(matrix.shape[0])
    spline = [CubicSpline(indices,matrix[:,i]) for i in range(matrix.shape[1])]
    new_indices = np.linspace(0,indices[-1], max_length)
    interpolated_matrix = np.vstack([interp(new_indices) for interp in spline])
    return(interpolated_matrix)

def createProgramMatrices():
    os.chdir(r'folder')
    allMatrices = []

    for file in os.listdir(): #turn each prog file into matrix
        studentFile = open(file).read().split("\n")
        indivMatrix = np.zeros((len(studentFile),len(keys)))
        StudentSimplified = []
        lineArr = []
        lineNum = 0
        for line in studentFile:
            line = line.strip()
            line = line.lower()
            hadKey = False
            for key in keys:
                if key in line:
                        indivMatrix[lineNum][keys[key]] = 1
            lineNum+=1
            StudentSimplified.append(lineArr)
            lineArr = []
        np.set_printoptions(threshold=np.inf)
        allMatrices.append(indivMatrix)
    return allMatrices

def toProgramProfile(programMatrices):
    max_program_length = max(matrix.shape[0] for matrix in programMatrices) #find longest prog
    for matrixIndex in range(len(programMatrices)): #interpolate them
        programMatrices[matrixIndex] = interp_matrix(programMatrices[matrixIndex],max_program_length)
    numMatrices = len(programMatrices)
    overall_matrix_weighted = np.divide(programMatrices[0], numMatrices) 
    for matrixIndex in range(1,len(programMatrices)):
        overall_matrix_weighted = np.add(overall_matrix_weighted, np.divide(programMatrices[matrixIndex],numMatrices))

    return(overall_matrix_weighted)
    
def curToMatrix(file,maxLines):
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
    testMatInterp = interp_matrix(testMat,maxLines)
    return(testMatInterp)
