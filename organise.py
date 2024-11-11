import os
import shutil

folder_to_organise = "C:/Users/Fola/Downloads"

#We create a list of all the files within the folder we want to organise 
all_files = os.listdir(folder_to_organise)

#Created folder names to sort out files
folder_names = {
   'Documents' : ['pdf', 'html', 'txt', 'docx', 'xlsx' ],
   'Images' : ['png', 'jpeg', 'gif', 'jpg'],
   'Videos' : ['mp4', 'mov', 'avi'],
   'Archives' : ['zip', 'rar', 'tar']
}

#Function to organise files
def organise_files(directory):
   for folder in folder_names.keys():
      folder_path = os.path.join(directory, folder)
      if not os.path.exists(folder_path):
         os.makedirs(folder_path)