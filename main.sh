#!/bin/bash
#PBS -l cput=1000:00:00
#PBS -l walltime=1000:00:00

use anaconda3use gcc48
python /user/i/iaraya/CIARP/Wind_speed/main.py $1 $2 $3 $4