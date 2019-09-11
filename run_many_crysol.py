import glob, os

path_dot_dat = "/Users/doonam/Dropbox/research/target/bvht/SAXS/latest_in_dropbox_keep/full_length/12mM_Mg/use_weak_SAXS_signal/dot_dat"
#path_dot_dat = "/Users/doonam/Dropbox/research/target/bvht/SAXS/latest_in_dropbox_keep/full_length/12mM_Mg/use_weak_SAXS_signal/pair-wise_distance_distribution"

for x in range(1, 31):
  
  atomic_model_name = "best" + str(x) + ".pdb"
  #cmd = "crysol -cst " + atomic_model_name + " " + path_dot_dat + "/weak_saxs_signal_full_bvht_12mM_Mg_merge_003.dat"
  cmd = "crysol " + atomic_model_name + " " + path_dot_dat + "/weak_saxs_signal_full_bvht_12mM_Mg_merge_003.dat"
  #cmd = "crysol " + atomic_model_name + " " + path_dot_dat + "/full_12mM_Mg_merge_003b.out"
  print cmd
  os.system(cmd)