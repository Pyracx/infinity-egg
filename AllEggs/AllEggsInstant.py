import streamlit as st

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

first_column = st.columns([0.25, 0.75])
chosen_pet = st.selectbox("Pet", petlist, None)
pet_image = st.image("https://www.bgsi.gg/items/"+ str(chosen_pet).replace(' ', '-').lower() +".png")
pet_name = st.text(chosen_pet)
rarity = st.text(str(petlist[chosen_pet] + "%"))