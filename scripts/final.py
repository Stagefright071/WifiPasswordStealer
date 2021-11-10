import zipfile
import subprocess
import os
import sys

bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
path_to_zip = os.path.abspath(os.path.join(bundle_dir, 'zips/notazip.zip'))

with zipfile.ZipFile(path_to_zip, 'r') as zip_ref:
    zip_ref.extractall("notazip")
    subprocess.call("notazip/runthis.exe")