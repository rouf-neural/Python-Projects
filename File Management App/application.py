import os 

def create_file(filename):
     try:
          with open(filename, "x") as f:
               print(f"file name {filename}: CREATED SUCCESSFULLY!")
     except FileExistsError:
          print(f'file name {filename} ALREADY EXISTS!')

     except Exception as E:
          print("AN ERROR OCCURRED!")

def view_all_files():
     files = os.listdir()
     if not files:
          print("NO FILE FOUND!")
     else:
          print("FILES IN DIRECTORY!")
          for file in files:
               print(file)

def delete_file(filename):
     try:
          os.remove(filename)
          print(f'{filename} HAS BEEN DELETED SUCCESSFULL!')
     except FileNotFoundError:
          print("FILE NOT FOUND")

     except Exception as e:
          print("AN ERROR OCCURRED")

def read_file(filename):
     try:
          with open('demo.txt', "r") as f:
               content = f.read()
               print(f"CONTENT OF '{filename}' : \n{content}")

     except FileNotFoundError:
        print(f"{filename} DOESNT EXIST")

     except Exception as e:
        print('AN ERROR OCCURRED')

def edit_file(filename):
     try:
          with open ('demo.txt', "a") as f:
               content = input("ENTER DATA TO ADD = ")
               f.write(content + "|\n")
               print('CONTENT ADDED TO {filename} SUCCESSFULLY!')

     except FileNotFoundError:
           print(f"{filename} DOESNT EXIST!")

     except Exception as e:
          print("AN ERROR OCCURRED!")

def main ():
     while True:
          print("FILE MANAGEMENT APP")
          print('1: Create file')
          print('2: View all file')
          print('3: Delete file')
          print('4: Read file')
          print('5: Edit file')
          print('6: Exit file')

          choice = input ('Enter your choice(1-6) = ')

          if choice == '1':
               filename = input("Enter your file-name to create = ")
               create_file(filename)

          elif choice == '2':
               view_all_files()

          elif choice == '3':
               filename = input("Enter the file you want to delete")
               delete_file(filename)

          elif choice == '4':
               filename =  input("Enter file name to read")
               read_file(filename)

          elif choice == '5':
               filename = input ("Enter your file to edit")
               edit_file(filename)

          elif choice == '6':
               print("clossing the app")
               break

          else:
               print('invalid choice')

if __name__ == "__main__":
     main()


