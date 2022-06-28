import pickle
import sys
import string
from pathlib import Path
import logging
import freesasa
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

    with open(Path.joinpath(casa_dir, 'data', 'cdr_residues.pkl'), 'rb') as file:
        cdr_residues = pickle.load(file)
    with open(Path.joinpath(casa_dir, 'data', 'filenames.pkl'), 'rb') as file:
        filenames = pickle.load(file)
    with open(Path.joinpath(casa_dir, 'data', 'chains.pkl'), 'rb') as file:
        chains = pickle.load(file)
    with(open(Path.joinpath(data_dir, 'pdb.list'), 'r')) as file:
        pdb_list = [linea.strip() for linea in file]
    print("Starting now.")

    surface_cdrh3 = {}
    # check_pdb = '1adq'
    # idx = pdb_list.index(check_pdb)
    # for pdb_idcode in [pdb_list[idx]]:
    for pdb_idcode in pdb_list:
        logging.info(pdb_idcode)

        pdb_filename = Path(filenames[pdb_idcode])
        pdb_file = Path.joinpath(exposed_dir, pdb_idcode, pdb_filename)
        # trj_in = md.load(Path.joinpath(exposed_dir, pdb_idcode, pdb_filename))
        ab_chains = chains[pdb_idcode].antibody
        ag_chains = chains[pdb_idcode].antigen
        seleccion = "h3, resi " + '+'.join(
            [resi.resSeq_str for resi in cdr_residues[pdb_idcode]['H3']])

        try:
            # structura = freesasa.Structure(str(pdb_file))
            # Separate chains to get the SASA of the free CDR H3
            structuras = freesasa.structureArray(
                str(pdb_file), {'separate-chains': True})

            for struct in structuras:
                if struct.chainLabel(0) == ab_chains[0]:
                    resultado = freesasa.calc(struct)
                    h3 = freesasa.selectArea([seleccion], struct, resultado)['h3']
                    break
            else:
                raise Exception("Couldn't match heavy-chain.")
            surface_cdrh3[pdb_idcode] = h3

        except Exception as e:
            logging.exception(e)
            logging.error(f" {pdb_idcode} CDR H3 surface calculation failed.")
            continue

    with open(Path.joinpath(data_dir, 'surface_cdrh3.pkl'), 'wb') as file:
        pickle.dump(surface_cdrh3, file)
