#  darknet to pytorch libraries: argh-0.26.2 pydispatcher-2.0.5 pyyaml-6.0 tool-0.8.0
# # parameters
# number_classes: 80  # number of classes
# depth_multiple: 1.0  # model depth multiple
# width_multiple: 1.0  # layer channel multiple
#
# # anchors
# anchors:
#   - [10,13, 16,30, 33,23]  # P3/8
#   - [30,61, 62,45, 59,119]  # P4/16
#   - [116,90, 156,198, 373,326]  # P5/32
#
# # CSPDarknet53-SPP backbone
# backbone:
#   # [from, number, module, args]
#   [[-1, 1, Conv, [32, 3, 1]],  # 0
#    [-1, 1, Conv, [64, 3, 2]],  # 1-P1/2
#    [-1, 1, BottleneckCSP, [64]],
#    [-1, 1, Conv, [64, 1, 1]],
#    [-1, 1, Conv, [128, 3, 2]],  # 4-P2/4
#    [-1, 2, BottleneckCSP, [128]],
#    [-1, 1, Conv, [128, 1, 1]],
#    [-1, 1, Conv, [256, 3, 2]],  # 7-P3/8
#    [-1, 8, BottleneckCSP, [256]],
#    [-1, 1, Conv, [256, 1, 1]],
#    [-1, 1, Conv, [512, 3, 2]],  # 10-P4/16
#    [-1, 8, BottleneckCSP, [512]],
#    [-1, 1, Conv, [512, 1, 1]],
#    [-1, 1, Conv, [1024, 3, 2]],  # 13-P5/32
#    [-1, 4, BottleneckCSP, [1024]],
#    [-1, 1, Conv, [1024, 1, 1]],  # 15
#   ]
#
# # YOLOv5 head
# head:
#   [[-1, 1, Conv, [512, 1, 1]],
#    [-1, 1, Conv, [1024, 3, 1]],
#    [-1, 1, Conv, [512, 1, 1]],
#    [-1, 1, SPP, [1024, [5, 9, 13]]],
#    [-1, 1, Conv, [512, 1, 1]],
#    [-1, 1, Conv, [1024, 3, 1]],
#    [-1, 1, Conv, [512, 1, 1]],  # 22
#
#    [-1, 1, Conv, [512, 1, 1]],
#    [-1, 1, nn.Upsample, [None, 2, "nearest"]],
#    [[-1, 12], 1, Concat, [1]],  # concat backbone P4
#    [-1, 3, BottleneckCSP, [512, False]],  # 26
#
#    [-1, 1, Conv, [256, 1, 1]],
#    [-1, 1, nn.Upsample, [None, 2, "nearest"]],
#    [[-1, 9], 1, Concat, [1]],  # concat backbone P3
#    [-1, 3, BottleneckCSP, [256, False]],  # 30
#
#    [-1, 1, Conv, [256, 3, 2]],
#    [[-1, 27], 1, Concat, [1]],  # concat head P4
#    [-1, 3, BottleneckCSP, [512, False]],  # 33
#
#    [-1, 1, Conv, [512, 3, 2]],
#    [[-1, 23], 1, Concat, [1]],  # concat head P5
#    [-1, 3, BottleneckCSP, [1024, False]],  # 36
#
#    [[30, 33, 36], 1, Detect, [number_classes, anchors]],  # Detect(P3, P4, P5)
#   ]



# # parameters
# number_classes: 80  # number of classes
# depth_multiple: 1.0  # model depth multiple
# width_multiple: 1.0  # layer channel multiple
#
# # anchors
# anchors:
#   - [10,14, 23,27, 37,58]  # P4/16
#   - [81,82, 135,169, 344,319]  # P5/32
#
# # CSPDarknet-19 backbone
# backbone:
#   # [from, number, module, args]
#   [[-1, 1, Conv, [32, 3, 2]],  # 0-p1/2
#    [-1, 1, Conv, [64, 3, 2]],  # 1-P2/4
#    [-1, 1, BottleneckCSP, [64]],
#    [-1, 1, Maxpool, [2, 2]],   # 3-P3/8
#    [-1, 1, BottleneckCSP, [128]],
#    [-1, 1, Maxpool, [2, 2]],   # 5-P4/16
#    [-1, 1, BottleneckCSP, [256]],
#    [-1, 1, Maxpool, [2, 2]],   # 7-P5/32
#    [-1, 1, Conv, [512, 3, 1]],
#   ]
#
# # YOLOv3-tiny head
# head:
#   [[-1, 1, Bottleneck, [512, False]],  # 9
#
#    [-1, 1, Conv, [128, 1, 1]],
#    [-1, 1, nn.Upsample, [None, 2, "nearest"]],
#    [[-1, 6], 1, Concat, [1]],  # concat backbone P4
#    [-1, 1, Conv, [256, 1, 1]],  # 13
#
#    [[13, 9], 1, Detect, [number_classes, anchors]],   # Detect(P4, P5)
#   ]


# from tool import darknet2pytorch
# import torch
#
# # load weights from darknet format
# model = darknet2pytorch.Darknet('path/to/cfg/yolov4-416.cfg', inference=True)
# model.load_weights('path/to/weights/yolov4-416.weights')
#
# # save weights to pytorch format
# torch.save(model.state_dict(), 'path/to/save/yolov4-pytorch.pth')
#
# # reload weights from pytorch format
# model_pt = darknet2pytorch.Darknet('path/to/cfg/yolov4-416.cfg', inference=True)
# model_pt.load_state_dict(torch.load('path/to/save/yolov4-pytorch.pth'))





# numpy==1.18.2
# torch==1.4.0
# tensorboardX==2.0
# scikit_image==0.16.2
# matplotlib==2.2.3
# tqdm==4.43.0
# easydict==1.9
# Pillow==7.1.2
# opencv_python
# pycocotools