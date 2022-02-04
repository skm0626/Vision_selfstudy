import cv2
from tqdm import tqdm

cap = cv2.VideoCapture('/data/test/jml_data/P2610247_2min_final.mp4')
fps = cap.get(cv2.CAP_PROP_FPS) #프레임 초당 프레임 수

width, height = cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #프레임 폭, 프레임 높이

re_width, re_height = 648, 1152 #원본 이미지 720,1280 
pad_top = 64 # 위 아래로 64씩 줄이면 648 + (64*2) = 720
pad_left = 36 # 양 옆으로 36씩이면 1152 + (36*2) = 1280

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # 총 프레임 개수

out = cv2.VideoWriter('result_pad.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (round(width), round(height)))
pbar = tqdm(range(length), disable=False)
i = 1
while True:
    ret, frame = cap.read()
    if not ret:
        break
    resize_img = cv2.resize(frame, (re_width, re_height),  cv2.INTER_LINEAR) 
    ref_img = cv2.copyMakeBorder(resize_img, pad_top, pad_top, pad_left, pad_left, cv2.BORDER_REPLICATE)
    out.write(ref_img)
    i+=1
    pbar.update()
pbar.close()
cap.release()
out.release()
