import csv

def ReadInTrainingData():
    SalePriceY = []
    GrLivAreaX1 = []
    OverallQualX2 = []
    with open("GrLivAreaOverallQual.tsv") as fd:
        rd = csv.reader(fd, delimiter="\t")
        for row in rd:
            SalePriceY.append(int(row[0]))
            GrLivAreaX1.append(int(row[1]))
            OverallQualX2.append(int(row[2]))
    return(SalePriceY, GrLivAreaX1, OverallQualX2)
        

def ReadInTestData():
    TestGrLivAreaX1 = []
    TestOverallQualX2 = []
    IdList = []
    with open("TestGrLivAreaOverallQual.tsv") as fd:
        rd = csv.reader(fd, delimiter="\t")
        for row in rd:
            IdList.append(int(row[0]))
            TestGrLivAreaX1.append(int(row[1]))
            TestOverallQualX2.append(int(row[2]))
    return(IdList, TestGrLivAreaX1, TestOverallQualX2)


def CalcRegressionFormula(Y,X1,X2):
    n = len(Y)
    xbar = sum(X1)/n
    x2bar = sum(X2)/n
    ybar = sum(Y)/n
    SS_xy = 0
    SS_x2y = 0
    SS_xx = 0
    SS_x2x2 = 0
    SS_xx2 = 0
    #SS_x1y - sum of products
    for i in range(n):
        Sxy = (X1[i] - xbar)*(Y[i] - ybar)
        SS_xy = SS_xy + Sxy
 

    #SS_x1x1 - sum of squares
    for i in range(n):
        Sxx = (X1[i] - xbar)**2
        SS_xx = SS_xx + Sxx

    #SS_x2y - sum of products
    for i in range(n):
        Sx2y = (X2[i] - x2bar)*(Y[i] - ybar)
        SS_x2y = SS_x2y + Sx2y
 

    #SS_x2x2 - sum of squares
    for i in range(n):
        Sx2x2 = (X2[i] - x2bar)**2
        SS_x2x2 = SS_x2x2 + Sx2x2

    #SS_x1x2 - sum of products
    for i in range(n):
        Sxx2 = (X1[i] - xbar)*(X2[i] - x2bar)
        SS_xx2 = SS_xx2 + Sxx2


    B_1 = (SS_xy * SS_x2x2 - SS_xx2 * SS_x2y) / (SS_xx * SS_x2x2 - SS_xx2 * SS_xx2)
    B_2 = (SS_x2y * SS_xx - SS_xx2 * SS_xy) / (SS_xx * SS_x2x2 - SS_xx2 * SS_xx2)
    B_0 = ybar - B_1 * xbar - B_2 * x2bar

    return(B_1, B_2, B_0)

def OutputRegressionFormula(B_1,B_2,B_0):
    print("b_0 = ", B_0)
    print("b_1 = ", B_1)
    print("b_2 = ", B_2)
    print("Linear Regression Equation:\ny = ",round(B_1,2), "x + ",round(B_2,2),"x + ",round(B_0,2))

def PredictY(IdList,X1,X2):
    PredictedY = []
    for i in range(len(IdList)):
        Y = B_1 * X1[i] + B_2 * X2[i] + B_0
        PredictedY.append(round(Y))
    return(PredictedY)
    #for y in PredictedY:
        #print(y)
    
def WriteToFile(PredictedY,IdList):
    with open('PredictedHousePrices.csv', mode = 'w') as csvfile:
        wr = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(IdList)):
            wr.writerow([IdList[i], PredictedY[i]])









TrainY, TrainX1, TrainX2 = ReadInTrainingData()
B_1, B_2, B_0 = CalcRegressionFormula(TrainY,TrainX1,TrainX2)
OutputRegressionFormula(B_1,B_2,B_0)
IdList,TestX1,TestX2 = ReadInTestData()
PredictedY = PredictY(IdList,TestX1,TestX2)
WriteToFile(PredictedY,IdList)

