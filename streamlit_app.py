import streamlit as st
import subprocess
import tempfile
import os

st.title("Simple Molecular Docking with AutoDock Vina")

st.markdown("""
Upload your protein (PDBQT) and ligand (PDBQT) files below and run docking.
Ensure AutoDock Vina is installed and accessible in your system PATH.
""")

protein = st.file_uploader("Upload Protein (PDBQT)", type=["pdbqt"])
ligand = st.file_uploader("Upload Ligand (PDBQT)", type=["pdbqt"])

exhaustiveness = st.slider("Exhaustiveness", 1, 20, 8)
num_modes = st.slider("Number of Modes", 1, 20, 9)

if st.button("Run Docking"):

    if protein is None or ligand is None:
        st.error("Please upload both protein and ligand files.")
    else:
        with tempfile.TemporaryDirectory() as tmpdir:
            protein_path = os.path.join(tmpdir, "protein.pdbqt")
            ligand_path = os.path.join(tmpdir, "ligand.pdbqt")
            out_path = os.path.join(tmpdir, "out.pdbqt")

            # Save uploaded files to temp directory
            with open(protein_path, "wb") as f:
                f.write(protein.getbuffer())
            with open(ligand_path, "wb") as f:
                f.write(ligand.getbuffer())

            # Define docking box parameters (simple example, you can customize)
            center_x, center_y, center_z = 0, 0, 0
            size_x, size_y, size_z = 20, 20, 20

            cmd = [
                "vina",
                "--receptor", protein_path,
                "--ligand", ligand_path,
                "--center_x", str(center_x),
                "--center_y", str(center_y),
                "--center_z", str(center_z),
                "--size_x", str(size_x),
                "--size_y", str(size_y),
                "--size_z", str(size_z),
                "--exhaustiveness", str(exhaustiveness),
                "--num_modes", str(num_modes),
                "--out", out_path
            ]

            try:
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                st.success("Docking finished successfully!")
                st.text("Vina output:\n" + result.stdout)

                # Show docking output file content
                with open(out_path, "r") as f:
                    docking_result = f.read()
                st.text_area("Docking Result (PDBQT)", docking_result, height=300)

                # Optionally let user download the result file
                st.download_button(
                    label="Download Docked Ligand (PDBQT)",
                    data=docking_result,
                    file_name="docked_ligand.pdbqt",
                    mime="text/plain"
                )

            except subprocess.CalledProcessError as e:
                st.error("Error running AutoDock Vina:")
                st.text(e.stderr)
