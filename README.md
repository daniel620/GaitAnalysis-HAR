# JHU-Gait-Watch-HAR

 Human Activity Recognition (HAR) using data from smart watches (Apple Watch, etc.).

# Data

## Visualization

![1664870848645](image/README/1664870848645.png)

![1664870858644](image/README/1664870858644.png)

![1664870864113](image/README/1664870864113.png)![1664870868084](image/README/1664870868084.png)![1664870871620](image/README/1664870871620.png)

## Directory Tree

```
.
├── LICENSE
├── PAMAP2
│   ├── data
│   │   ├── CleanedData.csv
│   │   ├── ScaledData.csv
│   │   ├── info.txt
│   │   ├── npy
│   │   │   ├── x
│   │   │   │   ├── x_0.npy
│   │   │   │   ├── x_1.npy
│   │   │   │   ├── x_10.npy
│   │   │   │   ├── x_11.npy
│   │   │   │   ├── x_12.npy
│   │   │   │   ├── x_13.npy
│   │   │   │   ├── x_14.npy
│   │   │   │   ├── x_15.npy
│   │   │   │   ├── x_16.npy
│   │   │   │   ├── x_17.npy
│   │   │   │   ├── x_18.npy
│   │   │   │   ├── x_19.npy
│   │   │   │   ├── x_2.npy
│   │   │   │   ├── x_20.npy
│   │   │   │   ├── x_21.npy
│   │   │   │   ├── x_22.npy
│   │   │   │   ├── x_23.npy
│   │   │   │   ├── x_24.npy
│   │   │   │   ├── x_25.npy
│   │   │   │   ├── x_26.npy
│   │   │   │   ├── x_27.npy
│   │   │   │   ├── x_28.npy
│   │   │   │   ├── x_29.npy
│   │   │   │   ├── x_3.npy
│   │   │   │   ├── x_30.npy
│   │   │   │   ├── x_31.npy
│   │   │   │   ├── x_32.npy
│   │   │   │   ├── x_33.npy
│   │   │   │   ├── x_34.npy
│   │   │   │   ├── x_35.npy
│   │   │   │   ├── x_36.npy
│   │   │   │   ├── x_37.npy
│   │   │   │   ├── x_38.npy
│   │   │   │   ├── x_39.npy
│   │   │   │   ├── x_4.npy
│   │   │   │   ├── x_40.npy
│   │   │   │   ├── x_41.npy
│   │   │   │   ├── x_42.npy
│   │   │   │   ├── x_43.npy
│   │   │   │   ├── x_44.npy
│   │   │   │   ├── x_45.npy
│   │   │   │   ├── x_5.npy
│   │   │   │   ├── x_6.npy
│   │   │   │   ├── x_7.npy
│   │   │   │   ├── x_8.npy
│   │   │   │   └── x_9.npy
│   │   │   └── y
│   │   │       ├── y_0.npy
│   │   │       ├── y_1.npy
│   │   │       ├── y_10.npy
│   │   │       ├── y_11.npy
│   │   │       ├── y_12.npy
│   │   │       ├── y_13.npy
│   │   │       ├── y_14.npy
│   │   │       ├── y_15.npy
│   │   │       ├── y_16.npy
│   │   │       ├── y_17.npy
│   │   │       ├── y_18.npy
│   │   │       ├── y_19.npy
│   │   │       ├── y_2.npy
│   │   │       ├── y_20.npy
│   │   │       ├── y_21.npy
│   │   │       ├── y_22.npy
│   │   │       ├── y_23.npy
│   │   │       ├── y_24.npy
│   │   │       ├── y_25.npy
│   │   │       ├── y_26.npy
│   │   │       ├── y_27.npy
│   │   │       ├── y_28.npy
│   │   │       ├── y_29.npy
│   │   │       ├── y_3.npy
│   │   │       ├── y_30.npy
│   │   │       ├── y_31.npy
│   │   │       ├── y_32.npy
│   │   │       ├── y_33.npy
│   │   │       ├── y_34.npy
│   │   │       ├── y_35.npy
│   │   │       ├── y_36.npy
│   │   │       ├── y_37.npy
│   │   │       ├── y_38.npy
│   │   │       ├── y_39.npy
│   │   │       ├── y_4.npy
│   │   │       ├── y_40.npy
│   │   │       ├── y_41.npy
│   │   │       ├── y_42.npy
│   │   │       ├── y_43.npy
│   │   │       ├── y_44.npy
│   │   │       ├── y_45.npy
│   │   │       ├── y_5.npy
│   │   │       ├── y_6.npy
│   │   │       ├── y_7.npy
│   │   │       ├── y_8.npy
│   │   │       └── y_9.npy
│   │   └── temp.ipynb
│   ├── images
│   │   ├── lying.jpg
│   │   ├── running.jpg
│   │   ├── sitting.jpg
│   │   ├── standing.jpg
│   │   └── walking.jpg
│   ├── make_dataset.py
│   ├── preprocess.ipynb
│   └── src
├── README.md
├── image
│   └── README
│       ├── 1664870733605.png
│       ├── 1664870848645.png
│       ├── 1664870858644.png
│       ├── 1664870864113.png
│       ├── 1664870868084.png
│       └── 1664870871620.png
└── images
    ├── lying.jpg
    ├── running.jpg
    ├── sitting.jpg
    ├── standing.jpg
    └── walking.jpg

10 directories, 116 files
```
