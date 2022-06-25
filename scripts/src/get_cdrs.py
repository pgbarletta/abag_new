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
# Get the list of CDR residues, dealing with the characters on the resSeqs.
###

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

    cdr_residues = {}
    KtoL = {'H': 'H', 'L': 'L', 'K': 'L'}
    letras = dict(zip(range(0, len(string.ascii_uppercase)),
                      tuple(string.ascii_uppercase)))
    # check_pdb = '2zuq'
    # idx = pdb_list.index(check_pdb)
    # for pdb_idcode in [pdb_list[idx]]:
    for pdb_idcode in pdb_list:
        logging.info(pdb_idcode)

        pdb_filename = Path(filenames[pdb_idcode])
        trj_in = md.load(Path.joinpath(exposed_dir, pdb_idcode, pdb_filename))
        ab_chains = chains[pdb_idcode].antibody
        ag_chains = chains[pdb_idcode].antigen

        try:
            cdr_residues_pdb = {}

            for row in epitope_buried_cleaned.query(
                    f"idcode == '{pdb_idcode}'").iterrows():
                chainID = row[1].chainID
                if chainID not in ab_chains:
                    continue
                chain_type = KtoL[row[1].chain_type]
                cdr = int(row[1].cdr)
                cdr_id = chain_type + str(cdr)
                # Deal with characters in `cdr_begin` and `cdr_begin`:
                try:
                    beg = int(row[1].cdr_begin)
                except ValueError:
                    beg = int(row[1].cdr_begin[:-1])
                try:
                    end = int(row[1].cdr_end)
                except ValueError:
                    end = int(row[1].cdr_end[:-1])
                cdr_range = range(beg, end)

                # Get the list of CDR residues as MDtraj residues
                cderes = tuple([residue for residue in trj_in.topology.residues if (
                    beg <= residue.resSeq <= end) and (residue.chain.chain_id == chainID)])

                # Now convert the CDR MDtraj residues to my residue format
                list_resis = []
                prev_residue = cderes[0]
                list_resis.append(
                    Residue(
                        index=prev_residue.index, resSeq=prev_residue.resSeq,
                        resSeq_str=str(prev_residue.resSeq),
                        resname=prev_residue.name, chain_ID=chainID,
                        chain_type=chain_type, CDR=cdr, SSE=''))
                letter_counter = 0
                for residue in cderes[1:]:
                    resSeq = residue.resSeq
                    prev_resSeq = prev_residue.resSeq
                    if resSeq == prev_resSeq:
                        resSeq_str = str(residue.resSeq) + letras[letter_counter]
                        letter_counter += 1
                    else:
                        resSeq_str = str(residue.resSeq)
                        prev_residue = residue

                    list_resis.append(
                        Residue(
                            index=residue.index, resSeq=resSeq, resSeq_str=resSeq_str,
                            resname=residue.name, chain_ID=chainID,
                            chain_type=chain_type, CDR=cdr, SSE=''))
                cdr_residues_pdb[cdr_id] = tuple(list_resis)
        except Exception as e:
            logging.exception(e)
            logging.error(f" {pdb_idcode} CDRs residues look-up failed.")
            continue

        cdr_residues[pdb_idcode] = cdr_residues_pdb

    with open(Path.joinpath(data_dir, 'cdr_residues.pkl'), 'wb') as file:
        pickle.dump(cdr_residues, file)
