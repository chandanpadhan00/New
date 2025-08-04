#!/usr/bin/env python3
import os
import xml.etree.ElementTree as ET
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ← EDIT THIS to the full or relative path of your XML file
XML_INPUT = "path/to/your/input.xml"

def xml_to_pdf(xml_path, pdf_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    margin, line_height = 50, 14
    y_pos = height - margin

    def write_element(elem, indent=0):
        nonlocal y_pos
        if y_pos < margin:
            c.showPage()
            y_pos = height - margin

        # opening tag
        c.drawString(margin + indent*20, y_pos, f"<{elem.tag}>")
        y_pos -= line_height

        # text content
        if elem.text and elem.text.strip():
            for line in elem.text.strip().splitlines():
                c.drawString(margin + (indent+1)*20, y_pos, line)
                y_pos -= line_height

        # children
        for child in elem:
            write_element(child, indent+1)

        # closing tag
        if y_pos < margin:
            c.showPage()
            y_pos = height - margin
        c.drawString(margin + indent*20, y_pos, f"</{elem.tag}>")
        y_pos -= line_height

    write_element(root)
    c.save()

def main():
    xml_file = XML_INPUT
    if not os.path.isfile(xml_file):
        print(f"Error: XML file not found → {xml_file}")
        return

    folder   = os.path.dirname(xml_file) or "."
    basename = os.path.splitext(os.path.basename(xml_file))[0]
    pdf_file = os.path.join(folder, basename + ".pdf")

    xml_to_pdf(xml_file, pdf_file)
    print(f"✅ PDF generated at: {pdf_file}")

if __name__ == "__main__":
    main()