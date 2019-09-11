import glob, os
for pdb in glob.glob("*.pdb"):
    sit_file_name = pdb[:-4] + "_20A.sit"
    run_pdb2vol = "pdb2vol " + pdb + " " + sit_file_name + " < /home/doonam/bin/pdb2vol/pdb2vol_options_20A"
    os.system(run_pdb2vol)

    run_this = "echo 1 >> input_parameter" # to auto mrc
    os.system(run_this)

    mrc_file_name = sit_file_name[:-4] + ".mrc"
    run_map2map = "map2map " + sit_file_name + " " + mrc_file_name + " < input_parameter"
    os.system(run_map2map)

    os.remove("input_parameter")
