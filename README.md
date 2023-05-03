## AI CDRs Analysis :bar_chart:

📈 This code repository is designed to identify unusual patterns in call data. It can help identify unexpected spikes in call volume or unusually long call durations, which could be indicators of fraudulent or suspicious activity.

🤖 The code works by loading call records data file and preprocessing it for anomaly detection using KMeans clustering. The data is split into numerical, categorical, and time features. The numerical features are standardized, the categorical features are one-hot encoded, and the time feature is converted to numeric values. The preprocessed data is then concatenated and used to train a KMeans clustering model. The clusters are used to identify anomalies as data points in small clusters, and the anomalies are printed out.

🔍 This repository is helpful for individuals or organizations looking to improve the security and reliability of their telecommunication services by detecting unusual patterns in call data.

**Sample Output** :clipboard:

The output represents a table of call records data that has been preprocessed and analyzed for anomalies using the KMeans clustering algorithm. The table contains information about each call, such as the buyer, seller, route, duration, amount, country, setup time, connect time, disconnect time, and disconnect reason. Each row in the table represents a single call record, and each column represents a feature of that call.

The values in the table are numeric representations of the original data, which have been standardized and one-hot encoded as necessary. The special thing about this output is that it identifies any unusual patterns in call data, such as unexpected spikes in call volume or unusually long call durations, which could be indicators of fraudulent or suspicious activity. The anomalies are identified as data points that are in small clusters and are printed out in the last line of the code.

```shell
         Buyer    Seller      Route           CLD            CLI           Country  ... Seller Amount  System Amount        Setup Time      Connect Time   Disconnect Time     Disconnect Reason
0      AcmeInc       MCI     MCI RT    2917537855    16597651075           ERITREA  ...      0.002755       0.000012  30/04/2023 23:59  30/04/2023 23:59  30/04/2023 23:59  Normal call clearing
1      AcmeInc       MCI     MCI RT    2917069725   808663602177           ERITREA  ...      0.002755       0.000012  30/04/2023 23:58  30/04/2023 23:58  30/04/2023 23:59  Normal call clearing
2      AcmeInc       MCI     MCI RT    2917273794   211955152607           ERITREA  ...      1.738405       0.007362  30/04/2023 23:58  30/04/2023 23:58   01/05/2023 0:08  Normal call clearing
3      AcmeInc       MCI     MCI RT    2917749045   143746234453           ERITREA  ...      0.002755       0.000012  30/04/2023 23:58  30/04/2023 23:58  30/04/2023 23:58  Normal call clearing
4      AcmeInc       MCI     MCI RT    2917213615    16716160268           ERITREA  ...      0.002755       0.000012  30/04/2023 23:58  30/04/2023 23:58  30/04/2023 23:58  Normal call clearing
...        ...       ...        ...           ...            ...               ...  ...           ...            ...               ...               ...               ...                   ...
57183  AcmeInc       MCI     MCI RT    2917301451    12905739610           ERITREA  ...      0.002755       0.000012  28/04/2023 13:33  28/04/2023 13:33  28/04/2023 13:33  Normal call clearing
57184  AcmeInc   Verizon  Voice_CLI   94760096299   966578152542         SRI LANKA  ...      0.067402       0.000432  28/04/2023 13:33  28/04/2023 13:33  28/04/2023 13:34  Normal call clearing
57185  AcmeInc  Vodafone    Premium  959890376077    19183138008           MYANMAR  ...      0.417028       0.006172  28/04/2023 13:33  28/04/2023 13:33  28/04/2023 13:42  Normal call clearing
57186  AcmeInc   Verizon  Voice_CLI   94771566152    97477763949         SRI LANKA  ...      7.286667       0.046667  28/04/2023 13:33  28/04/2023 13:33  28/04/2023 14:40  Normal call clearing
57187  AcmeInc       ATT   Platinum   67579115103  6281343444589  PAPUA NEW GUINEA  ...      0.899300       0.000700  28/04/2023 13:33  28/04/2023 13:33  28/04/2023 13:33  Normal call clearing


```
