# write a python prgm to Drawing Line chart & bar chart using matplotlib

import matplotlib.pyplot as plt
ri=[40,85,123,197]
overs=['5','10','15','20']
plt.subplot(1,2,1)
plt.plot(overs,ri,marker='o',color='red',label='india')
rs=[45,80,133,190]
plt.plot(overs,rs,marker='d',color='blue',label='srilanka')
plt.title('india vs srilanka')
plt.xlabel('overs')
plt.ylabel('runs')
plt.legend()
plt.subplot(1,2,2)
plt.bar(overs,ri,color='red',label='india')
plt.title('runs progress of india ')
plt.xlabel('overs')
plt.ylabel('runs')
plt.legend()
plt.show()