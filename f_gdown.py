import gdown
import os

# Define Google Drive links for the files
file_1_url = 'https://drive.google.com/uc?id=1gjn785gREju8bK5VbJhwJZK-oezQurMa'
file_2_url = 'https://drive.google.com/uc?id=1JPQmbfl9nGDDUqKoHtPGPOyJyDhat9pb'

# Define the local path where you want to save the files
file_1_path = 'lib/python3.12/site-packages/tensorflow/libtensorflow_cc.so.2'
file_2_path = 'lib/python3.12/site-packages/tensorflow/libtensorflow_framework.so.2'

# Ensure the directory exists
os.makedirs(os.path.dirname(file_1_path), exist_ok=True)

# Download the files
gdown.download(file_1_url, file_1_path, quiet=False)
gdown.download(file_2_url, file_2_path, quiet=False)

print(f"Files downloaded to {file_1_path} and {file_2_path}")
