#!/bin/bash
cd ImageNet_Utils
./downloadutils.py --downloadImages --wnid n03215508
./downloadutils.py --downloadImages --wnid n02744323
mkdir -p ../road_data/data
mv ./n03215508/url_images/* ../road_data/data/*
mv ./n02744323/url_images/* ../road_data/data/*
cd ..
