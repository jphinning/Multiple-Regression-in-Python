import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

data = loadmat('./src/data/IN_OUT_PA.mat')

input_array = np.concatenate(np.array(data['in']))
output_array = np.concatenate(np.array(data['out']))

# Ploting charts
fig, ax = plt.subplots()

plt.plot(input_array, output_array, 'o', label='Amplifier data', markersize=3)
plt.legend()
ax.grid()
ax.set(xlabel='input', ylabel='output', title='Amplifier data')
fig.savefig("amplifier_data.png")
