1. Sampling Bias (Conditional Collection)
Approved loans only were kept (credit ≥620, income ≥45k from 10k applicants).

Dataset	    Rows	Default Rate	Avg Income	Avg Credit
Population	10k	        12%	            ~60k	    ~651
Approved	5.6k	    0%	            ~64k	    ~688

Problem: High-risk cases vanish; models underestimate defaults.

2. Class Imbalance (Misleading Metrics)
5% minority class in 10k samples. Predict majority always.

Accuracy: 95%

Minority recall: 0%

Confusion: 
[[9500 0]
[500 0]]
​

Problem: Accuracy hides total failure on rare events.

3. Data Leakage (Target in Features)
Feature directly encodes target; model gets 100% accuracy.

Confusion: 
[[1019 0]
[0 481]]
​

Problem: Perfect metrics, but uses unavailable future info. Most dangerous.