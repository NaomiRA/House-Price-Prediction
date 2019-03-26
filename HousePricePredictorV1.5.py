import csv

SalePriceY = []
GrLivAreaX1 = []
OverallQualX2 = []
TestGrLivAreaX1 = []
TestOverallQualX2 = []
IdList = []
PredictedY = []

with open("GrLivAreaOverallQual.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t")
    for row in rd:
        SalePriceY.append(int(row[0]))
        GrLivAreaX1.append(int(row[1]))
        OverallQualX2.append(int(row[2]))
        #print(row)

with open("TestGrLivAreaOverallQual.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t")
    for row in rd:
        IdList.append(int(row[0]))
        TestGrLivAreaX1.append(int(row[1]))
        TestOverallQualX2.append(int(row[2]))
        #print(row)

n = len(SalePriceY)
xbar = sum(GrLivAreaX1)/n
x2bar = sum(OverallQualX2)/n
ybar = sum(SalePriceY)/n
SS_xy = 0
SS_x2y = 0
SS_xx = 0
SS_x2x2 = 0
SS_xx2 = 0

#SS_x1y - sum of products
for i in range(n):
    Sxy = (GrLivAreaX1[i] - xbar)*(SalePriceY[i] - ybar)
    SS_xy = SS_xy + Sxy
 

#SS_x1x1 - sum of squares
for i in range(n):
    Sxx = (GrLivAreaX1[i] - xbar)**2
    SS_xx = SS_xx + Sxx

#SS_x2y - sum of products
for i in range(n):
    Sx2y = (OverallQualX2[i] - x2bar)*(SalePriceY[i] - ybar)
    SS_x2y = SS_x2y + Sx2y
 

#SS_x2x2 - sum of squares
for i in range(n):
    Sx2x2 = (OverallQualX2[i] - x2bar)**2
    SS_x2x2 = SS_x2x2 + Sx2x2

#SS_x1x2 - sum of products
for i in range(n):
    Sxx2 = (GrLivAreaX1[i] - xbar)*(OverallQualX2[i] - x2bar)
    SS_xx2 = SS_xx2 + Sxx2

B_1 = (SS_xy * SS_x2x2 - SS_xx2 * SS_x2y) / (SS_xx * SS_x2x2 - SS_xx2 * SS_xx2)
B_2 = (SS_x2y * SS_xx - SS_xx2 * SS_xy) / (SS_xx * SS_x2x2 - SS_xx2 * SS_xx2)
B_0 = ybar - B_1 * xbar - B_2 * x2bar

print("b_0 = ", B_0)
print("b_1 = ", B_1)
print("b_2 = ", B_2)
print("Linear Regression Equation:\ny = ",round(B_1,2), "x + ",round(B_2,2),"x + ",round(B_0,2))

for i in range(len(IdList)):
    Y = B_1 * TestGrLivAreaX1[i] + B_2 * TestOverallQualX2[i] + B_0
    PredictedY.append(round(Y))
for y in PredictedY:
    print(y)
