import os


from PyPDF2 import PdfMerger


def merge_pdfs(folder_path,Output_path):
    merger=PdfMerger()

    pdf_files=[file for file in os.listdir(folder_path) if file.endswith('.pdf')]
    pdf_files.sort()

    for pdf_file in pdf_files:
        file_path=os.path.join(folder_path,pdf_file)

        merger.append(file_path)

    merger.write(Output_path)
    merger.close()


folder_path='D:\\Title_Files\\Processed\\Order No 1139295'
Output_path='D:\\Title_Files\\Processed\\Order No 1139295\\OP.pdf'
merge_pdfs(folder_path,Output_path)
