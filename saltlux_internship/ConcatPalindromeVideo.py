import cv2
import os
import argparse
from tqdm import tqdm

def mkPelindrome(in_fn):
    print("-------Current File : ", in_fn)
    cap = cv2.VideoCapture(os.path.join(input_path,in_fn))

    frame_list = []

    while True:
        check , vid = cap.read()
        if check is True:
            #cv2.imwrite()
            frame_list.append(vid)
        else:
            break

    reversed_frame_list = list(reversed(frame_list))    
    print("frame list len : ",len(frame_list))     

    print("reversed frame list len : ",len(reversed_frame_list))     
    
    out_list = frame_list + reversed_frame_list 
    print("out list len : ",len(out_list))     
    cap.release()
    height, width, layers = out_list[0].shape
    size = (width,height)
    print("frame size : ",size)
    out = cv2.VideoWriter(os.path.join(output_path,in_fn.replace(".mp4","_concat.mp4")),cv2.VideoWriter_fourcc(*'mp4v'), 30.0, size)
    for i in tqdm(range(len(out_list))):
        out.write(out_list[i])
    out.release()
    

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--filename', type=str , help='if you want to use every file than - all  or  if you want to use specific file than - filename.mp4')

args = parser.parse_args()
print(args.filename)
inputs = []


input_path = os.path.join(os.getcwd(), "input")
if args.filename == 'all':
    inputs = os.listdir(input_path)
else:
    inputs.append(args.filename)
output_path = os.path.join(os.getcwd(), "output")

print(inputs)

for inpt in inputs:
    mkPelindrome(inpt)

print("done")

