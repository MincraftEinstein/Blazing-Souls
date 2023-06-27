import os
import shutil

cwd = os.getcwd()
output_dir = cwd + '/build'
version = input("Version: ")
minecraft_version = input("Minecraft Version: ")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_file = output_dir + '-'.join(['/Blazing-Souls', minecraft_version, version])

shutil.make_archive(output_file, 'zip', cwd + '/src')

if os.path.exists(output_file + '.zip'):
    print("BUILD SUCCESSFUL")
else:
    print("BUILD FAILED")
