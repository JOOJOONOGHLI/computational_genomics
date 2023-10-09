import matplotlib.pyplot as plt
import pandas as pd

# Load the TSV file into a pandas DataFrame
data = pd.read_csv('hg38_lincRNA_clean.tsv', delimiter='\t')



# Plot the data using matplotlib
plt.plot(x, y)
plt.xlabel('chromosome')
plt.ylabel('y')
plt.title('Data Plot')
plt.show()