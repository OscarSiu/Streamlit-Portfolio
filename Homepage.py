import streamlit as st
from constant import *
from PIL import Image
from st_functions import st_button, load_css
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from streamlit_extras.badges import badge

st.set_page_config(page_title='Oscar\'s portfolio' ,layout="centered",page_icon='✈️')

load_css()


## use tab

#####################
# Header 
st.write('# Siu Cheuk Yin Oscar')
image = Image.open('profile.JPG')
st.image(image)

#st.markdown('## Summary', unsafe_allow_html=True)
st.info('Engineer | Robotics and Intelligent Systems, Connected and Autonomous Vehicles, ROS, Computer Vision, CAD design')

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)


#####################
st.subheader('Education 📖')

txt('**Bachelor of Engineering** (Mechanical and Automation Engineering), *CUHK*',
'2015-2019')
st.markdown('''
- Honour: `Second Class Upper Division`
- Research topic: `Obstacle Detection by Laser Scanners of Autonomous Vehicles`.
- Course Covered: `Complex Analysis and Different Equations for Engineers, Mechanics of Materials, Fluid Mechanics, Introduction to Robotics`
''')


#####################
st.subheader('Career snapshot👨‍💻️')
    
with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)


#####################
st.subheader('Skills & Tools ⚒️')
def skill_tab():
    rows,cols = len(info['skills'])//skill_col_size,skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()

#####################
st.subheader('Social Media 🔗')
icon_size = 20
st_button('linkedin', 'http://www.linkedin.com/in/siucheukyin', 'Follow me on LinkedIn', icon_size)
st_button('git', 'https://github.com/OscarSiu', 'Check out my works on Github', icon_size)
badge(type="github", name="OscarSiu/NTRIP-Client")