
import os
cwd =os.getcwd()
print("current path = ", cwd)
def find_filse(suffix,path):

    if path ==None:
        return None
    total_suffix_files=set()
    total_files=set()
    if os.path.isdir(path):
            
            for i in  os.listdir(path):
                total_files.add(i)
                print(total_files)

                for x in total_files:
                    if x.endswith(suffix):
                        total_suffix_files.add(x)
                        print(total_suffix_files)

            # return total_suffix_files

            return total_files
    else:
         print("Empty folder")

print(find_filse(".c","path")) 

print(find_filse(".h","path"))











#  print(find_filse(".c","path")) 

#  print(find_filse(".h","path"))


##################################################################

# import os

# current_dir = os.getcwd()


# def find_files(suffix, current_dir):
#     files = os.listdir(current_dir)
#     flag = False
#     for file in files:
#         if os.path.isdir(file):
#             find_files(suffix, os.path.join(current_dir, file))
#         if (current_dir + file).endswith(suffix):
#             print(current_dir + "/" + file)

#     return


# print("---------test case 1-------------")

# print(find_files(".c", current_dir))

# print("---------test case 2-------------")

# print(find_files(".h", current_dir))

# print("---------test case 3-------------")

# print(find_files(".xyz", current_dir


###################################################


# def find_files(suffix,cwd):
    
#     flag=False
#     for x in os.listdir(cwd):
#         while os.path.isdir(x):
#             temp_path=os.path.join(cwd,x)
#             find_files(suffix,temp_path)
        
#         if (cwd+x).endswith(suffix):
#             print(cwd+"/"+x)
#     return 

# print("######################")

# print(find_files(".c",cwd)) 

# print("###############")
# print(find_files(".h",cwd))
