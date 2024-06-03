from roi_detect import main as roi_detect
from reading_detect import main as reading_detect
from ref_detect import main as ref_detect
import os 
import json
def main():
    url=roi_detect()
    reading=reading_detect()
    ref_number=ref_detect()
    head,filename=os.path.split(url)
    # print('url:',url)
    # print('reading:',reading)
    # print('ref number:',ref_number) 
    output={"url":url,"Meter reading":reading,"BarCode Number":ref_number}
    
    with open(head+'\\'+filename[:-3]+'json', 'w') as f:
        json.dump(output, f)
    return output
if __name__ == "__main__":
    # opt = parse_opt()
    a=main()
    print(a)
    