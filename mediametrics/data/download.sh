#!/bin/bash

for i in {07..10}; do
    for j in {01..31}; do
        axel -an10 "http://mediametrics.ru/data/archive/hour/ru-2016-${i}-${j}.zip"
    done
done