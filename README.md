# AI CDRs Analysis

This code repository is designed to identify unusual patterns in call data. It can help identify unexpected spikes in call volume or unusually long call durations, which could be indicators of fraudulent or suspicious activity.

The code works by loading call records data file and preprocessing it for anomaly detection using KMeans clustering. The data is split into numerical, categorical, and time features. The numerical features are standardized, the categorical features are one-hot encoded, and the time feature is converted to numeric values. The preprocessed data is then concatenated and used to train a KMeans clustering model. The clusters are used to identify anomalies as data points in small clusters, and the anomalies are printed out.

This repository is helpful for individuals or organizations looking to improve the security and reliability of their telecommunication services by detecting unusual patterns in call data.
