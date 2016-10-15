#!/bin/bash
cd ImageNet_Utils
./downloadutils.py --downloadImages --wnid n04096066
mkdir -p ../road_data/road
mv ./n04096066/url_images/* ../road_data/road/*
cd ..
