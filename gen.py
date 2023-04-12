import os
import glob

# Get the current working directory
current_dir = os.getcwd()

# Define the file pattern to match
file_pattern = "emoji-*.png"

# Use glob to find all PNG files in the current directory and its subdirectories
png_files = glob.glob(os.path.join(current_dir, "**", file_pattern), recursive=True)

# Print the total number of PNG files found
print(f"All the {len(png_files)} icons below, shown at 24pt size:")

# Group the PNG files by subfolder
png_files_by_subfolder = {}
for png_file in png_files:
    subfolder = os.path.dirname(png_file)
    if subfolder not in png_files_by_subfolder:
        png_files_by_subfolder[subfolder] = []
    png_files_by_subfolder[subfolder].append(png_file)

# Sort the list of subfolders by path and make the paths relative to the current folder
subfolders = sorted([os.path.relpath(subfolder, current_dir).replace(os.path.sep, '/') for subfolder in png_files_by_subfolder.keys()])

# Print the HTML image tags for each subfolder
for subfolder in subfolders:
    print()
    print(f"### {subfolder}")
    print()
    for png_file in png_files_by_subfolder[os.path.join(current_dir, subfolder).replace('/', os.path.sep)]:
        emoji_name = os.path.splitext(os.path.basename(png_file))[0].split('-')[1]
        html_tag = f'<img src="{os.path.relpath(png_file, current_dir).replace(os.path.sep, "/")}" alt="{emoji_name}" title="{emoji_name}" width="24"></img>'
        print(html_tag)
