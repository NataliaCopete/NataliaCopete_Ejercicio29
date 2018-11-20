!/bin/bash
#PBS -l nodes=2:intel:ppn=6, mem=64gb
#PBS -l walltime=00:15:00
#PBS -M n.copete@uniandes.edu.co
#PBS -m abe
#PBS -N ncpexo29
#PBS -j oe

module load anaconda/python3
cd $PBS_O_WORKDIR
c++ -o burgers_x burgers.c
./burgers_x>advecc.txt
python graf_ad.py

