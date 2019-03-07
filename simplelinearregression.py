x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]

n = len(x)
xbar = sum(x)/n
ybar = sum(y)/n
SS_xy = 0
SS_xx = 0

#SS_xy
for i in range(n):
    Sxy = (x[i] - xbar)*(y[i] - ybar)
    SS_xy = SS_xy + Sxy
 

#SS_xx
for i in range(n):
    Sxx = (x[i] - xbar)**2
    SS_xx = SS_xx + Sxx

B_1 = SS_xy / SS_xx
B_0 = ybar - B_1 * xbar

print("b_0 = ", B_0)
print("b_1 = ", B_1)
