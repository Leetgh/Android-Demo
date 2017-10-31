import os,  sys

os.system("for file in *.apk; do adb install $file; done");
