import glob, os

for x in range(1, 31):
  
  atomic_model_name = "best" + str(x) + "_fixed_for_phenix.pdb"
  cmd = "supcomb 12mM_Mg_damfilt_12mM_Mg.pdb before_supcomb/" + atomic_model_name
  print cmd
  os.system(cmd)