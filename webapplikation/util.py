# Used for accessability changes of webapplication
## the functions of this script are imported in accessability_contrast.py

import re
import random
from colorsys import hls_to_rgb
from typing import NamedTuple

import streamlit as st
import wcag_contrast_ratio as contrast


class ThemeColor(NamedTuple):
    primaryColor: str
    backgroundColor: str
    secondaryBackgroundColor: str
    textColor: str

# retrieve the theme colors from the Streamlit configuration options and return them as a ThemeColor named tuple. 
@st.cache_resource
def get_config_theme_color():
    config_theme_primaryColor = st._config.get_option('theme.primaryColor')
    config_theme_backgroundColor = st._config.get_option('theme.backgroundColor')
    config_theme_secondaryBackgroundColor = st._config.get_option('theme.secondaryBackgroundColor')
    config_theme_textColor = st._config.get_option('theme.textColor')
    if config_theme_primaryColor and config_theme_backgroundColor and config_theme_secondaryBackgroundColor and config_theme_textColor:
        return ThemeColor(
            primaryColor=config_theme_primaryColor,
            backgroundColor=config_theme_backgroundColor,
            secondaryBackgroundColor=config_theme_secondaryBackgroundColor,
            textColor=config_theme_textColor,
        )

    return None

# take a hexadecimal color string and converts it to a tuple of floats representing the RGB values of the color.
def parse_hex(rgb_hex_str: str) -> tuple[float, float, float]:
    if not re.match(r"^#[0-9a-fA-F]{6}$", rgb_hex_str):
        raise ValueError("Invalid hex color")
    return tuple(int(rgb_hex_str[i:i+2], 16) / 255 for i in (1, 3, 5))

# function generates random color in HLS (Hue, Lightness, Saturation) color space. It adjusts the lightness value to ensure it falls within a certain range.
def random_hls():
    h = random.random()
    l = random.random()
    s = random.random()

    MAX_LIGHTNESS = 0.3
    if l < 0.5:
        l = l * (MAX_LIGHTNESS / 0.5)
    else:
        l = 1 - l
        l = l * (MAX_LIGHTNESS / 0.5)
        l = 1 - l
    return (h, l, s)

# take a color in the HLS color space and returns a new color with the lightness inverted, creating a high contrast effect.
def high_contrast_color(color):
    h, l, s = color
    l = 1 - l
    return (h, l, s)

# function converts an HLS color to a hexadecimal color string.
def hls_to_hex(color):
    r, g, b = hls_to_rgb(*color)
    return "#{:02x}{:02x}{:02x}".format(round(r * 255), round(g * 255), round(b * 255))


# function attempts to find a color that has a sufficient contrast ratio with a base color.
def find_color_with_contrast(base_color, min_contrast_ratio, max_attempts):
    for _ in range(max_attempts):
        candidate_color = random_hls()
        if contrast.rgb(hls_to_rgb(*candidate_color), hls_to_rgb(*base_color)) > min_contrast_ratio: #  generates random candidate colors and checks their contrast ratio using the contrast.rgb() function from the wcag_contrast_ratio module.
            return candidate_color
    return high_contrast_color(base_color)

# generating a complete color scheme by calling the above functions.  
def generate_color_scheme():
    primary_color = random_hls() # generate primary color
    basic_background = high_contrast_color(primary_color) #generate basic background color

    text_color = find_color_with_contrast(basic_background, 7, 100)
    secondary_background = find_color_with_contrast(primary_color, 7, 100) # a text color with sufficient contrast, and a secondary background color with sufficient contrast.

    return hls_to_hex(primary_color), hls_to_hex(text_color), hls_to_hex(basic_background), hls_to_hex(secondary_background)