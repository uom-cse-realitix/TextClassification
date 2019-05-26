# Results in SVMs

The SVM was tested upon three separate algorithms.

1. Linear
2. Polynomial
3. RBF
4. Sigmoid

## Linear Kernel

|              | Precision | Recall | F1-Score | Support |
|--------------|------------|--------|----------|---------|
| 0.0          | 1.0        | 1.0    | 1.0      | 12      |
| 1.0          | 1.0        | 1.0    | 1.0      | 11      |
| 2.0          | 1.0        | 1.0    | 1.0      | 18      |
| Accuracy     |            |        | 1.0      | 41      |
| Macro Avg    | 1.0        | 1.0    | 1.0      | 41      |
| Weighted Avg | 1.0        | 1.0    | 1.0      | 41      |

## Polynomial Kernel

|              | Preceision | Recall | F1-Score | Support |
|--------------|------------|--------|----------|---------|
| 0.0          | 1.0        | 1.0    | 1.0      | 12      |
| 1.0          | 1.0        | 0.55   | 0.71     | 11      |
| 2.0          | 0.78       | 1.0    | 0.88     | 18      |
| Accuracy     |            |        | 0.88     | 41      |
| Macro Avg    | 0.93       | 0.85   | 0.86     | 41      |
| Weighted Avg | 0.90       | 0.88   | 0.87     | 41      |

## RBF Kernel

|              | Precision | Recall | F1-Score | Support |
|--------------|------------|--------|----------|---------|
| 0.0          | 1.0        | 1.0    | 1.0      | 12      |
| 1.0          | 1.0        | 1.0    | 1.0      | 11      |
| 2.0          | 1.0        | 1.0    | 1.0      | 18      |
| Accuracy     |            |        | 1.0      | 41      |
| Macro Avg    | 1.0        | 1.0    | 1.0      | 41      |
| Weighted Avg | 1.0        | 1.0    | 1.0      | 41      |

## Sigmoid Kernel

|              | Preceision | Recall | F1-Score | Support |
|--------------|------------|--------|----------|---------|
| 0.0          | 1.0        | 1.0    | 1.0      | 12      |
| 1.0          | 1.0        | 0.45   | 0.62     | 11      |
| 2.0          | 0.78       | 0.78   | 0.88     | 18      |
| 3.0          | 0.0        | 0.0    | 0.0      | 0       |
| Accuracy     |            |        | 0.76     | 41      |
| Macro Avg    | 0.75       | 0.56   | 0.62     | 41      |
| Weighted Avg | 1.00       | 0.76   | 0.84     | 41      |
