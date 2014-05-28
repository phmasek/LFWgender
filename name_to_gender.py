import os
import sys
from django.http import request
from os import rename
import requests
import shutil

__author__ = 'Philip Masek'



def main(argv):
    fileList = []
    fileSize = 0
    folderCount = 0
    rootdir = "lfw"
    maleFolder = "result/male"
    femaleFolder = "result/female"
    count = 0
    tmp = ""

    for root, subFolders, files in os.walk(rootdir):
        folderCount += len(subFolders)
        for file in files:
            f = os.path.join(root,file)
            fileSize = fileSize + os.path.getsize(f)
            fileSplit = file.split("_")
            fileList.append(f)
            count += 1

            if count == 1:
                result = requests.get("http://api.genderize.io?name=%s" % fileSplit[0])
                result = result.json()
                tmp = fileSplit[0]
            elif tmp != fileSplit[0]:
                result = requests.get("http://api.genderize.io?name=%s" % fileSplit[0])
                result = result.json()
                tmp = fileSplit[0]
            else:
                tmp = fileSplit[0]

            try:
                if float(result['probability']) > 0.9:
                    if result['gender'] == 'male':
                        shutil.copyfile(f,"%s/%s" % (maleFolder,file))
                    elif result['gender'] == 'female':
                        shutil.copyfile(f,"%s/%s" % (femaleFolder,file))
            except Exception as e:
                print result['name']

            print count



if __name__ == "__main__":
    main(sys.argv)