import os


directory = '/Users/fola/Documents'


folders = {
   "Images" : [".jpg", ".png", ".gif", ".svg", ".heif"],
   "Documents" : [".txt", ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".csv"],
   "Video" : [".mp4", ".mov", ".avi"],
   "Audio" : [".mp3", ".wav"],
   "Spreadsheets" : [".xls", ".xlsx", ".csv"],
   "Code" : [".js", ".html", ".py", ".css", ".java"],
   "Archives": [".zip", ".rar"]
}


if not os.path.exists(directory):
   print ("This path does not exist")

else:
   if os.path.isdir(directory):
      print("Directory found. Proceeding to list files ")
      files = os.listdir(directory)

      if not files == 0 :
         print("Directory is empty!")
      else:
            
         #Creating folders
         for folder in folders: 
            folder_path = os.path.join('/Users/fola/Documents', folder)
            if not os.path.exists(folder_path):
               os.mkdir(folder_path)

         for file in files:
            root, extension = os.path.splitext(file)
            extension.lower()

            for folder, format_list in folders.items() : 
               for format in format_list:
                  if extension == format:
                     if os.path.exists(directory + '/folder'):






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