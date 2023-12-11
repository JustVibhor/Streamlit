# import streamlit as st
# import pandas as pd

# st.write(""" 
#          # Nice
#          Pretty wacky stuff! *
#          """)

# df = pd.read_csv("https://github.com/datablist/sample-csv-files/blob/main/files/people/people-100.csv")

import streamlit as st
import numpy as np
import pandas as pd
import streamlit as st
import time



dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

if st.checkbox('show Table 1'):
    st.dataframe(dataframe.style.highlight_max(axis=0))

if st.checkbox('Show Table 2'):
    st.write("Table 2")
    st.table(dataframe)
    
    
if st.checkbox("Show Remaining things"):
    st.line_chart(
        pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )
    )

    x = st.slider('x')  # 👈 this is a widget
    st.write(x*2, 'squared is', (x * x)/100)

    st.text_input("Your name", key="name")


    # You can access the value at any point with:
    st.write(st.session_state.name)

    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [x, 79.0193],  # Delhi's approximate coordinates
        columns=['delhi_lat', 'delhi_lon']
    )

    # Rename columns to 'lat' and 'lon'
    map_data = map_data.rename(columns={'delhi_lat': 'lat', 'delhi_lon': 'lon'})

    # Display the map using Streamlit
    st.map(map_data)
    
    
df = pd.DataFrame({
    'third column': [i for i in range(1, 101)]
    })

if st.checkbox("Show the dropbox"):
    option = st.selectbox(
        'Which number do you like best?',
        df['third column'])

    'You selected: ', option
    

if st.checkbox("Show Loading"):
    

    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
    # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.01)

    '...and now we\'re done!'


    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.button('Press me!')

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")