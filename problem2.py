import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

# import or paste dataset here
myFile = open('vehicle_survey_1.txt')
data1 = myFile.readlines()
data1 = [float(x) for x in data1]
myFile.close() # No longer need to have file open

print("\n\n")

# code for question 2
samp_size = len(data1) #Sample size value is the amt of data surveyed which would be the length of list
avg = np.mean(data1) #average of sample
sd = np.std(data1, ddof=1) #standard deviation
se = sd / np.sqrt(samp_size)
z_val = (avg-8) / se
p_val = 2*stats.norm.cdf(-abs(z_val))
print('Problem 2 Answers:')
print("Sample Size:",samp_size)
print("SD:", sd)
print("Sample Mean:", avg)
print("Standard Erro:", se)
print("Z test Val:", z_val)
print("P Val:", p_val)
# code below this line

print("\n\n")

# code for question 3
zval2 = norm.ppf((0.05/2))
zval2 = zval2 * -1
se_max = (avg - 8) / zval2 
size = (sd/se_max)**2
print('Problem 3 Answers:')
print("SE MAX:",se_max)
print("Samp size:", size)
# code below this line



print("\n\n")
# code for question 5
print('Problem 5 Answers:')
myFile2a = open('vehicle_survey_2.txt')
data2a = myFile2a.readlines()
myFile3 = open('vehicle_survey_3.txt')
data3 = myFile3.readlines()
data2a = [float(x) for x in data2a]
data3 = [float(y) for y in data3]
myFile2a.close() # No longer need to have file open
myFile3.close() # No longer need to have file open
# code below this line
samp_size_file2 = len(data2a)
print("Samp size of file 2:", samp_size_file2)
samp_size_file3 = len(data3)
print("Samp size of file 3:", samp_size_file3)

avg2 = np.mean(data2a) #average of sample
print("Samp Mean of File 2:",avg2)

avg3 = np.mean(data3) #average of sample
print("Samp Mean of File 3:",avg3)

sd2a = np.std(data2a, ddof=1) #standard deviation
sd3 = np.std(data3, ddof=1) #standard deviation
sd2a_squared = sd2a**2
sd3_squared = sd3**2
se2a = sd2a_squared/samp_size_file2 #standard error of file 2
se3 = sd3_squared/samp_size_file3 #standard error of file 3
sd_combo = (se2a + se3)**(0.5) #Standard deviation of both files
print("SD Val: ",sd_combo)
se_combo = (sd_combo) / (samp_size_file2+samp_size_file3)**(0.5) #standard error of both files
print("Overall SE:", se_combo)
avg_combo = avg2-avg3 #Calculate xbar
print("AVG combo val:", avg_combo)
z_combo = (avg_combo - 0) / sd_combo 
print("Z combo val:", z_combo)
p_combo = norm.cdf(z_combo)*2 #Probability Val
print("Prob:",p_combo)












