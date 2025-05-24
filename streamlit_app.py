import streamlit as st
import subprocess
import tempfile
import os

def run_vina(receptor_path, ligand_path, output_path):
    cmd = [
        "vina",
        "--receptor", receptor_path,
        "--ligand", ligand_path,
        "--out", output_path,
        "--center_x", "0",
        "--center_y", "0",
        "--center_z", "0",
        "--size_x", "20",
        "--size_y", "20",
        "--size_z", "20",
        "--exhaustiveness", "8"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout, result.stderr

st.title("Simple AutoDock Vina Docking")

protein_file = st.file_uploader("Upload receptor (PDBQT)", type=["pdbqt"])
ligand_file = st.file_uploader("Upload ligand (PDBQT)", type=["pdbqt"])

if protein_file and ligand_file:
    with tempfile.TemporaryDirectory() as tmpdirname:
        receptor_path = os.path.join(tmpdirname, "receptor.pdbqt")
        ligand_path = os.path.join(tmpdirname, "ligand.pdbqt")
        output_path = os.path.join(tmpdirname, "docked_out.pdbqt")

        # Save uploaded files
        with open(receptor_path, "wb") as f:
            f.write(protein_file.getbuffer())
        with open(ligand_path, "wb") as f:
            f.write(ligand_file.getbuffer())

        if st.button("Run Docking"):
            st.info("Running AutoDock Vina...")
            stdout, stderr = run_vina(receptor_path, ligand_path, output_path)

            if stderr:
                st.error(f"Error:\n{stderr}")
            else:
                st.success("Docking completed!")
                st.text(stdout)
                st.download_button(
                    label="Download Docked Ligand",
                    data=open(output_path, "rb").read(),
                    file_name="docked_out.pdbqt",
                    mime="chemical/x-pdbqt"
                )
