#!/bin/bash

if [[ $# -lt 1 ]] ;then
	echo "Specified value of the argument is invalid"
	echo "USAGE: $0 (result_file) (n_sample)"
	exit 1
fi

DIR=`pwd`

if [ -d $1 ]; then
	echo "$1 exists."
	CNT=1
	while [ -d "${1}.${CNT}" ]
	do
		(( CNT++))
	done
	mv $1 ${1}.${CNT}
fi

if [[ -n $2 ]] ;then
	N_SAMPLE=$2
fi


mkdir $1
cd $1
SAVE_DIR=`pwd`
cd $DIR

#make venv
python3 -m venv virtualenv
# venv activate
source virtualenv/bin/activate
pip install wheel
pip install pdfkit
pip install selenium
pip install PyPDF2
#pip install chromedriver-binary==96.0.4664.18
pip install webdriver_manager
echo "install package:"
pip freeze

pwd

python3 src/HTML2PDF.py data/mondai.html $SAVE_DIR $N_SAMPLE
python3 src/ConnectPDF.py $SAVE_DIR 
rm -r virtualenv
echo END
