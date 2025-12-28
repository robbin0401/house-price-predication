import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_california_housing
st.title('🏠house price predication using ML')
st.image('https://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-11/256/house.png')
data=fetch_california_housing()
X=pd.DataFrame(data['data']),
          column=da