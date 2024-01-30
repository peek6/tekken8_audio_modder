#  Script to automate audio modding for Tekken 8
#  Author: peek6

# Usage:

#  To extract audio, set do_extract=True
#  To auto-generate a mod, set do_mod=True

#  Set mod_filename to the mod name you want, in the form z_your_mod_name_P

# Assuming you stick this Python script in some directory my_dir, create the following 3 directories under it:
  #  my_dir/txtp
  #  my_dir/Media
  #  my_dir/modded_wems

# Stick your txtp files (from https://mega.nz/folder/BylDlBSZ#OuaBM0uP-4mGvOgm6Lynkg )  in my_dir/txtp
# Extract ALL the wems from Fmodel and stick ALL the wems in my_dir/Media directory
# If you want to make a mod, set do_mod=True and stick your modded wem files in my_dir/modded_wems directory, with names EXACTLY matching the txtp filenames (not the wem IDs)

# Run the script, which will:
#   - rename the wems from Fmodel and copy them to the my_dir/renamed_wem directory
#   - create a mod with your modded wems and place the mod in the my_dir/packed directory.



import os
import shutil
from pathlib import Path

do_extract = True
do_mod = True

mod_filename = "z_mod_P"  # you can change this name to whatever you want

# You need to populate these:
txtp_dir = "txtp"  # stick the txtp files here
fmodel_wem_dir = "Media"  # stick ALL the wems from Fmodel in the "Media" directory
modded_wems_dir = "modded_wems"  # stick your modded wem files in this directory, with names EXACTLY matching the txtp filenames (not the wem IDs)

# And the script will populate these for you
renamed_wem_dir = "renamed_wem"  # renamed (original) wems will be populated here
output_pak_dir = "packed"  # your packed mod will end up here

output_mod_dir_top = mod_filename
full_output_mod_dir = output_mod_dir_top + r'\Polaris\Content\WwiseAudio\Media'

Path(renamed_wem_dir).mkdir(parents=True, exist_ok=True)
Path(modded_wems_dir).mkdir(parents=True, exist_ok=True)
Path(output_pak_dir).mkdir(parents=True, exist_ok=True)
Path(output_mod_dir_top).mkdir(parents=True, exist_ok=True)
Path(full_output_mod_dir).mkdir(parents=True, exist_ok=True)

p = Path('.')
txt_filenames = []
wem_mappings = {}

# Extract wem IDs from txtp files
for file in p.glob(txtp_dir+'\\**/*.txtp'):

    txt_filename = file.name[:-5]
    f_in = open(file,'r')
    read_buf = f_in.read()

    end_idx = read_buf.find('.wem')

    if(end_idx!=-1):
        wem_id = read_buf[:end_idx].split('/')[-1]
        wem_mappings[txt_filename] = wem_id
        txt_filenames.append(txt_filename)

    f_in.close()

# Rename wem files
if do_extract:
    for key in wem_mappings:
        shutil.copyfile(fmodel_wem_dir + "\\" + wem_mappings[key] + ".wem ", renamed_wem_dir+"\\" + key + ".wem")

# Make the mod
if do_mod:
    for file in p.glob(modded_wems_dir + '\\**/*.wem'):
        wem_filename = file.name[:-4]
        if wem_filename in wem_mappings:
            shutil.copyfile(modded_wems_dir + "\\" + wem_filename + ".wem", full_output_mod_dir + "\\" + wem_mappings[wem_filename] + ".wem")


    filelist = open('filelist.txt', 'w+')
    filelist.write('\"' + output_mod_dir_top + '\*.*\" \"..\..\..\*.*\" ')
    filelist.close()
    os.system('UnrealPak.exe packed\\'+mod_filename+'.pak ' + '-create=filelist.txt --compress')