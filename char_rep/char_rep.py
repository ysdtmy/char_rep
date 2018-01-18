import os
import re
import sys

def char_rep(file,outputfile,replace_wd,new_wd):

    if os.path.exists(outputfile):
        os.remove(outputfile)

    print('INPUT File -->' + file)
    print('OUTPUT File -->' + outputfile)
    print('Serach Word -->' + replace_wd)
    print('Replace FILE -->' + new_wd + '\n')

    print('---------Search word----------' )


    try:
        f = open(file,'r')

    except FileNotFoundError:
        print("File not found...")
        return

    lines = f.readlines()

    rep_wd_cnt = 0

    for line in lines:
        wd_cnt = re.findall(replace_wd, line)
        rep_wd_cnt += len(wd_cnt)

        rep_line = line.replace(replace_wd, new_wd)

        if len(wd_cnt) > 0:
            print(line)
            print('----> ' + rep_line)

        with open(outputfile,'a') as f:
            f.write(rep_line)


    f.close()

    print('-----------------------------')
    if rep_wd_cnt == 0:
        print("Search word not found")


    print("Total Replace words")
    print(rep_wd_cnt)




if __name__ == "__main__":

    char_rep("./SAMPLE.hive"
             ,"./SAMPLE_REP.hive"
             ,"sigma_impl"
             ,"${hivevar:DB}")