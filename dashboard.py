import streamlit as st
import pandas as pd
import os
import warnings
import plotly.express as px
import plotly.figure_factory as ff

warnings.filterwarnings('ignore')

css = '''
    <style>
        div.block-container{
            padding-top: 1rem;
        }
    </style>
'''

st.set_page_config(page_title='SuperStore!!!', page_icon=":bar_chart:", layout="wide")

st.title(" :bar_chart: Sample superstore EDA")

st.write(css, unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file", type=(['csv', 'txt', 'xlsx', 'xls']))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding="ISO-8859-1")
else:
    os.chdir(r"C:\Users\Vishal Gupta\Desktop\ask-multiple-pdfs")
    df = pd.read_csv("Sample - Superstore.csv", encoding="ISO-8859-1")

col1, col2 = st.columns(2)
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Getting the nim and max date

start_date = df['Order Date'].min()
end_date = df['Order Date'].max()

with col1:
    date1 = pd.to_datetime(st.date_input('Start Date', start_date))
with col2:
    date2 = pd.to_datetime(st.date_input('End Date', end_date))

df = df[(df['Order Date'] >= date1) & (df['Order Date'] <= date2)].copy()

st.sidebar.header("Choose Your Filter: ")

# Create for Region
region = st.sidebar.multiselect("Pick Your Region", df['Region'].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]

# Create for State
state = st.sidebar.multiselect("Pick Your State", df2['State'].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2["State"].isin(state)]

# Create for City
city = st.sidebar.multiselect("Pick Your City", df3['City'].unique())

# filter the data based on region, state, city
if not region and not state and not city:
    filtered_df = df
elif not state and not city:
    filtered_df = df[df["Region"].isin(region)]
elif not region and not city:
    filtered_df = df[df["State"].isin(state)]
elif state and city:
    filtered_df = df3[df["State"].isin(state) & df3["City"].isin(city)]
elif region and city:
    filtered_df = df3[df["Region"].isin(region) & df3["City"].isin(city)]
elif region and state:
    filtered_df = df3[df["Region"].isin(region) & df3["State"].isin(state)]
elif city:
    filtered_df = df3[df3['City'].isin(city)]
else:
    filtered_df = df3[df3['Region'].isin(region) & df3['State'].isin(state) & df3['City'].isin(city)]

category_df = filtered_df.groupby(by=["Category"], as_index=False)["Sales"].sum()

with col1:
    st.subheader("Category wise Sales")
    fig = px.bar(category_df, x="Category", y="Sales", text=['${:,.2f}'.format(x) for x in category_df["Sales"]],
                 template="seaborn")
    st.plotly_chart(fig, use_container_width=True, height=200)

with col2:
    st.subheader('Region wise Sales')
    fig = px.pie(filtered_df, values='Sales', names='Region', hole=0.5)
    fig.update_traces(text=filtered_df['Region'], textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

cl1, cl2 = st.columns(2)
with cl1:
    with st.expander("Category_viewData"):
        st.write(category_df.style.background_gradient(cmap="Blues"))
        csv = category_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name='Category.csv', mime="text/csv",
                           help="Click here to download the data as csv file")

with cl2:
    with st.expander("Region_viewData"):
        region = filtered_df.groupby(by="Region", as_index=False)["Sales"].sum()
        st.write(region.style.background_gradient(cmap="Oranges"))
        csv = region.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name='Region.csv', mime="text/csv",
                           help="Click here to download the data as csv file")

filtered_df['month_year'] = filtered_df['Order Date'].dt.to_period('M')
st.subheader("Time Series Analysis")

linechart = pd.DataFrame(
    filtered_df.groupby(filtered_df['month_year'].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
fig2 = px.line(linechart, x="month_year", y="Sales", labels={"Sales": "Amount"}, height=500, width=1000,
               template="gridon")
st.plotly_chart(fig2, use_container_width=True)

with st.expander("View Data of TimeSeries:"):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode('utf-8')
    st.download_button("Download Data", data=csv, file_name='TimeSeries.csv', mime="text/csv",
                       help="Click here to download the data as csv file")

# Create a tree map based on Region, Category, Sub-Category
st.subheader("Hierarchical view of Sales using TreeMap")
fig3 = px.treemap(filtered_df, path=['Region', 'Category', 'Sub-Category'], values="Sales", hover_data=['Sales'],
                  color="Sub-Category")
fig3.update_layout(width=800, height=650)
st.plotly_chart(fig3, use_container_width=True)


chart1, chart2 = st.columns(2)
with chart1:
    st.subheader("Segment wise Sales")
    fig = px.pie(filtered_df, values="Sales", names="Segment", template="plotly_dark")
    fig.update_traces(text=filtered_df['Segment'], textposition="inside")
    st.plotly_chart(fig, use_container_width=True)

with chart2:
    st.subheader("Category wise Sales")
    fig = px.pie(filtered_df, values="Sales", names="Category", template="gridon")
    fig.update_traces(text=filtered_df['Category'], textposition="inside")
    st.plotly_chart(fig, use_container_width=True)


st.subheader(":point_right: Month wise Sub_category Sales Summary")