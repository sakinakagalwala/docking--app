import streamlit as st
import time
import random

st.set_page_config(page_title="🔬 Molecular Docking Simulator", layout="wide")

# ---- HEADER ----
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🔬 Molecular Docking Simulator</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size:16px; color: #555;'>Upload your receptor and ligand PDBQT files, set parameters, and simulate docking results instantly.</p>",
    unsafe_allow_html=True,
)

st.write("---")

# ---- FILE UPLOADS ----
col1, col2 = st.columns(2)
with col1:
    protein_file = st.file_uploader("🧬 Upload Receptor (PDBQT)", type=["pdbqt"])
with col2:
    ligand_file = st.file_uploader("⚛️ Upload Ligand (PDBQT)", type=["pdbqt"])

st.write("")

# ---- PARAMETERS ----
with st.expander("⚙️ Docking Parameters", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        exhaustiveness = st.slider("Exhaustiveness", 1, 32, 8, help="Higher value increases thoroughness but takes longer.")
    with col2:
        num_modes = st.slider("Number of Binding Modes", 1, 20, 9)
    with col3:
        energy_range = st.slider("Energy Range (kcal/mol)", 1.0, 10.0, 3.0)

st.write("")

# ---- RUN BUTTON ----
if protein_file and ligand_file:
    if st.button("▶️ Run Docking Simulation"):
        with st.spinner("Running docking simulation... please wait ⏳"):
            time.sleep(3)  # simulate processing time

        # Fake results generation
        predicted_affinity = round(random.uniform(-12, -6), 2)
        rmsd_lower_bound = round(random.uniform(0.5, 1.5), 2)
        rmsd_upper_bound = round(random.uniform(1.5, 3.0), 2)

        st.success("✅ Docking completed successfully!")

        # Results displayed side by side
        rcol1, rcol2 = st.columns(2)
        with rcol1:
            st.subheader("📊 Results Summary")
            st.markdown(f"""
            - **Predicted Binding Affinity:**  
              <span style='color:#e76f51; font-weight:bold;'>{predicted_affinity} kcal/mol</span>
            - **Number of Modes Analyzed:** {num_modes}  
            - **Energy Range:** {energy_range} kcal/mol
            """, unsafe_allow_html=True)

        with rcol2:
            st.subheader("📐 RMSD Values")
            st.markdown(f"""
            - **RMSD Lower Bound:**  
              <span style='color:#2a9d8f; font-weight:bold;'>{rmsd_lower_bound} Å</span>
            - **RMSD Upper Bound:**  
              <span style='color:#2a9d8f; font-weight:bold;'>{rmsd_upper_bound} Å</span>
            - **Exhaustiveness:** {exhaustiveness}
            """, unsafe_allow_html=True)

        # Dummy download file
        dummy_output = b"""REMARK  DUMMY DOCKED LIGAND FILE
HETATM    1  C   LIG     1       0.000   0.000   0.000  1.00  0.00           C
END
"""
        st.download_button(
            label="📥 Download Docked Ligand File",
            data=dummy_output,
            file_name="docked_ligand.pdbqt",
            mime="chemical/x-pdbqt",
            use_container_width=True,
        )
else:
    st.info("📂 Please upload both receptor and ligand PDBQT files to enable docking.")

st.write("---")
st.markdown("<center>© 2025 Molecular Docking Simulation App — Made with ❤️ by Sakina</center>", unsafe_allow_html=True)


