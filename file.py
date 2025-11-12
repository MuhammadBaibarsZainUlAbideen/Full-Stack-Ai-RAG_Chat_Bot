from PyPDF2 import PdfReader

async def extracting_pdf_file(upload_file):
    content = await upload_file.read()
    from io import BytesIO
    pdf_reader = PdfReader(BytesIO(content))
    
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text
