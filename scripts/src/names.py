from collections import namedtuple

InterfaceAtoms = namedtuple('InterfaceAtoms', ['antibody', 'antigen'])
ResiCount = namedtuple('ResiCount', ['antibody', 'antigen'])
Residue = namedtuple('Residue',
                     ['index', 'resSeq', 'resSeq_str', 'resname', 'chain_ID',
                      'chain_type', 'CDR', 'SSE'])
TYRs = namedtuple('TYRs', ['heavy', 'light', 'antigen'])
AA_count = namedtuple('AA_count', ['heavy', 'light', 'antigen'])
PiPiPair = namedtuple('PiPiPair', ['antibody', 'antigen'])
PionPair = namedtuple('PionPair', ['ring', 'ion'])
HBondAtom = namedtuple('HBondAtom', ['chainID', 'chain_type',
                       'CDR', 'resSeq', 'resname', 'index', 'serial', 'element', 'is_sidechain'])
HBond = namedtuple('HBond', ['donor', 'acceptor'])
# Water mediated doesnt' care about donor/acceptor.
WBond = namedtuple('WBond', ['water', 'residue'])
ShieldingAtom = namedtuple(
    'ShieldingAtom', ['chainID', 'chain_type', 'CDR', 'resSeq', 'resname', 'index',
                      'serial', 'element', 'is_sidechain'])
PolarCount = namedtuple('PolarCount', ['cdr_SC', 'cdr_BB', 'epi_SC', 'epi_BB'])
Chains = namedtuple('Chains', ['antibody', 'antigen'])
Atom = namedtuple('Atom', ['index', 'serial', 'element', 'is_sidechain', 'resSeq',
                  'resSeq_str', 'resname', 'chain_ID', 'chain_type', 'CDR'])
ShieldingAtom = namedtuple(
    'ShieldingAtom', ['chainID', 'chain_type', 'CDR', 'resSeq', 'resname', 'index',
                      'serial', 'element', 'is_sidechain'])
AA_LIST = ["ALA", "ARG", "ASN", "ASP", "CYS", "GLU", "GLN", "GLY", "HIS",
           "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL"]
AA_SET = {"ALA", "ARG", "ASN", "ASP", "CYS", "GLU", "GLN", "GLY", "HIS",
           "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL"}
