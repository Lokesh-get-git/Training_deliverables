import pandas as pd
import matplotlib.pyplot as plt

# df=pd.read_csv("synthetic_data/linear_regression_data.csv")
# # print(df.head())

# print(df.describe())

# plt.scatter(df.price,df.distance_city)
# plt.show()
class linear_model:

    def __init__(self):     
        self.m=0
        self.b=0


    def loss_function(self,m,b,x,y):
        n=len(x)
        total=0
        for i in range(n):
            total+=(y[i]-(m*x[i]+b))**2
        loss=total/float(n)
        return loss

    def gradient_descent(self,m_now,b_now,x,y,L):
        m_gradient=0
        b_gradient=0
        n=len(x)
        for i in range(n):
            m_gradient+=(-2/n)*x[i]*(y[i]-(m_now*x[i]+b_now))
            b_gradient+=(-2/n)*(y[i]-(m_now*x[i]+b_now))
        m=m_now-L*m_gradient
        b=b_now-L*b_gradient
        return m,b

    def build_model(self,x,y,epochs=300,L=0.0001):
        self.m=0
        self.b=0
        for i in range(epochs+1):
            self.m,self.b=self.gradient_descent(self.m,self.b,x,y,L)
            if i%50==0:
                print(f"\nEpoch={i}\
                    \nm={self.m}\
                    \nb={self.b}\
                    \nLoss={self.loss_function(self.m,self.b,x,y)}")
        return self.m,self.b
                    
    def predict(self,x):
        y=self.m*x+self.b
        return y
