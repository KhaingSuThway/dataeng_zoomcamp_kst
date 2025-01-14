import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

random_state = 42
random_number = np.random.RandomState(random_state)
array_list = random_number.randint(0, 100, 1000)

df = pd.DataFrame(array_list, columns=['value'])

plt.hist(df['value'], bins=100)
plt.show()

print(sys.argv)
print("File name is: ", sys.argv[0])
day = sys.argv[1]


print('Job finished successfully for day {}'.format(day))