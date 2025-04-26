import time
import streamlit as st
import random
from collections import defaultdict

# Pet Pools
SECRET_PETS = {
    "Secret - Overlord": 20,
    "Secret - GCC": 20,
    "Secret - Easter Basket": 10,
    "Secret - King Doggy": 10,
    "Secret - Godly Gem": 4,
    "Secret - Dementor": 1,
}

TIER3_PETS = {
    "Tier 3 Legendary - Dualcorn": 20,
    "Tier 3 Legendary - Virus": 20,
    "Tier 3 Legendary - Rainbow Marshmellow": 8,
    "Tier 3 Legendary - Demonic Hydra": 10,
    "Tier 3 Legendary - Hexarium": 10,
    "Tier 3 Legendary - Ethereal Bunny": 10,
    "Tier 3 Legendary - Rainbow Shock": 5,
    "Tier 3 Legendary - Holy Egg": 2,
    "Tier 3 Legendary - Cardinal Bunny": 1,
    "Tier 3 Legendary - Nullvoid": 1,
}

# Weighted random helper
def weighted_random_choice(pet_weights):
    total = sum(pet_weights.values())
    r = random.uniform(0, total)
    upto = 0
    for pet, weight in pet_weights.items():
        if upto + weight >= r:
            return pet
        upto += weight
    return random.choice(list(pet_weights.keys()))

# Apply Shiny/Mythic
def apply_multipliers(pet, shiny_chance, mythic_chance):
    shiny = random.random() < shiny_chance
    mythic = random.random() < mythic_chance
    if shiny and mythic:
        return pet + " [Shiny+Mythic]"
    elif shiny:
        return pet + " [Shiny]"
    elif mythic:
        return pet + " [Mythic]"
    return pet

# GUI
st.title("Infinity Egg Simulator")

num_hatches = st.number_input("Number of Eggs to Simulate", min_value=1, max_value=10_000_000, value=100_000, step=1000)
luck_multiplier = st.slider("Luck Multiplier", 1.0, 27.0, 1., 0.1)
shiny_chance = st.slider("Shiny Chance (1 in X)", 13, 40, 40)
mythic_chance = st.slider("Mythic Chance (1 in X)", 12, 100, 100)
eggs_to_open = st.slider("Number of Eggs to Hatch at Once", 1, 6, 6)
skip_animation = st.checkbox("Skip Animation (Instant Results)")

# Track pet hatch history
results = defaultdict(int)
shiny_counts = defaultdict(int)
mythic_counts = defaultdict(int)
shiny_mythic_counts = defaultdict(int)

# Run simulation
if st.button("Run Simulation"):
    shiny_chance_val = 1 / shiny_chance
    mythic_chance_val = 1 / mythic_chance

    SECRET_BASE_CHANCE = 1 / 50_000_000
    TIER3_BASE_CHANCE = 1 / 50_000

    secret_chance = SECRET_BASE_CHANCE * luck_multiplier
    tier3_chance = TIER3_BASE_CHANCE * luck_multiplier

    iterations = num_hatches // eggs_to_open

    # Simulation without animation (Instant hatch, no delay)
    for batch in range(iterations):
        current_eggs = []
        for egg in range(eggs_to_open):
            pet = "Common"
            roll = random.random()
            if roll < secret_chance:
                pet = weighted_random_choice(SECRET_PETS)
            elif roll < tier3_chance + secret_chance:
                pet = weighted_random_choice(TIER3_PETS)
            else:
                continue  # Skip recording commons

            # Apply multipliers
            final_pet = apply_multipliers(pet, shiny_chance_val, mythic_chance_val)

            # Record results
            base_pet = pet
            results[base_pet] += 1
            if "[Shiny+Mythic]" in final_pet:
                shiny_mythic_counts[base_pet] += 1
            elif "[Shiny]" in final_pet:
                shiny_counts[base_pet] += 1
            elif "[Mythic]" in final_pet:
                mythic_counts[base_pet] += 1

            current_eggs.append(final_pet)

    # Final summary (no animation, direct output)
    st.subheader("Final Summary")
    for pet in sorted(results.keys()):
        st.write(
            f"{pet}: {results[pet]}, S {shiny_counts[pet]}, M {mythic_counts[pet]}, SM {shiny_mythic_counts[pet]}"
        )

    st.success("Simulation Complete!")
