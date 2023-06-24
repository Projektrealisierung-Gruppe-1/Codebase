# Used for accessability changes of webapplication
## the functions of this script are imported in accessability_contrast.py

import streamlit as st
import wcag_contrast_ratio as contrast
import util

# display a contrast summary between a foreground color and a background color.
def contrast_summary(label: str, foreground_rgb_hex: str, background_rgb_hex: str) -> None:
    rgb_foreground = util.parse_hex(foreground_rgb_hex)
    rgb_background = util.parse_hex(background_rgb_hex)
    contrast_ratio = contrast.rgb(rgb_foreground, rgb_background)
    contrast_ratio_str = f"{contrast_ratio:.2f}"

    st.metric(label, value=f"{contrast_ratio_str} : 1", label_visibility="collapsed")

    if contrast.passes_AAA(contrast_ratio):
        st.markdown(":white_check_mark: :white_check_mark: WCAG AAA")
    elif contrast.passes_AA(contrast_ratio):
        st.markdown(":white_check_mark: WCAG AA")
    else:
        st.markdown(":x: Fail WCAG")

    st.markdown(f'<p style="color: {foreground_rgb_hex}; background-color: {background_rgb_hex}; padding: 12px">Lorem ipsum</p>', unsafe_allow_html=True)

# display a set of sample components for testing accessibility. 
def sample_components(key: str):
    st.header("Sample components")
    st.text_input("Text input", key=f"{key}:text_input")
    st.slider("Slider", min_value=0, max_value=100, key=f"{key}:slider")
    st.button("Button", key=f"{key}:button")
    st.checkbox("Checkbox", key=f"{key}:checkbox", value=True)
    st.radio("Radio", options=["Option 1", "Option 2"], key=f"{key}:radio")
    st.selectbox("Selectbox", options=["Option 1", "Option 2"], key=f"{key}:selectbox")