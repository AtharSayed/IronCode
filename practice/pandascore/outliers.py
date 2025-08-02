# Detecting outliers from the dataset using Z-Score

import numpy as np

def detect_outliers(data):
    outliers = []
    threshold = 3
    mean = np.mean(data)
    std = np.std(data, ddof=1)  # use sample std dev

    for i in data:
        z_score = (i - mean) / std
        if abs(z_score) > threshold:
            outliers.append(i)
    return outliers

def main():
    dataset = [11, 10, 12, 14, 12, 15, 14, 13, 15, 102, 12, 14, 17, 19, 107, 10, 13, 12, 14, 12, 108, 12, 11]
    res = detect_outliers(dataset)
    print("Outliers:", res)

if __name__ == "__main__":
    main()
