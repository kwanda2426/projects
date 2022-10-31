#pip install streamlit-aggrid
#pip install plotly-express
#pip install pandas
#pip install streamlit
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

st.set_page_config(
     page_title="Data Loader",
     page_icon= 'Capture.PNG',
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

st.image('Final_logo.jpg')

original_list = ['csv', 'xlsx']

result = st.selectbox('Select which file to upload:', original_list)

uploaded_file = st.file_uploader('Choose a {} file'.format(result), type = result)

if uploaded_file:
    st.markdown('---')

    if result == 'csv':
          
          df = pd.read_csv(uploaded_file).astype(str)

    elif result == 'xlsx':
     
          df = pd.read_excel(uploaded_file, engine = 'openpyxl').astype(str)

    
load = st.button('load data')

# initialize session state
if "load_state" not in st.session_state:
    st.session_state.load_state = False



if load or st.session_state.load_state:
    st.session_state.load_state = True
        
    data = AgGrid(df)




# user options
opt = st.radio('Plot type :',['Bar graph', 'Pie chart'] )
st.write('<style>div.row-widget.widget.stradio > div {flex-direction:row;}</style>', unsafe_allow_html=True)

import pandas as pd
import streamlit as st

# Cache the dataframe so it's only loaded once
@st.experimental_memo
def load_data():
    return pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)