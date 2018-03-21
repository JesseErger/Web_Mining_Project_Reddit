import os

path_to_data_files = (r"C:\Reddit_Data")

for dirName, subdirList, fileList in os.walk(path_to_data_files):
    for fname in fileList:
        fp = open(dirName+"\\"+fname, 'r' , encoding="utf-8")
        files_dir = fname.split(".")[0]+"_"+"partitions"
        try:
          os.mkdir(files_dir)
        except:
          pass #dir already exists
        ct = 0
        file_num = 0
        header = ""
        out_fp = open( (files_dir+"//"+fname.split('.')[0]+"_"+str(file_num))+".csv",'w')
        for line in fp:
          if(ct == 0):
            header = line
            out_fp.write(header)
            ct+=1
          elif(ct%100000 != 0):
            try:
              out_fp.write(line)
            except:
              out_fp.write("UNABLE TO DECODE LINE, NOT IN UTF-8??")
            ct+=1
          else:
            file_num+=1
            out_fp = open((files_dir+"//"+fname.split('.')[0]+"_"+str(file_num))+".csv",'w')
            out_fp.write(header)
            try:
              out_fp.write(line)
            except:
              out_fp.write("UNABLE TO DECODE LINE, NOT IN UTF-8??")
            ct+=1
            print("Creating File in -> " + files_dir+("/"+fname+"_"+str(file_num)).split(".")[0]+".csv")
            