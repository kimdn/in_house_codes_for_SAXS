# author: Doonam


import glob, os, sys

def convert_main(input_pdb_file_name):

  output_pdb_file_name = convert (input_pdb_file_name) 
  
  final_output_pdb_file_name = input_pdb_file_name[:-4] + "_bead.pdb"
  cmd = "mv " + output_pdb_file_name + " " + final_output_pdb_file_name
  os.system(cmd)
  
  return final_output_pdb_file_name
##################################### end of clean_main function


def deal_OC1(atom, new_line):
  if atom == "OC1":
    new_line = new_line[:13] + "OXT" + new_line[16:]
  return new_line 
##################################### end of def deal_OC1(atom)


def convert(input_pdb_file_name):
  f_in = open(input_pdb_file_name)
  output_pdb_file_name = input_pdb_file_name[:-4] + "_converted.pdb"
  f_out = open(output_pdb_file_name, 'wt')
  bead_num = 0 
  for line in f_in:
    ATOM = line[:4]
    if (ATOM != "ATOM") : 
      f_out.write(line)
    else:
      bead_num = bead_num + 1
      new_line = ''
      if bead_num < 10:
        new_line = line[:23] + "  " + str(bead_num) + line[26:53] + "  6.00  0.000" + "\n"
      elif bead_num < 100:
        new_line = line[:23] + " " + str(bead_num) + line[26:53] + "  6.00  0.000" + "\n"
      else: # elif bead_num < 1000:
        new_line = line[:23] + str(bead_num) + line[26:53] + "  6.00  0.000" + "\n"  
      f_out.write(new_line)
      
  f_in.close()
  f_out.close()
  #cmd = "rm " + input_pdb_file_name
  #os.system(cmd)
  return output_pdb_file_name
##################################### end of clean function

if (__name__ == "__main__") :
  args=sys.argv[1:]
  if (len(args) >= 1):
    input_pdb_file_name = args[0] # pdb input file
    if (input_pdb_file_name[-4:] != ".pdb"):
      print "Entered input_pdb_file is not in pdb format."
      exit(1)
  else:
    print "Please provide a pdb file."
    exit(1)
  
  convert_main(input_pdb_file_name)