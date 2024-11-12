import os
import shutil

folder_to_organise = "C:/Users/Fola/Downloads"

#create a list of all the files within the folder we want to organise 
all_files = os.listdir(folder_to_organise)

#Created folder names to sort out files
folder_names = {
   'Documents' : ['pdf', 'html', 'txt', 'docx', 'xlsx' ],
   'Images' : ['png', 'jpeg', 'gif', 'jpg'],
   'Videos' : ['mp4', 'mov', 'avi'],
   'Archives' : ['zip', 'rar', 'tar'],
   'Other': []
}

#Function to organise files

def organise_files(directory):
   #Create folders that will store our files
   for folder in folder_names.keys():
      folder_path = os.path.join(directory, folder)
      if not os.path.exists(folder_path):
         os.makedirs(folder_path)

   #Check if the folder exists
   
      #If it doesn't exist:
         #display an error and stop the program
      if not os.path.isdir(directory):
         print("Error: Folder does not exist")
         exit()
      #If it exists:
      else:
        
         #If it has no files:
            #display a message and stop 
         if len(os.listdir(directory)) == 0:
            print("No files found in the directory")
            exit()
         #If it has files
         else:
            

         
            #Loop through our files 
            for file in os.listdir(directory):
               #For each file:
                  #Check if its extension matches any values in our folder names values
                     #If it matches:
                        #Check if a folder for that category exists 
                           #if folder exists:
                              #Move File into that folder
                           #Else if it doesn't
                              #Create that folder 
                              #Move the file into that folder 
                  #If the the file does not match any extensions: 
                     #Print a message that skips the file 
      #Log the results
      #Print "File organisation completed"