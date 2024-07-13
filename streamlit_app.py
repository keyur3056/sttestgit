import streamlit as st
from streamlit_option_menu import option_menu

from pathlib import Path

with st.sidebar:
    
    st.image(str(Path(__file__).with_name("cardlogo.jpg")), width=50)

    select = option_menu(
        menu_title = None,
        options=["Home","database","visuals","Audio", "Contact"],
        icons=["house","database", "speedometer2", "soundwave","telephone"]
    )



st.image(str(Path(__file__).with_name("cardlogo.jpg")), width=50)


select = option_menu(
menu_title = None,
options=["Home","database","visuals","Audio", "Contact"],
icons=["house","database", "speedometer2", "soundwave","telephone"],
orientation="horizontal" 
)

#st.image("cardlogo.jpg")


st.text("ggggg")

st.metric(label="mylabl",value=67/5, delta="2.7m")
st.metric(label="mylabl",value=67/5, delta="2.7m")
st.metric(label="mylabl",value=67/5, delta="2.7m")