import os
import shutil
import time
from datetime import datetime

downloads_folder = os.path.expanduser('~/Downloads')

log_file_path = os.path.expanduser('~/clean_downloads_log.txt')

# Define the age threshold for deletion
age_threshold = 30 #days
now = time.time()

def log_deletion(file_path):
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Deleted: {file_path}\n")
        
def clean_downloads_folder(folder, age_threshold_days):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        
        # Check if file or directory
        if os.path.isfile(file_path) or os.path.isdir(file_path):
            file_age = os.stat(file_path).st_mtime
            
            # Check file age
            if (now - file_age) > (age_threshold_days * 86400): 
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print(f"Deleted file: {file_path}")
                        log_deletion(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print(f"Deleted directory: {file_path}")
                        log_deletion(file_path)
                except Exception as e: 
                    print(f"Failed to delete {file_path}: {e}")
                    
clean_downloads_folder(downloads_folder, age_threshold)