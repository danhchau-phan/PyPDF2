import sys
sys.path.append('../../PyPDF2')
# print(sys.path)
from PyPDF2.pdf import PdfFileReader as reader

def extract(filename):
    fd = open(filename, 'rb')
    myreader = reader(fd)
    page0 = myreader.getPage(0)

    print(page0.extractRawText())

def main():
    script, filename = sys.argv
    extract(filename)

if __name__ == '__main__':
    main()