# Model Comparison Summary

## Objective
Train and compare multiple classification models on the same dataset using a structured evaluation matrix to understand differences in model behavior.

## Dataset
- Breast Cancer Wisconsin (Diagnostic)
- Binary classification
- Stratified train/test split (80/20)

## Models Compared
- Logistic Regression   (linear model)
- K-Nearest Neighbors (KNN) (distance based model)
- Support Vector Machine (RBF) (margin based model)
- Random Forest (tree based model)
- Gaussian Naive Bayes (probablistic model)

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

## Performance Summary
- **Logistic Regression** and **SVM (RBF)** achieved the best overall performance, with the highest accuracy (0.9825), F1-score (0.9861), and ROC-AUC (~0.995).
- **KNN** and **Random Forest** showed slightly lower performance, indicating sensitivity to local noise and variance despite strong recall.
- **Naive Bayes** performed worst among the models but remained competitive given its strong independence assumptions.

## Key Takeaways
- The dataset is close to linearly separable, which explains the strong performance of Logistic Regression.
- More complex models did not significantly outperform simpler ones.
- Model choice mattered more than model complexity for this task.


Model	            Accuracy	Precision	Recall	F1	    ROC-AUC
					
Logistic Regression	0.9825	    0.9861	    0.9861	0.9861	0.9954
KNN	                0.9561	    0.9589	    0.9722	0.9655	0.9788
SVM (RBF)	        0.9825	    0.9861	    0.9861	0.9861	0.9950
Random Forest	    0.9561	    0.9589	    0.9722	0.9655	0.9937
Naive Bayes	        0.9386	    0.9452	    0.9583	0.9517	0.9878