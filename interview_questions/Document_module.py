import docx
wordDoc = docx.Document('<path to docx file>')


for table in wordDoc.tables:
    for row in table.rows:
        for cell in row.cells:
            print(cell.text)