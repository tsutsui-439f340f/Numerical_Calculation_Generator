import PyPDF2
import glob
import sys
import os

WORK_DIR=sys.argv[1]
RESULT_PDF="result.pdf"
merger = PyPDF2.PdfFileMerger()

file_names=glob.glob(os.path.join(WORK_DIR,"*.pdf"))
[print(i) for i in file_names]
for f_name in file_names:
    merger.append(f_name)

merger.write(os.path.join(WORK_DIR,RESULT_PDF))
merger.close()

#個別の.pdfファイルをすべて消す
for f_name in file_names:
    os.remove(f_name)
