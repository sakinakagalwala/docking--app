import streamlit as st
import time

st.set_page_config(page_title="Docking Demo App", layout="centered")

# Sidebar info
st.sidebar.title("About")
st.sidebar.info("""
This is a demo docking app for demonstration purposes only.  
No real docking is performed here.  
Uploads receptor and ligand files (PDBQT format) and simulates docking.
""")

st.title("Protein-Ligand Docking Demo")

st.markdown("""
Upload your receptor and ligand files in **PDBQT format** to run a mock docking simulation.  
This demo app is designed to showcase your docking workflow UI.
""")

# File uploads
protein_file = st.file_uploader("Upload Receptor (PDBQT file)", type=["pdbqt"])
ligand_file = st.file_uploader("Upload Ligand (PDBQT file)", type=["pdbqt"])

# Optional docking parameters section
with st.expander("Docking Parameters (mock)"):

    exhaustiveness = st.slider("Exhaustiveness", 1, 20, 8)
    num_modes = st.slider("Number of Modes", 1, 10, 9)
    energy_range = st.slider("Energy Range (kcal/mol)", 1.0, 5.0, 3.0)

if protein_file and ligand_file:
    if st.button("Run Docking"):
        with st.spinner("Running docking simulation..."):
            time.sleep(3)  # simulate waiting

        st.success("Docking completed successfully!")

        # Show mock results
        st.markdown(f"""
        **Results:**  
        - Predicted Binding Energy: **-7.5 kcal/mol**  
        - Exhaustiveness: {exhaustiveness}  
        - Number of Modes: {num_modes}  
        - Energy Range: {energy_range} kcal/mol
        """)

        # Provide dummy output file download
        dummy_output = b"""REMARK  DUMMY DOCKED LIGAND FILE
HETATM    1  C   LIG     1       0.000   0.000   0.000  1.00  0.00           C
END
"""
        st.download_button(
            label="Download Docked Ligand File",
            data=dummy_output,
            file_name="docked_ligand.pdbqt",
            mime="chemical/x-pdbqt"
        )
else:
    st.info("Please upload both receptor and ligand files to enable docking.")

# Footer
st.markdown("---")
st.caption("Demo app created by Sakina Kagalwala")

