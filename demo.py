import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

def prediction(value):
    x=np.array([5,15,25,35,45,55]).reshape(-1,1)
    y=np.array([4,20,14,32,22,38])
    model=LinearRegression()
    model.fit(x,y)
    pr=np.array([value]).reshape(-1,1)
    #extra
    pr=pr.astype(float)
    pred=model.predict(pr)
    #extra
    pred='{:.2f}'.format(pred[0])
    return pred




def main():
    st.title("AN AI APP")

    Value=st.text_input("Value","please enter num value")
    if st.button("Predict"):
        ot=prediction(Value)
        st.success("The predicted value is:{}".format(ot))



if __name__=='__main__':
    main()


