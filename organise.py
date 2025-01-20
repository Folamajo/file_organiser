import os
import shutil


directory = '/Users/fola/Desktop'


folders = {
   "Images" : [".jpg", ".png", ".gif", ".svg", ".heif"],
   "Documents" : [".txt", ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".csv"],
   "Video" : [".mp4", ".mov", ".avi"],
   "Audio" : [".mp3", ".wav"],
   "Spreadsheets" : [".xls", ".xlsx", ".csv"],
   "Code" : [".js", ".html", ".py", ".css", ".java"],
   "Archives": [".zip", ".rar"]
}

#Check to see if the directory doesn't exist before 
if not os.path.exists(directory):
   print ("This path does not exist")

else:
   #If it is a directory list the files 
   if os.path.isdir(directory):
      print("Directory found. Proceeding to list files ")
      files = os.listdir(directory)

      #If there are no files to sort in the directory 
      if not files :
         print("Directory is empty!")
      else:
         #If there are files to sort in the directory. 
         #We create folders 
         for folder in folders: 
            folder_path = os.path.join(directory, folder)
            if not os.path.exists(folder_path):
               os.mkdir(folder_path)

         #Check the files in our directory
         #We split the text and filename wwe get the filename and we get the extension 
         for file in files:
            name, extension = os.path.splitext(file)
            extension.lower()

            #We get the key-value pair from the folders dictionary
            #the keys are stored in folder, and the list of formats are stored in format_list
            for folder, format_list in folders.items() : 
               for format in format_list:
                  if extension.lower() == format:
                     destination_folder = os.path.join(directory, folder)
                     if os.path.exists(destination_folder):
                        shutil.move(os.path.join(directory, file), destination_folder)







# checks if path exists 
# if os.path.exists(directory):
#    print("this path exists")
#    print(os.listdir(directory))
# else:
#    print("this path does not exist")

# os.listdir(directory)

# folders = {
#    "Images", "Documents", "Video", "Audio", "Spreadsheets", "Code", "Archives", "Uncategorised"
# }