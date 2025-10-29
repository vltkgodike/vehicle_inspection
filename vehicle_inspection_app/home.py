
import streamlit as st

st.set_page_config(page_title="Vehicle Inspection - Home", layout="centered")

st.title("🚘 Vehicle Inspection System")
st.markdown("### Select the modules you want to run:")

# Active and Upcoming Modules
active_modules = ["Scratch", "Dent", "Corrosion", "Windshield"]
upcoming_modules = ["Tire (coming soon)", "Interior (coming soon)", "Underbody (coming soon)"]

# Multi-select for module selection
selected_modules = st.multiselect(
    "Choose Modules:",
    options=active_modules + upcoming_modules,
    help="Select one or more modules to perform inspection."
)

# Store selected modules in session state
if st.button("Next ➡️"):
    if not selected_modules:
        st.warning("Please select at least one module.")
    else:
        st.session_state.selected_modules = selected_modules
        st.switch_page("pages/upload_inspection.py")


