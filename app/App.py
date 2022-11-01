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
        
    
    #data = st.dataframe(df)

    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_pagination(enabled = True)
    gd.configure_side_bar() #Add a sidebar
    gd.configure_selection('multiple', use_checkbox=True)
    gd.configure_default_column(editable = True, groupable = True)
    gridoptions = gd.build()
    grid_response= AgGrid(data = df, 
                            gridOptions = gridoptions, 
                            data_return_mode='AS_INPUT',
                            fit_columns_on_grid_load = True,
                            height=350, 
                            width='100%',
                            )

    data = grid_response['data']
    selected = grid_response['selected_rows'] 
    dd = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df
    cols = dd.columns[1:]
    st.dataframe(dd[cols])




    # user options
#opt = st.radio('Plot type :',['Bar graph', 'Pie chart'] )
#st.write('<style>div.row-widget.widget.stradio > div {flex-direction:row;}</style>', unsafe_allow_html=True)

#transform = st.button('Transform data')










