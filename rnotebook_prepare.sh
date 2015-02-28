#!/bin/sh

# Install R and some required apt packages
sudo apt-get update --fix-missing
sudo apt-get install r-base-core r-recommended r-cran-xml libcairo2-dev libcurl4-openssl-dev
 
# Now download and execute the script to install and run rNotebook
cd /tmp
wget https://gist.github.com/mjbommar/7186297/raw/rnotebook_install_run.R
sudo R --vanilla < rnotebook_install_run.R
