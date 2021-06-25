#bars
'''import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
lang=['c','c++','java','python']
stud=[10,20,40,25]
ax.bar(lang,stud)
ax.set_xlabel('courses')
ax.set_ylabel('no of student')
ax.legend(labels=['stud','lang'])
plt.show()'''

#plotting without line
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,8])
y = np.array([3,10])
plt.plot(x,y, 'o')
plt.show()'''

#marker * + green line
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,2,10,30])
y = np.array([0,4,20,25])
plt.plot(x, y,'*--g')
plt.show()'''

#multiple points
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,2,10,30])
y = np.array([0,4,20,25])
plt.plot(x, y)
plt.show()'''

#marker *
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,2,10,30])
y = np.array([0,4,20,25])
plt.plot(x, y,marker='*')
plt.show()'''

#format strings
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,2,10,30])
y = np.array([0,4,20,25])
plt.plot(x, y,'*:g')
plt.show()'''

#marker size + marker
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,2,10,30])
y = np.array([0,4,20,25])
plt.plot(x, y,marker='o',ms=20)
plt.show()'''

#marker color
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,2,10,30])
y = np.array([0,4,20,25])
plt.plot(x, y,marker='o',ms=20,mec='r',mfc='b')
plt.show()
'''

#multiple lines
'''import matplotlib.pyplot as plt
import numpy as np
x1=np.array([0,1,2,3])
y1=np.array([3,8,1,10])
x2=np.array([0,1,2,3])
y2=np.array([6,2,7,11])
plt.plot(x1,y1,x2,y2)
plt.show()'''

#line width
'''import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y, linewidth='20.5')
plt.show()'''

#set font properties fr title & labels
'''import numpy as np
import matplotlib.pyplot as plt
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':15}
plt.title("Sports Watch Data",fontdict=font1)
plt.xlabel("Average Plus",fontdict=font2)
plt.ylabel("Calorie Burnage",fontdict=font2)
plt.plot(x,y)
plt.show()'''

#add grid lines to plot & set line properties for the grid
'''import numpy as np
import matplotlib.pyplot as plt
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.title("Sports Watch Data")
plt.xlabel("Average Plus")
plt.ylabel("Calorie Burnage")
plt.plot(x,y)
plt.grid(color='blue',ls='--',linewidth=0.5)
plt.show()'''

'''#display multi plots with subplots() functn
import matplotlib.pyplot as plt
import numpy as np
#plot 1:
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("SALES")
#plot 2:
x = np.array([0,1,2,3])
y= np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("INCOME")
plt.suptitle("MY SHOP")  #use for super title
plt.show()'''

#scatter plots(big dots) & color map
'''import matplotlib.pyplot as plt
import  numpy as np
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes= 10 * np.random.randint(100, size=(100))
plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap='nipy_spectral') #scatter plot,cmap=color map,alpha for transparency
plt.colorbar()
plt.show()'''

#a normal data distribution by numpy generates arrays
'''import numpy as np
x=np.random.normal(170,10,250)
print(x)'''

#Histograms
import matplotlib.pyplot as plt
import numpy as np
'''x=np.random.normal(170,10,250)
plt.hist(x)
plt.show()'''

#explode pie chart
'''import matplotlib.pyplot as plt
import numpy as np
y = np.array([35,25,25,15])
mylabels = ["Apples","Bananas","Cherries","Dates"]
myexplode = [0.2,0,0,0]
plt.pie(y, labels = mylabels, explode=myexplode)
plt.show()'''

#add legend with header in pie chart
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35,25,25,15])
mylabels = ["Apples","Bananas","Cherries","Dates"]
plt.pie(y, labels = mylabels)
plt.legend(title="Four Fruits:")
plt.show()