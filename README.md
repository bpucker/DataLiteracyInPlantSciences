# DataLiteracyInPlantSciences
This repository contains scripts and data sets associated with the ['Data Literacy in Plant Sciences'](https://github.com/bpucker/teaching/tree/master/GE32_DataLiteracyInPlantSciences) course.


## (1) Introduction
### (1.1) Establishing access to de.NBI cloud

### (1.2) Documentation
Please ensure a proper documentation of all analyses. This includes the version of applied tools, the parameters, input files, and output files.

### (1.3) Introduction to Linux
File names should not include spaces or other special characters.
Important commands are:

`cd <FOLDER>` changes the working directory to the specified folder

`mkdir <FOLDER>` creates a new folder in the working directory

`ls` list the content of the working directory

### (1.4) Downloading and transferring files
`scp` this function can be used to transfer files. Please see the [documentation](https://linux.die.net/man/1/scp) for details.

`wget` this function can be used to download files. Please see the [documentation](https://ftp.gnu.org/old-gnu/Manuals/wget-1.8.1/html_mono/wget.html) for details.

`md5sum <FILENAME>` calculates a hash (finger print) for a given file. This hash can be used to check the complete transfer of files.



## (2) Understanding the mysteries of plant pigmentation
Helpful data sets are available here: here: https://lnk.tu-bs.de/pE3yxC.

Here you can find an online tool for co-expression: http://pbb.bot.nat.tu-bs.de/CoExp/

[MAFFT](https://www.ebi.ac.uk/Tools/msa/mafft/) can be used for glogabl alignments.

Tools for phylogenetic tree construction: [FastTree2](http://www.microbesonline.org/fasttree/), [RAxML](https://cme.h-its.org/exelixis/web/software/raxml/).

[iTOL](https://itol.embl.de/) is helpful for the visualization of phylogenetic trees.


## (3) Re-using gene expression data sets

[fastq-dump](https://rnnh.github.io/bioinfo-notebook/docs/fastq-dump.html) of the SRA toolkit can be used to download FASTQ files from the [Sequence Read Archieve](https://www.ncbi.nlm.nih.gov/sra).



## (4) Distribution of Caryophyllales
[GBIF](https://www.gbif.org/) is a valuable source of species distribution data sets. A [tutorial](https://www.r-bloggers.com/2021/03/downloading-and-cleaning-gbif-data-with-r/) explains how to download and clean GBIF data sets. Additional cleaning with [CoordinateCleaner](https://ropensci.github.io/CoordinateCleaner/) is recommended.

Running these cleaning steps requires the installation of several tools:

`sudo apt-get install r-base`

`sudo apt-get install gdebi-core`

`wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-2022.07.0-548-amd64.deb`

`sudo gdebi rstudio-server-2022.07.0-548-amd64.deb`

`sudo apt install liblapack-dev libopenblas-dev`

`sudo apt-get install libcurl4-openssl-dev`

`sudo apt-get install libxml2-dev`

`sudo apt-get install libssl-dev`

`sudo apt-get install libpng-dev`

`sudo apt install libgdal-dev`

`sudo apt-get install -y libudunits2-dev`


Several R packages are required to run these cleaning analyses:

"rgbif", "remotes", "slam", "qlcMatrix", "curl", "crul", "ropensci/scrubr", "openssl", "httr", "maps", "CoordinateCleaner"


## (5) Finding flaws in publications


### (6) Statistical tests

The script statistic_test.py contains functions to run some basic statistic tests.

```
Usage
python3 statistic_test.py --in <FILE>
Mandatory:
--in      STR   Input data file

Optional:
--test    STR   Statistic test
--paired  NONE  Indicates paired samples
```

`--in` or `--input` specifies the input data file that contains the values for statistical tests. The first row must contain the sample names. All following rows are considered data rows. Two columns with one value each are expected. If the samples are unpaired and one sample is larger than the other, the larger sample must be in the first column.

`--test` specifies the statistical test to run.

`--paired` indicates that the samples are paired. This will trigger paired tests if available for the selection.


## References
