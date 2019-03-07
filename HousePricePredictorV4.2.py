"""
House Price Predictor v4.1

Created by Naomi 1803688 9/2/19

This program:
> Predicts the price of a house using the multiple linear regression model.
> Uses the least squares method to calculate the regression model.
> Uses the Ames Housing dataset.
> Outputs predicted sale prices into a .csv file "PredictedHousePrices.csv"
> Uses 2 features;
        - GrLivArea (Above grade (ground) living area square feet)
        - LotArea (Lot size in square feet)
"""
import csv

def ReadInTrainingData():
    """
    Read in the training data from a .csv file.
    Append each column to its own list.
    """
    SalePriceY = []
    GrLivAreaX1 = []
    LotAreaX2 = [] ### NEEDS A TRY CATCH BLOCK
    with open("InputTrainingData.csv") as fd:
        rd = csv.reader(fd, delimiter=",")
        for row in rd:
            SalePriceY.append(int(row[0]))
            GrLivAreaX1.append(int(row[1]))
            LotAreaX2.append(int(row[2]))
    return(SalePriceY, GrLivAreaX1, LotAreaX2)
        

def ReadInTestData():
    """
    Read in the test data from a .csv file.
    Append each column to its own list.
    """
    TestGrLivAreaX1 = []
    TestLotAreaX2 = []
    IdList = [] ### try catch block plz
    with open("InputTestData.csv") as fd:
        rd = csv.reader(fd, delimiter=",")
        for row in rd:
            IdList.append(int(row[0]))
            TestGrLivAreaX1.append(int(row[1]))
            TestLotAreaX2.append(int(row[2]))
    return(IdList, TestGrLivAreaX1, TestLotAreaX2)


def CalcRegressionFormula(Y,X1,X2):
    """
    Calculates the linear regression formula using the least squares method.
    xbar and ybar is the average of their respective lists.
    """
    n = len(Y)
    xbar = sum(X1)/n
    x2bar = sum(X2)/n
    ybar = sum(Y)/n
    SP_x1y = 0
    SP_x2y = 0
    SS_xx = 0
    SS_x2x2 = 0
    SP_x1x2 = 0
    
    #SS_x1y - sum of products
    for i in range(n):
        Sxy = (X1[i] - xbar)*(Y[i] - ybar)
        SP_x1y = SP_x1y + Sxy

    #SS_x1x1 - sum of squares
    for i in range(n):
        Sxx = (X1[i] - xbar)**2
        SS_xx = SS_xx + Sxx

    #SP_x2y - sum of products
    for i in range(n):
        Sx2y = (X2[i] - x2bar)*(Y[i] - ybar)
        SP_x2y = SP_x2y + Sx2y
 
    #SS_x2x2 - sum of squares
    for i in range(n):
        Sx2x2 = (X2[i] - x2bar)**2
        SS_x2x2 = SS_x2x2 + Sx2x2

    #SS_x1x2 - sum of products
    for i in range(n):
        Sxx2 = (X1[i] - xbar)*(X2[i] - x2bar)
        SP_x1x2 = SP_x1x2 + Sxx2

    B_1 = (SP_x1y * SS_x2x2 - SP_x1x2 * SP_x2y) / (SS_xx * SS_x2x2 - SP_x1x2 * SP_x1x2)
    B_2 = (SP_x2y * SS_xx - SP_x1x2 * SP_x1y) / (SS_xx * SS_x2x2 - SP_x1x2 * SP_x1x2)
    B_0 = ybar - B_1 * xbar - B_2 * x2bar

    return(B_1, B_2, B_0)

def OutputRegressionFormula(B_1,B_2,B_0):
    """
    Displays the regression formula for testing purposes.
    Online regression calculators can be used to verify that the program
    is working correctly by comparing the formulas.
    """
    print("b_0 = ", B_0)
    print("b_1 = ", B_1)
    print("b_2 = ", B_2)
    print("Linear Regression Equation:\ny = ",round(B_1,2), "x + ",round(B_2,2),"x + ",round(B_0,2))

def PredictY(IdList,X1,X2):
    """
    Predict the values of y by applying the regression formula
    to each value of X_1 and X_2.
    Append each predicted y to a list and return it.
    """
    PredictedY = []
    for i in range(len(IdList)):
        Y = B_1 * X1[i] + B_2 * X2[i] + B_0
        PredictedY.append(round(Y))
    return(PredictedY)

    
def WriteToFile(PredictedY,IdList):
    """
    Write each house ID and predicted y value to a .csv file.
    """
    with open('OutputPredictedHousePrices.csv', mode = 'w') as csvfile:
        wr = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        wr.writerow(['Id','SalePrice'])
        for i in range(len(IdList)):
            wr.writerow([IdList[i], PredictedY[i]])


"""
Main Program
"""
TrainY, TrainX1, TrainX2 = ReadInTrainingData()
B_1, B_2, B_0 = CalcRegressionFormula(TrainY,TrainX1,TrainX2)
IdList,TestX1,TestX2 = ReadInTestData()
PredictedY = PredictY(IdList,TestX1,TestX2)
WriteToFile(PredictedY,IdList)

