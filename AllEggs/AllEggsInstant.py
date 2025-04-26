import streamlit as st
import math

petlist = {
    "Emerald Golem": 0.5,
    "Inferno Dragon": 0.25,
    "Unicorn": 0.25,
    "Flying Pig": 0.1,
    "Lunar Serpant": 0.25,
    "Electra": 0.1,
    "Dark Phoenix": 0.05,
    "Neon Elemental": 0.02,
    "Null Void": 0.00001,
    "Inferno Cube": 0.025,
    "Virus": 0.002, 
    "Green Hydra": 0.004,
    "Demonic Hydra": 0.001,
    "Hexarium": 0.001,
    "Rainbow Shock": 0.0005,
}

chosen_pet = st.selectbox("Pet", petlist, None)


hatch_speed = st.number_input("Hatch Speed (%)", min_value=1, max_value=1000, value=160, step=10)
luck_multiplier = st.slider("Luck Multiplier", 1, 2700, 50, 1)
shiny_chance = st.slider("Shiny Chance (1 in X)", 13, 40, 40)
mythic_chance = st.slider("Mythic Chance (1 in X)", 12, 100, 100)
eggs_to_open = st.slider("Number of Eggs you Hatch at Once", 1, 6, 6)
num_hatches = math.trunc(((time_spent*(0.1375*hatch_speed))*eggs_to_open))
str_num_hatches = st.text("Number of Eggs Hatched: " + str(num_hatches))

if chosen_pet != None:
    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        pet_name = st.title(chosen_pet)
        pet_image = st.image("https://www.bgsi.gg/items/"+ str(chosen_pet).replace(' ', '-').lower() +".png")
    with col2:
        rarity = st.text(str(petlist[chosen_pet]) + "%")