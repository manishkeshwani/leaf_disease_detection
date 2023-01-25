import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(menu_title = "Navigation Bar",
                           
                           options=['Home','About'],
                           
                           icons=['activity','activity'],
                           
                           menu_icon = 'cast',
                                                     
                           orientation = 'vertical',
                           
                           default_index = 0)

# Home page 
if(selected == 'Home'):
    st.title("Plant Disease Detection System")
    st.markdown('---')
    image = st.file_uploader("Please Upload an Image",type=['jpg','png','jpeg'])

    if image is not None:
        st.image(image)
        st.success(image)
    

# About page    
if(selected == 'About'):
    st.title("About")
    st.markdown('---')

    col1,col2,col3,col4 = st.columns(4)

    image2 = "Manish.jpg"

    with col1:
        st.image(image2)
        st.success('Manish Keshwani')
    with col2:
        st.image(image2)
        st.success('Manish Keshwani')
    with col3:
        st.image(image2)
        st.success('Manish Keshwani')
    with col4:
        st.image(image2)
        st.success('Manish Keshwani')




