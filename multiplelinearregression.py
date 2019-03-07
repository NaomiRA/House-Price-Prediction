"""
Sum of squares (SSX1) = 82.5
Sum of squares (SSX2) = 132
Sum of products (SPX1Y) = 96.5
Sum of products (SPX2Y) = 120
Sum of products (SPX1X2) = 103

Regression Equation = ŷ = b1X1 + b2X2 + a

b1 = ((SPX1Y)*(SSX2)-(SPX1X2)*(SPX2Y)) / ((SSX1)*(SSX2)-(SPX1X2)*(SPX1X2)) = 378/281 = 1.3452

b2 = ((SPX2Y)*(SSX1)-(SPX1X2)*(SPX1Y)) / ((SSX1)*(SSX2)-(SPX1X2)*(SPX1X2)) = -39.5/281 = -0.14057

a = MY - b1*MX1 - b2*MX2 = 6.5 - (1.35*4.5) - (-0.14*7) = 1.4306

ŷ = 1.3452X1 - 0.14057X2 + 1.4306
"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x2 = [1, 2, 4, 6, 7, 7, 9, 11, 11, 12]
y = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]

n = len(x)
xbar = sum(x)/n
x2bar = sum(x2)/n
ybar = sum(y)/n
SS_xy = 0
SS_x2y = 0
SS_xx = 0
SS_x2x2 = 0
SS_xx2 = 0

#SS_x1y - sum of products
for i in range(n):
    Sxy = (x[i] - xbar)*(y[i] - ybar)
    SS_xy = SS_xy + Sxy
 

#SS_x1x1 - sum of squares
for i in range(n):
    Sxx = (x[i] - xbar)**2
    SS_xx = SS_xx + Sxx

#SS_x2y - sum of products
for i in range(n):
    Sx2y = (x2[i] - x2bar)*(y[i] - ybar)
    SS_x2y = SS_x2y + Sx2y
 

#SS_x2x2 - sum of squares
for i in range(n):
    Sx2x2 = (x2[i] - x2bar)**2
    SS_x2x2 = SS_x2x2 + Sx2x2

#SS_x1x2 - sum of products
for i in range(n):
    Sxx2 = (x[i] - xbar)*(x2[i] - x2bar)
    SS_xx2 = SS_xx2 + Sxx2

B_1 = (SS_xy * SS_x2x2 - SS_xx2 * SS_x2y) / (SS_xx * SS_x2x2 - SS_xx2 * SS_xx2)
B_2 = (SS_x2y * SS_xx - SS_xx2 * SS_xy) / (SS_xx * SS_x2x2 - SS_xx2 * SS_xx2)
B_0 = ybar - B_1 * xbar - B_2 * x2bar

print("b_0 = ", B_0)
print("b_1 = ", B_1)
print("b_2 = ", B_2)
print("Linear Regression Equation:\ny = ",round(B_1,2), "x + ",round(B_2,2),"x + ",round(B_0,2))
