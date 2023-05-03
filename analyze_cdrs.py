import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load the call records data
df = pd.read_csv("cdrs.csv")

# Extract the relevant features for anomaly detection
numeric_features = ["Duration", "Buyer Amount", "Seller Amount", "System Amount"]
categorical_features = ["Country", "Description", "Buyer", "Seller", "Route" ]
time_feature = "Setup Time"

X_numeric = df[numeric_features]
X_categorical = df[categorical_features]
X_time = pd.to_numeric(pd.to_datetime(df[time_feature]))

# Preprocess the numerical data
scaler = StandardScaler()
X_numeric = scaler.fit_transform(X_numeric)

# Preprocess the categorical data
encoder = OneHotEncoder()
X_categorical = encoder.fit_transform(X_categorical)

# Combine the preprocessed data
X = np.concatenate([X_numeric, X_categorical.toarray(), np.array(X_time).reshape(-1, 1)], axis=1)

# Train a KMeans clustering model
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)

# Predict the clusters for each data point
y_pred = kmeans.predict(X)

# Identify anomalies as data points that are in a small cluster
cluster_sizes = np.bincount(y_pred)
anomaly_threshold = np.percentile(cluster_sizes, 5)
anomaly_indices = np.where(cluster_sizes < anomaly_threshold)[0]

# Print the anomalies
anomalies = df.iloc[np.isin(y_pred, anomaly_indices)]
print(anomalies)
