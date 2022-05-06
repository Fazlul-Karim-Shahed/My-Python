import os, time, datetime

currentFolderPath = os.getcwd()
# currentFilePath = os.path.realpath(__file__)
files = os.listdir(currentFolderPath)
print("Before", files)

files.sort(key=os.path.getctime)
print("After", files)

for item in files:
    print(item)
    path = currentFolderPath + "\\%s"%item
    c_time = os.path.getctime(path)
    created_time = time.ctime(c_time)
    print("Created time: ", created_time, end="           ")

    m_time = os.path.getmtime(path)
    modified_time = time.ctime(m_time)
    print("Modified time: ",modified_time)
    print("=" * 100)
