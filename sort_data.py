import os
import sys

# Sorts data into hotdog and not-hotdog classes

hotdog_prefixes = ["frankfurter", "chili-dog", "hotdog"]

dirpath = sys.argv[1]
hotdogpath = os.path.join(dirpath, "hotdog")
nothotdogpath = os.path.join(dirpath, "not-hotdog")
if not os.path.exists(hotdogpath):
    os.makedirs(hotdogpath)
if not os.path.exists(nothotdogpath):
    os.makedirs(nothotdogpath)

for file in os.listdir(dirpath):
    filepath = os.path.join(dirpath, file)
    if os.path.isdir(filepath):
        continue  # Skip directories

    filename = os.fsdecode(file)
    if any(filename.lower().startswith(prefix) for prefix in hotdog_prefixes):
        os.rename(filepath, os.path.join(hotdogpath, filename))
    else:
        os.rename(filepath, os.path.join(nothotdogpath, filename))
