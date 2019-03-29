from scipy.stats import linregress
import matplotlib.pyplot as mt
import math
import numpy as np
#import statistics as st
data5_2500 = [10.7,23.32,38.46,57.71,82.82]
data10_2500 = [5.62,25.91,49.27,84.49,144.68]
data15_2500 = [2.92,16.7,33.12,53.43,79.79]
data5_3000 = [4.62,18.04,35.97,58.9,91.25]
data10_3000 = [8.23,28.72,55.4,94.44,169.0]
data15_3000 = [2.06,16.82,34.26,56.17,86.17]
data5_3500 = [2.79,17.21,33.98,55,83.55]
data10_3500 = [10.14,25.98,45.4,70.48,106.92]
data15_3500 = [1.22,18.49,39.5,67.6,109.85]
data5_4000 = [9.01,44.11,69.5,104.31,168.88]
data10_4000 = [3.24,17.55,34.72,55.55,84.88]
data15_4000 = [15.3,34.64,59.26,95.62,159.99]
data5_4500 = [3.21,18.65,36.73,89.96,139.65]
data10_4500 = [2.0,11.26,23.28,38.84,59.78]
data15_4500 = [8.11,27.54,53.02,90.11,160.48]
s5_2500,s10_2500,s15_2500,s5_3000,s10_3000,s15_3000,s5_3500,s10_3500,s15_3500,s5_4000,s10_4000,s15_4000,s5_4500,s10_4500,s15_4500 = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
t5_2500,t10_2500,t15_2500,t5_3000,t10_3000,t15_3000,t5_3500,t10_3500,t15_3500,t5_4000,t10_4000,t15_4000,t5_4500,t10_4500,t15_4500 = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
for i in range(4):
    s5_2500.append(data5_2500[i+1] - data5_2500[i])
    s10_2500.append(data10_2500[i+1] - data10_2500[i])
    s15_2500.append(data15_2500[i+1] - data15_2500[i])
    s5_3000.append(data5_3000[i+1] - data5_3000[i])
    s10_3000.append(data10_3000[i+1] - data10_3000[i])
    s15_3000.append(data15_3000[i+1] - data15_3000[i])
    s5_3500.append(data5_3500[i+1] - data5_3500[i])
    s10_3500.append(data10_3500[i+1] - data10_3500[i])
    s15_3500.append(data15_3500[i+1] - data15_3500[i])
    s5_4000.append(data5_4000[i+1] - data5_4000[i])
    s10_4000.append(data10_4000[i+1] - data10_4000[i])
    s15_4000.append(data15_4000[i+1] - data15_4000[i])
    s5_4500.append(data5_4500[i+1] - data5_4500[i])
    s10_4500.append(data10_4500[i+1] - data10_4500[i])
    s15_4500.append(data15_4500[i+1] - data15_4500[i])
    t5_2500.append((data5_2500[i+1] + data5_2500[i])/2)
    t10_2500.append((data10_2500[i+1] + data10_2500[i])/2)
    t15_2500.append((data15_2500[i+1] + data15_2500[i])/2)
    t5_3000.append((data5_3000[i+1] + data5_3000[i])/2)
    t10_3000.append((data10_3000[i+1] + data10_3000[i])/2)
    t15_3000.append((data15_3000[i+1] + data15_3000[i])/2)
    t5_3500.append((data5_3500[i+1] + data5_3500[i])/2)
    t10_3500.append((data10_3500[i+1] + data10_3500[i])/2)
    t15_3500.append((data15_3500[i+1] + data15_3500[i])/2)
    t5_4000.append((data5_4000[i+1] + data5_4000[i])/2)
    t10_4000.append((data10_4000[i+1] + data10_4000[i])/2)
    t15_4000.append((data15_4000[i+1] + data15_4000[i])/2)
    t5_4500.append((data5_4500[i+1] + data5_4500[i])/2)
    t10_4500.append((data10_4500[i+1] + data10_4500[i])/2)
    t15_4500.append((data15_4500[i+1] + data15_4500[i])/2)
dataTable = np.log(np.array(s5_2500))
sigmas = math.sqrt(2)/s5_2500[3]
ilk = np.log(s5_2500)
slope,intercept,rvalue,pvalue,stderr=linregress(t5_2500,np.log(s5_2500))
fit=np.polyfit(t5_2500,np.log(s5_2500),1)
bfl=np.poly1d(fit)
mt.scatter(t5_2500,np.log(s5_2500),color="black")
mt.plot(t5_2500,bfl(t5_2500),color="green")
mt.title("T vs ln(s) Line fit and scatter")
mt.xlabel("T")
mt.ylabel("ln(s)")
mt.grid()
mt.show()				
slopeArr, interceptArr, rvalueArr, stderrArr = [],[],[],[]
for x in range(5,10):
    for y in range(1,4):
        sstr = "np.array(s"+str((y)*5)+"_"+str((x)*500)+")"
        slope,intercept,rvalue,pvalue,stderr=linregress(eval("t"+str((y)*5)+"_"+str((x)*500)),np.log(eval(sstr)))
        slopeArr.append(slope)
        interceptArr.append(intercept)
        rvalueArr.append(rvalueArr)
        stderrArr.append(stderr)
def calculateTop(lambdax, sigma):
    omega = (1/((sigma)**2))
    return omega * lambdax
top = 0
bottom = 0
std = 0
for k in range(15):
    top += calculateTop(slopeArr[k],stderrArr[k])
    std += (1/(stderrArr[k]**2))
    bottom += (1/((stderrArr[k])**2))
lambdaAvg = top / bottom
sigmaLambdaAvg = (1/math.sqrt(std))
thalf = np.log(2) / lambdaAvg
sigmathalf = ((np.log(2)/(lambdaAvg**2))) * (sigmaLambdaAvg)
print("Lambda_Average: "+str(lambdaAvg))
print("Sigma Lambda_Average: "+str(sigmaLambdaAvg))
print("Half Life: "+str(thalf))
print("Sigma Half Life: "+str(sigmathalf))
print("Theoratical Half Life: "+str(55.7))
print("Total Error: "+str((thalf - 55.7)/sigmathalf)+" sigma away from the theoratical value")
