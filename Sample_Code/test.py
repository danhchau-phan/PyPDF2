import sys
sys.path.append('../../PyPDF2')
# print(sys.path)
from PyPDF2.pdf import PdfFileExtractor as extractor
import os

def extract(filename):
    fd = open(filename, 'rb')
    # print(fd.read())
    myreader = extractor(fd)

    # print(fd.writable())
    # print(type(fd))
    # fd.close()
    
    # fd1 = open(filename, 'wb')
    # print(fd1.read())
    # fd1.close()

    # fd2 = os.open(filename, os.O_RDWR)
    # print(type(fd2))
    # print(fd2)
    # print(os.read(fd2,1000000))

def main():
    script, filename = sys.argv
    extract(filename)

if __name__ == '__main__':
    main()