import pandas as pd
import streamlit as st
import plotly.express as px

# Title
st.title('Customer Segmentation Results')

# Load data
df = pd.read_csv('clustered_data.csv')

# Display the clustered dataset
st.subheader('Clustered Data')
st.dataframe(df)

# Display the cluster mean values
st.subheader('Cluster Means')
cluster_means = df.groupby('Cluster').mean(numeric_only=True)
st.dataframe(cluster_means)

# Show Elbow Method image
st.subheader('Elbow Method')
st.image('elbow_method.png', caption='Elbow Method to Determine Optimal Clusters', use_container_width=True)

# Show Dendrogram image
st.subheader('Dendrogram')
st.image('dendrogram.png', caption='Hierarchical Clustering Dendrogram', use_container_width=True)

# Visualize customer segments
st.subheader('Customer Segments Visualization')
fig = px.scatter(
    df,
    x='Age',
    y='Spending Score (1-100)',
    color='Cluster',
    title='Customer Segments based on Age and Spending Score',
    hover_data=['Annual Income (k$)']
)
st.plotly_chart(fig)
