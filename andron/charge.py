import tempfile
import os

import parmed as pmd

__all__ = ['assign_charge']

def assign_charge(struct_in, net_charge=0):
    #antechamber -i prcarb.pdb -fi pdb -o prcarb.mol2 -fo mol2 -c bcc -nc 0
    tmp_dir = tempfile.mkdtemp()
    input_file = os.path.join(tmp_dir, 'input.pdb')
    output_file = os.path.join(tmp_dir, 'output.mol2')
    struct_in.save(input_file)
    os.system('antechamber -i {0} -fi pdb -o {1} -fo mol2 -c bcc -nc {2} -pf y'.format(
        input_file, output_file, net_charge))
    struct_out = pmd.load_file(output_file)
    struct_out.fix_charges()
    return struct_out
