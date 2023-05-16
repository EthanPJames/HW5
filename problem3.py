import math as m
import numpy as np
import scipy.stats as stats

# import or paste dataset here
data = np.array([196.8 , 196.7 ,189.4 ,196.6 ,173.5 ,195.2 ,217.9 ,195.2 ,194.3 ,211.2 ,201.0 ,197.1 ,209.1 ,207.3 ,206.4 ,195.2 ,190.1 ,203.2 ,194.1 ,201.8])


# code for question 1

print('Problem 1 Answers:')
# code below this line
samp_size1 = len(data)
print("Samp_Size:", samp_size1)
avg1 = np.mean(data) #AVG of data
print("AVG of samp:",avg1)
i = 0
part_two = 0
while(i <= (samp_size1 - 1)):
    part_two = (data[i] - avg1)**2 + part_two
    i = i + 1
    

se1 = ((1/(samp_size1-1)) * part_two)**(0.5) / (samp_size1)**(0.5)
print("SE VALUE:", se1)

t_val = stats.t.ppf(1-(1-0.9)/2, 19)
print("T_VAL:", t_val)

con_int1 = avg1 - (t_val*se1)
print("Confidence INTV LOW bound:", con_int1)
con_int2 = avg1 + (t_val*se1)
print("Confidence INTV UP bound:", con_int2)

print("\n\n")
# code for question 2
print('Problem 2 Answers:')
# code below this line
t_val2 = stats.t.ppf(1-(1-0.95)/2, 19)
print("T_VAL2:", t_val2)
con_int3 = avg1 - (t_val2*se1)
print("Confidence INTV LOW bound:", con_int3)
con_int4 = avg1 + (t_val2*se1)
print("Confidence INTV UP bound:", con_int4)
print("Width1:", con_int2-con_int1)
print("Width2", con_int4-con_int3)


print("\n\n")
# code for question 3
print('Problem 3 Answers:')
# code below this line
#sd1 = np.std(data, ddof=1)
#print("Standard Deviation:", sd1)

se2 = 10 / (samp_size1)**(0.5)
print("SE VAL:", se2)

z_val = stats.norm.ppf(1-(1-0.95)/2)
print("ZTEST VAL:", z_val)


con_int5 = avg1 - (z_val*se2)
print("Confidence INTV LOW bound:", con_int5)
con_int6 = avg1 + (z_val*se2)
print("Confidence INTV Upper bound:", con_int6)
print("Width3", con_int6-con_int5)

# code for question 4
print('Problem 4 Answers:')
# code below this line


