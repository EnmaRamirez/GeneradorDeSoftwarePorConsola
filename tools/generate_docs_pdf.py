from pathlib import Path
from fpdf import FPDF
import unicodedata

HEADER_STYLE = {
    1: {'size': 18, 'style': 'B'},
    2: {'size': 14, 'style': 'B'},
    3: {'size': 12, 'style': 'B'},
}


def render_markdown_to_pdf(md_path: Path, pdf_path: Path) -> None:
    lines = md_path.read_text(encoding='utf-8-sig').splitlines()
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font('Arial', size=12)

    for raw_line in lines:
        line = raw_line.rstrip()
        line = unicodedata.normalize('NFKD', line)
        line = line.encode('latin-1', 'ignore').decode('latin-1')
        if not line:
            pdf.ln(6)
            continue

        if line.startswith('# '):
            style = HEADER_STYLE[1]
            pdf.set_font('Arial', style=style['style'], size=style['size'])
            pdf.cell(0, 10, line[2:].strip(), ln=True)
            pdf.ln(2)
            pdf.set_font('Arial', size=12)
        elif line.startswith('## '):
            style = HEADER_STYLE[2]
            pdf.set_font('Arial', style=style['style'], size=style['size'])
            pdf.cell(0, 10, line[3:].strip(), ln=True)
            pdf.ln(2)
            pdf.set_font('Arial', size=12)
        elif line.startswith('### '):
            style = HEADER_STYLE[3]
            pdf.set_font('Arial', style=style['style'], size=style['size'])
            pdf.cell(0, 8, line[4:].strip(), ln=True)
            pdf.ln(1)
            pdf.set_font('Arial', size=12)
        elif line.startswith('```'):
            if pdf.get_x() != 10:
                pdf.ln(4)
            # code block delimiter, ignore
            continue
        elif line.startswith('- '):
            text = '- ' + line[2:].strip()
            pdf.multi_cell(0, 6, text)
        else:
            pdf.multi_cell(0, 6, line)

    pdf.output(str(pdf_path))


if __name__ == '__main__':
    root = Path(__file__).resolve().parent.parent
    docs = [
        root / 'docs' / 'especificacion_lenguaje.md',
        root / 'docs' / 'reporte_optimizaciones.md',
    ]
    for md_file in docs:
        pdf_file = md_file.with_suffix('.pdf')
        render_markdown_to_pdf(md_file, pdf_file)
        print(f'Generado: {pdf_file}')
