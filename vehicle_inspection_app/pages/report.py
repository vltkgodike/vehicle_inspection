

import streamlit as st
import os
from io import StringIO
import time

# ---------------------------#
# ✅ Streamlit Page Config
# ---------------------------#
st.set_page_config(page_title="Inspection Report", layout="centered")
st.title("📄 Vehicle Inspection Report")

# ---------------------------#
# ✅ Check if results exist
# ---------------------------#
if "inspection_results" not in st.session_state or not st.session_state.inspection_results:
    st.warning("⚠️ No inspection data found. Please run an inspection first.")
    st.stop()

results = st.session_state.inspection_results

# ---------------------------#
# 🧠 Model Detection Summary
# ---------------------------#
st.subheader("🔍 Detection Summary")

# Generate report text
report_text = StringIO()
report_text.write("Inspection Report\n\n")

selected_modules = list(results.keys())
report_text.write(f"Selected modules: {', '.join(selected_modules)}\n\n")
report_text.write("Detected (sample):\n")

# Display detection results and build text report
for module, data in results.items():
    detections = data.get("Detections", 0)
    # confidence = data.get("Confidence", "N/A")
    image_path = data.get("Result Path", None)

    # Display output image
    if image_path and os.path.exists(image_path):
        st.image(image_path, caption=f"{module} Detection Result")

    # Detection info under each image
    st.markdown(f"### {module}")
    st.divider()

    # Add to text report
    report_text.write(f"{module}: {detections}\n")

report_text.write("\n✅ End of Report ✅\n")

# ---------------------------#
# 📄 Download Report
# ---------------------------#
st.subheader("⬇️ Download Inspection Report")

st.download_button(
    label="📥 Download Report as TXT",
    data=report_text.getvalue(),
    file_name="inspection_report.txt",
    mime="text/plain"
)

# ---------------------------#
# 🔙 Back Button
# ---------------------------#
st.divider()
st.markdown("### Navigation")
if st.button("⬅️ Back to Inspection Module"):
    st.info("Navigating back to the inspection module...")
    time.sleep(1)
    st.switch_page("pages/upload_inspection.py")


