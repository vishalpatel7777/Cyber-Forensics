#import the dependency
import pikepdf

#open pdf file with the pikepdf
pdf = pikepdf.Pdf.open('48_laws_of_powers_-_Robert_Greene.pdf')

# Extract the metadata from the pdf
pdf_metadata = pdf.docinfo

#print the metadata
for key,value in pdf_metadata.items():
    print(f'{key} : {value}')

