import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#loading the 2 csv files for set 1
data_scanA = pd.read_csv("scan_posA.csv")
data_scanB = pd.read_csv("scan_posB.csv")

xA,yA = data_scanA['x'].values, data_scanA['y'].values # x and y coordinates of scan A
xB,yB = data_scanB['x'].values , data_scanB['y'].values ## x and y coordinates of scan B

#plotting both scas in a single figure (task A)
plt.figure(figsize = (6,6))
plt.scatter(xA, yA, c='blue', label='Scan A')
plt.scatter(xB, yB, c='red', label='Scan B')
plt.grid(True)
plt.title('Task (a):Data points from both scans')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.tight_layout()
plt.savefig('task_a.png')
plt.axis('equal')
plt.show()