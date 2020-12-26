import os
import pandas as pd

#dirpath = '{Source}/{Directory}'
#output = '{Destination}/{Directory}/{Output_Filename}'
dirpath = '/home/robertv/Downloads/nsfw_data_source_urls-master/Full source/'
output = '/home/robertv/Downloads/nsfw_data_source_urls-master/ALL_C.csv'
csvout_lst = []
files = [os.path.join(dirpath, fname) for fname in os.listdir(dirpath)]

for filename in sorted(files):
    print(filename)
    data = pd.read_csv(filename, sep=',', header=None, error_bad_lines=False)
    data.drop_duplicates()
    csvout_lst.append(data)

pd.concat(csvout_lst).to_csv(output, header=False, index=False)