# Series examples
#neg 1
'''import pandas as pd
s=pd.Series()
print(s)'''

#neg 2
'''import pandas as pd
import numpy as np

data=np.array(['a','b','c'])
print(data)
s=pd.Series(data)
print(s)'''

# neg 3
'''import pandas as pd
import numpy as np

data={'a':0,'b':1,'c':2}
s=pd.Series(data,index=['b','c','d'])
print(s)
'''

# data frame
#neg 4
'''import pandas as pd
import numpy as np

s=pd.DataFrame()
print(s)'''

#neg 5
'''import pandas as pd
import numpy as np
data=[['abc',10],['def',20],['xyz',30]]
s=pd.DataFrame(data,index=['en1','en2','en3'],columns=['name','age'],dtype=int,copy=True)
print(s)'''

#neg 6
'''import pandas as pd
import numpy as np
data=pd.DataFrame([['abc',10],['def',20],['xyz',30]],columns=['a','b'])
data1=pd.DataFrame([['lmn',40],['qrs',50]],columns=['a','b'])
data =data.append(data1)
print(data)
data=data.drop(0)
print(data)
print(data.iloc[0])'''

