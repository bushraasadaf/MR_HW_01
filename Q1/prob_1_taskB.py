import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#load scans
data_scanA = pd.read_csv("scan_posA.csv")
data_scanB = pd.read_csv("scan_posB.csv")

xA, yA = data_scanA['x'].values, data_scanA['y'].values
xB, yB = data_scanB['x'].values, data_scanB['y'].values

#task b:
pts_B_homo = np.vstack((xB, yB, np.ones_like(xB)))

T_A_B = np.array([
    [-1.0,  0.0, 0.0],
    [ 0.0, -1.0, 1.4],
    [ 0.0,  0.0, 1.0]
])

pts_B_in_A = T_A_B @ pts_B_homo

#fused figure
plt.figure(figsize=(6, 6))
plt.scatter(xA, yA, c='blue', label='Scan A')
plt.scatter(pts_B_in_A[0, :], pts_B_in_A[1, :], c='green', label='Scan B (Transformed)')
plt.axis('equal')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Task (b): Fused LiDAR Scans in Frame A')
plt.legend()
plt.tight_layout()
plt.savefig('task_b_fused.png')
plt.show()