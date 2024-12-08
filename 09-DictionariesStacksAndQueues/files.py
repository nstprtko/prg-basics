import queue

# creates a queue of files to print
files_to_print = queue.Queue()

while True:
   print('1. Add file to print')
   print('2. Print file')
   print('0. Quit')
   menu = input('Select an option: ')
   print()
   
   if menu == '1':
    file_name = input('Enter file name to print: ')
      # add new file to the end of the queue 
    files_to_print.put(file_name)
    print(f'{file_name} is added to the queue')

   elif menu == 2:
      if not files_to_print.empty():
        file_to_print = files_to_print.get()
        print(f'File {file_to_print} is currently being printed. Please wait!')
      else:
         print('No files')

   elif menu == '0':
      break