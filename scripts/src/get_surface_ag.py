import pickle
import sys
import string
from pathlib import Path
import logging
import mdtraj as md
source_location = (Path(__file__) / '..').resolve()
scripts_loc = (Path(__file__) / '..' / '..').resolve()
sys.path.append(source_location)
from names import *

casa_dir = (Path(__file__) / '..' / '..' / '..').resolve()
data_dir = Path.joinpath(casa_dir, "data")
str_dir = Path.joinpath(casa_dir, "structures/raw")
exposed_dir = Path.joinpath(casa_dir, "structures/exposed")
###
# Get the list of residues that make up the Antigen surface.
###


def get_resis(df, ag_chains):
    for row in df.iterrows():
        for resi in row[1].ag_interface_res:
            try:
                resSeq = int(resi[1].strip())
            except ValueError:
                resSeq = int(resi[1].strip()[:-1])
            if resi[0] in ag_chains:
                yield Residue(index=-1, resSeq=resSeq,
                              resSeq_str=resi[1].strip(), resname=resi[2],
                              chain_ID=resi[0], chain_type='.', CDR=-1, SSE='')


if __name__ == '__main__':
    logging.basicConfig(filename="log_" + Path(__file__).name, level=logging.INFO)

    with open(Path.joinpath(
            casa_dir, "data", 'epitope_buried_cleaned.pickle'), 'rb') as file:
        epitope_buried_cleaned = pickle.load(file)
    with open(Path.joinpath(casa_dir, 'data', 'filenames.pkl'), 'rb') as file:
        filenames = pickle.load(file)
    with open(Path.joinpath(casa_dir, 'data', 'chains.pkl'), 'rb') as file:
        chains = pickle.load(file)
    with(open(Path.joinpath(data_dir, 'pdb.list'), 'r')) as file:
        pdb_list = [linea.strip() for linea in file]
    print("Starting now.")

    surface_residues = {}
    # check_pdb = '1afv'
    # idx = pdb_list.index(check_pdb)
    # for pdb_idcode in [pdb_list[idx]]:
    for pdb_idcode in pdb_list:
        logging.info(pdb_idcode)

        # pdb_filename = Path(filenames[pdb_idcode])
        # trj_in = md.load(Path.joinpath(exposed_dir, pdb_idcode, pdb_filename))
        ab_chains = chains[pdb_idcode].antibody
        ag_chains = chains[pdb_idcode].antigen

        try:
            interface_tuples = {resi for resi in get_resis(
                epitope_buried_cleaned.query(f"idcode == '{pdb_idcode}'"), ag_chains)}
        except Exception as e:
            logging.exception(e)
            logging.error(f" {pdb_idcode} antigen's surface residue look-up failed.")
            continue

        surface_residues[pdb_idcode] = tuple(interface_tuples)

    with open(Path.joinpath(data_dir, 'surface_residues.pkl'), 'wb') as file:
        pickle.dump(surface_residues, file)
