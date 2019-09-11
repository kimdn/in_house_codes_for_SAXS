import glob, os

map_path = "/Users/doonam/Dropbox/research/target/bvht/SAXS/latest_in_dropbox_keep/full_length/12mM_Mg/use_weak_SAXS_signal/damaver/map/"

for x in range(1, 31):
  
  atomic_model_name = "best" + str(x) + "_fixed_for_phenixr.pdb"
  output_name = "best" + str(x) + "_fixed_for_phenixr_docked_in_map.pdb"
  cmd = "phenix.dock_in_map " + map_path + "old_saxs_damfilt_12mM_Mg_14p2A_reso_by_mtriage.ccp4 " + atomic_model_name + \
        " resolution=14.2 nproc=3 pdb_out=" + output_name
  print cmd
  os.system(cmd)