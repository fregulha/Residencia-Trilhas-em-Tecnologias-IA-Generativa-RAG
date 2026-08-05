import os

os.environ["TORCH_COMPILE_DISABLE"] = "1"

from pathlib import Path
from docling.document_converter import DocumentConverter

print("Iniciando...")

converter = DocumentConverter()

pdfs = list(Path(".").glob("*.pdf"))

print(f"Foram encontrados {len(pdfs)} PDFs")

for pdf in pdfs:
    print(f"Convertendo: {pdf.name}")

    resultado = converter.convert(str(pdf))

    markdown = resultado.document.export_to_markdown()

    pdf.with_suffix(".md").write_text(markdown, encoding="utf-8")

    print(f"{pdf.name} convertido!")

print("Fim!")