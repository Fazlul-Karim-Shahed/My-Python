
import os, time

def fileInfo(path):
    
    import os, time
    filepath = path
    
    fileName = os.path.basename(filepath)
    createdTime = os.path.getctime(filepath)
    modifiedTime = os.path.getmtime(filepath)
    accessTime = os.path.getatime(filepath)
    
    print("File name: ", fileName)
    print("File path: ", filepath)
    print("Access time: ",accessTime)
    print("Created time: ", createdTime)
    print("Modified time: ", modifiedTime)
    

fileInfo(__file__)

    