from PyPDF2 import PdfReader
import tiktoken



def get_pdf_text(pdf_doc):
    text = ""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text



def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

pdfFileObj = open('files/pdfs/STEP7.V53_FBD_r.pdf', 'rb')
text = get_pdf_text(pdfFileObj)
print("Letters in pdf: ", len(text))
print(text[:11])
print("Tokens in pdf: ", num_tokens_from_string(text, "cl100k_base"))

pdfFileObj.close