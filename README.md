# Script to automate audio modding for Tekken 8

## Features:
 - Will rename the WEMs from wem IDs to the filenames of the txtp files, when you set do_extract=True
 - Will auto-generate a mod based on your modded wem files (with names corresponding to the txtp filenames), when you set set do_mod=True

## Usage:

Assuming you stick this Python script in some directory my_dir, create the following 3 directories under it:
  - txtp
  - Media
  - modded_wems

Before running the script:
- Stick your txtp files (from https://mega.nz/folder/BylDlBSZ#OuaBM0uP-4mGvOgm6Lynkg ) in my_dir/txtp
- Extract ALL the wems from Fmodel and stick ALL the wems in my_dir/Media directory
- If you want to make a mod, set do_mod=True and stick your modded wem files in my_dir/modded_wems directory, with names EXACTLY matching the txtp filenames (not the wem IDs)
- Set mod_filename to the mod name you want, in the form z_your_mod_name_P
- To rename the WEMs from wem IDs to the filenames of the txtp files, set do_extract=True
- To auto-generate a mod based on your modded wem files, set do_mod=True

Run the script, which will:
- rename the wems from Fmodel and copy them to the my_dir/renamed_wem directory
- create a mod with your modded wems and place the mod in the my_dir/packed directory.
