import kagglehub
import shutil
import os

# Download latest version of the dataset
path = kagglehub.dataset_download("rush4ratio/video-game-sales-with-ratings")

# Ensure target directory exists
target_dir = os.path.join(os.path.dirname(os.getcwd()), "data")
os.makedirs(target_dir, exist_ok=True)

# Move each file from the downloaded path to the target directory
for filename in os.listdir(path):
    shutil.move(os.path.join(path, filename), os.path.join(target_dir, filename))

print("Path to dataset files:", target_dir)