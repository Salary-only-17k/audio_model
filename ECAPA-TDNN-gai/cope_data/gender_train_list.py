import tqdm
import pathlib
import os
import random
random.seed(2025)
import argparse

parser = argparse.ArgumentParser(description = "Gender txt")

parser.add_argument('--data_dir', type=str,   default="/home/cheng/Downloads/ECAPA-TDNN-main/data/test_escapa_tdnn/train",     help='数据目录') 
parser.add_argument('--save_txt',  type=str,   default="/home/cheng/Downloads/ECAPA-TDNN-main/data/train_list.txt",      help='保存txt的路径')
args = parser.parse_args()

"""
/home/cheng/Downloads/ECAPA-TDNN-main/data
    OK/20251201/*.wav
    OK/20251201/*.wav
    OK/20251201/*.wav
    OK/20251201/*.wav
    ...
    NG/20251201/*.wav
    NG/20251201/*.wav
    NG/20251201/*.wav
    NG/20251201/*.wav
    ...
"""


def pth1_pth2(pth1:str,pth2:str)->str:
    l1 = pth1.split(os.path.sep)  # 长路径
    l2 = pth2.split(os.path.sep)     # 短路径
    for l in l2:
        l1.remove(l)
    return os.path.join(*l1)

class gender_train_list():
    def __init__(self,dir:str,train_txt:str):
        self.pths_lst = [pth1_pth2(str(pth),dir) for pth in list(pathlib.Path(dir).glob("**/*.wav"))]
        self.train_txt =train_txt
    def loop(self):
        random.shuffle(self.pths_lst)
        with open(self.train_txt,"w") as wf:
            for pth in tqdm.tqdm(self.pths_lst):
                label = pth.split(os.path.sep)
                wf.write(f"{label[0]}  {pth}\n")


if __name__ == "__main__":
    func = gender_train_list(args.data_dir,args.save_txt)
    func.loop()