import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

def generate_scatter_plot():
    # Generate random data
    x = np.random.randn(100)
    y = np.random.randn(100)

    # Create scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y)
    plt.title('Random Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    st.pyplot()

# Main function to run the app
def main():
    generate_scatter_plot()
