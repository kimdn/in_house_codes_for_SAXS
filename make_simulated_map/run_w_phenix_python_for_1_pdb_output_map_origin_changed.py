# run with phenix.python make_fake_map.py
# it will produce result.mtz
# then do phenix.mtz2map result.mtz
# still map and input.pdb will have different origins

import sys

def make_fake_map(pdb_file_name):
     import iotbx.pdb
     import libtbx
     import mmtbx.utils, os
     from mmtbx import monomer_library
     
     resolution = 14.2
     
     mon_lib_srv = monomer_library.server.server()
     ener_lib = monomer_library.server.ener_lib()
       
     processed_pdb_file = monomer_library.pdb_interpretation.process(
          mon_lib_srv               = mon_lib_srv,
          ener_lib                  = ener_lib,
          file_name                 = pdb_file_name,
          raw_records               = None,
          force_symmetry            = True)
     
     pdb_hierarchy = processed_pdb_file.all_chain_proxies.pdb_hierarchy
     
     xray_structure = iotbx.pdb.input(file_name=pdb_file_name).xray_structure_simple()
     #f_calc = xray_structure.structure_factors(d_min=3.4).f_calc()
     f_calc = xray_structure.structure_factors(d_min=resolution).f_calc()
     resolution_factor=0.2
     fft_map = f_calc.fft_map(resolution_factor=resolution_factor)
     
     fft_map.apply_sigma_scaling()
     map_data = fft_map.real_map_unpadded()
     
     '''
     #original
     selection_string = "chain 2 and resseq 1:16"
     selection_radius = 5
     box_offset = 2
     '''
     
     # Doonam's choice for now
     selection_string = "chain A and resseq 1:636"
     selection_radius = 5
     box_offset = 20 #2
     
     selection = pdb_hierarchy.atom_selection_cache().selection(
         string = selection_string)
     selection = xray_structure.selection_within(
         radius    = selection_radius,
         selection = selection)
       
     r = mmtbx.utils.extract_box_around_model_and_map(
         xray_structure = xray_structure,
         map_data       = map_data,
         selection      = selection,
         box_cushion    = box_offset)
     
     output_file_name = pdb_file_name[:-4] + ".mtz"
     mc = r.map_coefficients(d_min=resolution, resolution_factor=resolution_factor,
         file_name=output_file_name)
     
     print "done, we will do phenix.mtz2map result.mtz"
     
     cmd = "phenix.mtz2map " + output_file_name
     libtbx.easy_run.call(cmd)
     
     cmd = "rm " + output_file_name
     libtbx.easy_run.call(cmd)
######### end of make_fake_map function


if (__name__ == "__main__") :
     args=sys.argv[1:]
     if len(args) < 1:
       print "input format: phenix.python make_fake_map_for_1_pdb.py pdb_file_name \n"
       print "example usage: phenix.python make_fake_map_for_1_pdb.py best1_fixed_for_phenixr.pdb \n"
       exit(1)
     pdb_file_name = args[0]
     make_fake_map(pdb_file_name)
     