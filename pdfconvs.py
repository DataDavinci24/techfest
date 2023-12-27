# # importing required modules
# from PyPDF2 import PdfReader
#
# # creating a pdf reader object
# reader = PdfReader('example.pdf')
#
# # printing number of pages in pdf file
# print(len(reader.pages))
#
# # getting a specific page from the pdf file
# page = reader.pages[0]
#
# # extracting text from page
# text = page.extract_text()
# print(text)
# with open('example.txt','w') as f:
#     f.write(text)
import os
import aspose.words as aw
for i in os.listdir("resumes"):
    doc = aw.Document(f".//resumes/{i}")
    doc.save(f".//text_resumes/{i}.txt")
for i in os.listdir("jds"):
    doc = aw.Document(f".//jds/{i}")
    doc.save(f".//jd_text/{i}.txt")
