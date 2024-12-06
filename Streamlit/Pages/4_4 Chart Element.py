import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.header("4. Chart Elements : Streamlit based/ Matplotlib based")

st.write("0. Initialization : data/library initialization")
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C'])

st.code(""" import numpy as np
import pandas as pd
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C'])
st.dataframe(chart_data)""")

st.dataframe(chart_data)

st.divider()

st.write("1. Line Chart :")
st.code("""st.line_chart(chart_data)""")
st.line_chart(chart_data)

st.divider()

st.write("2. Area Chart :")
st.code("""st.area_chart(chart_data)""")
st.area_chart(chart_data)

st.divider()

st.write("3. Bar Chart :")
st.code("""st.bar_chart(chart_data)""")
st.bar_chart(chart_data)

st.divider()

st.write("4. Scatter Chart :")
st.code("""scatter_data = pd.DataFrame({ 'x' :np.random.randn(100),
                              'y' :np.random.randn(100)})
st.scatter_chart(scatter_data)""")
scatter_data = pd.DataFrame({ 'x' :np.random.randn(100),
                              'y' :np.random.randn(100)})
st.scatter_chart(scatter_data)

st.divider()

st.write("5. Line Chart (Matplotlib) :")
st.code("""fig,ax = plt.subplots()
ax.plot(chart_data['A'],label='A')
ax.plot(chart_data['B'],label='B')
ax.plot(chart_data['C'],label='C')
ax.set_title("Pyplot Line Chart")
ax.legend()
st.pyplot(fig)""")

fig,ax = plt.subplots()
ax.plot(chart_data['A'],label='A')
ax.plot(chart_data['B'],label='B')
ax.plot(chart_data['C'],label='C')
ax.set_title("Pyplot Line Chart")
ax.legend()
st.pyplot(fig)

st.divider()

st.write("6. Map (based on co-ordinates) :")
st.code("""map_data = pd.DataFrame(
    np.random.rand(100,2)/ [50,50] + [23.04,72.47],
    columns=['lat','lon'])
st.map(map_data,size=50,height=370)""")

map_data = pd.DataFrame(
    np.random.rand(100,2)/ [50,50] + [23.04,72.47],
    columns=['lat','lon'])
st.map(map_data,size=50,height=370)
st.divider()
st.subheader("Help :")
st.page_link("Help.py",label = "Click Here")
st.divider()
