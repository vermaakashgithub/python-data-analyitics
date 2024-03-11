### running the dashboard ####
## open the terminal
## cd immigration_analysis
## streamlit run dashboard.py

## libraries import
import streamlit as st
import pandas as pd
import os
import numpy as np
import plotly.express as px

# data loading  ## help to load data perform fast
@st.cache_data
def load_data():
    # load the data
    df = pd.read_excel('Canada.xlsx', 
                   sheet_name=1,
                   skiprows=20, 
                   skipfooter=2)
    # rename the columns
    df = df.rename(columns={
        'OdName': 'country',
        'AreaName': 'continent',
        'RegName': 'region',
        'DevName': 'status',
    })
    # rename the values accordingly
    df = df.replace('United Kingdom of Great Britain and Northern Ireland','UK',)
    # drop unnecessary columns
    cols_to_drop = ['Type', 'Coverage', 'AREA', 'REG', 'DEV']
    df = df.drop(columns=cols_to_drop)
    # create a new column to display the total
    years = list(range(1980, 2014))
    df['total'] = df[years].sum(axis=1)
    # set country as index (optional & for this case only )
    df=df.set_index('country')
    return df # return the dataframe
#ui setup
st.set_page_config(
    page_icon='🌍',
    page_title='Immigration Analyisi Dashboard',
    layout='wide',
    initial_sidebar_state='collapsed'
 )


# calling ui functions
years = list(range(1980, 2014))

df= load_data()

st.title('Immigration Analysis Dashboard')
st.subheader('United Nation data on  international migration')
c1,c2,c3,c4= st.columns(4)
chosen_years= st.sidebar.multiselect('Select years', years,years,
    help='Select the years to find immigration data')
chosen_countries= c2.multiselect('Select countries',df.index.tolist(),default=['India','China'],
    help='Select one or more contrie(s)')
sort_order=c3.selectbox('Sort order',['Assending','Desending'])

## visualization
if chosen_years and chosen_countries:
    filtered_df= df.loc[chosen_countries,chosen_years]
    if sort_order == 'Assending':
        filtered_df = filtered_df.sort_values(by=chosen_years,ascending=True)
    else:
        filtered_df= filtered_df.sort_values(by=chosen_years,ascending=False)
    st.dataframe(filtered_df)
    fig= px.line(filtered_df.T, x=filtered_df.columns,
         y=filtered_df.index)
    st.plotly_chart(fig,use_container_width=True)
