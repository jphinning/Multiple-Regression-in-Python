import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

data = loadmat('./src/data/IN_OUT_PA.mat')

input_array = np.concatenate(np.array(data['in']))
output_array = np.concatenate(np.array(data['out']))

#Parameters
p_range = int(input("Enter your value for p: ")) + 1
m_range = int(input("Enter your value for m: ")) + 1

regression_matrix_list = []

#Duvida: O que fazer quando n-m eh um valor menor que 0? Colocamos no array valores soh de input(n)? Ou pulamos?
for data in range(len(input_array)):
  equation_instance_array = []
  for p in range(1,p_range):
    for m in range(m_range):
      if((data - m) < 0):
        equation_instance_array.append(input_array[data] ** p)
      else:
        equation_instance_array.append(input_array[data - m] ** p)

  regression_matrix_list.append(equation_instance_array)


regression_matrix = np.array(regression_matrix_list)


coeficient_array, residuals, rank, s = np.linalg.lstsq(
    regression_matrix, output_array, rcond=None)


#Output Calc
predicted_output_array = []

for i in range(len(regression_matrix)):
  sum = 0
  for j in range(len(coeficient_array)):
    sum += coeficient_array[j] * regression_matrix[i][j]

  predicted_output_array.append(sum)

# Ploting charts
fig, ax = plt.subplots()

plt.plot(input_array, output_array, 'o', label='Original data', markersize=3)
plt.plot(input_array, predicted_output_array, 'o', label='Predicted data', markersize=3)
ax.set(xlabel='input', ylabel='output', title='Amplifier data')
plt.legend()
ax.grid()

fig.savefig("multiple_regression.png")
