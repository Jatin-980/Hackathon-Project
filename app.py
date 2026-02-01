import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

def main():
    print("Welcome to your AI/ML Hackathon Project!")
    print("Environment check:")
    print(f"- NumPy: {np.__version__}")
    print(f"- Pandas: {pd.__version__}")
    print(f"- Seaborn: {sns.__version__}")
    
    # Example: Create a dummy dataset
    df = pd.DataFrame({
        'offset': np.random.randn(100),
        'value': np.random.randn(100) + 5
    })
    
    print("\nSample Data:")
    print(df.head())
    
    # Check simple plot (won't show in terminal but verifies verify import)
    # plt.figure()
    # sns.scatterplot(data=df, x='offset', y='value')
    # print("\nPlotting libraries imported successfully.")

if __name__ == "__main__":
    main()
