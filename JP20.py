#  write a python prgm to Histogram & Pie chart using matplotlib

import matplotlib.pyplot as plt
sub=['python','cma','ic','gen_eng']
m=[78,75,65,80]
ex=[0.2,0,0,0]
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.title('subject marks of kumar')
plt.pie(m,labels=sub,explode=ex,shadow=True)
avg=[78,45,65,80,33,34,55,88,50,60]
bins=[0,35,70,100]
plt.subplot(1,2,2)
plt.hist(avg,bins,edgecolor='black')
plt.xticks([0,35,70,100])
plt.title('student grade')
plt.xlabel('marks')
plt.ylabel('number of students')
plt.show()