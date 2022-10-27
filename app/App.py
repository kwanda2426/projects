#pip install streamlit-aggrid
#pip install plotly-express
#pip install pandas
#pip install streamlit
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

st.set_page_config(page_title = 'Kwanda')
st.title('Data Loader')
st.subheader('Data file')

original_list = ['csv', 'xlsx']

result = st.selectbox('Select which file to upload:', original_list)

uploaded_file = st.file_uploader('Choose a {} file'.format(result), type = result)

if uploaded_file:
    st.markdown('---')

    if result == 'csv':
        while True:
            try:
                df = pd.read_csv(uploaded_file).astype(str)
                break
            except ValueError:
                print("Oop!  That was not a csv.  Check the file type and try again...")

    elif result == 'xlsx':
        while True:
            try:
                df = pd.read_excel(uploaded_file, engine = 'openpyxl').astype(str)
                break
            except ValueError:
                print("Oop!  That was not a csv.  Check the file type and try again...")
    
load = st.button('load data')

# initialize session state
if "load_state" not in st.session_state:
    st.session_state.load_state = False



if load or st.session_state.load_state:
    st.session_state.load_state = True

    grid_response = AgGrid(
    df,
    gridOptions = gridOptions,
    data_return_mode ='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    reload_data=True
)

data = grid_response['df']
selected = grid_response['selected_rows'] 
df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df

# user options
opt = st.radio('Plot type :',['Bar graph', 'Pie chart'] )
st.write('<style>div.row-widget.widget.stradio > div {flex-direction:row;}</style>', unsafe_allow_html=True)


if opt == 'Bar graph':
    fig= px.bar(df, x=st.radio('X column:',df.columns), y = st.radio('Y column:',df.columns), title = 'Bar chart')
        
    st.write('<style>div.row-widget.widget.stradio > div {flex-direction:row;}</style>', unsafe_allow_html=True)
    st.plotly_chart(fig)
else:
    fig=px.pie(df, names=st.radio('Name:', df.columns), values =st.radio('Values: ',df.columns), title='Pie chart' )
    fig.update_traces(
            textposition = "inside",
            textinfo = "percent +label +text")
    fig.update_layout(
    title_font_size = 22,
    plot_bgcolor = "rgb(243,243,243)",
    paper_bgcolor= "rgb(243,243,243)")
    st.plotly_chart(fig)
