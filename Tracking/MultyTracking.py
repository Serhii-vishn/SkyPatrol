import cv2
import sys
from random import randint

video = cv2.VideoCapture('TestVideos/test2.mp4')
if not video.isOpened():
    print('Error while loading the video!')
    sys.exit()
ok, frame = video.read()

bboxes = []
colors = []

while True:
    bbox = cv2.selectROI('MultiTracker', frame)
    bboxes.append(bbox)
    colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))
    print('Press Q to start tracking')
    print('Press any key to select the next object')
    k = cv2.waitKey(0) & 0XFF
    if k == 113: # Q - quit
        break

print(bboxes)
print(colors)

multi_tracker = cv2.legacy.MultiTracker_create()
for bbox in bboxes:
    multi_tracker.add(cv2.legacy.TrackerCSRT_create(), frame, bbox)

while video.isOpened():
    ok, frame = video.read()
    if not ok:
        break

    ok, boxes = multi_tracker.update(frame)

    for i, new_box in enumerate(boxes):
        (x, y, w, h) = [int(v) for v in new_box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), colors[i], 2)

    cv2.imshow('MultiTracker', frame)
    if cv2.waitKey(1) & 0XFF == 27:
        break
