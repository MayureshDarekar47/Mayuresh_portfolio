from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        pass
    def footer(self):
        pass

pdf = PDF(format='A4')
pdf.set_margins(15, 15, 15)
pdf.add_page()

# Title
pdf.set_font('helvetica', 'B', 22)
pdf.set_text_color(30, 30, 30)
pdf.cell(0, 10, 'Mayuresh Darekar', ln=True)

# Subtitle
pdf.set_font('helvetica', '', 11)
pdf.set_text_color(60, 60, 60)
pdf.cell(0, 7, 'Second Year B.Tech Computer Science Engineering Student', ln=True)

# Contact info
pdf.set_font('helvetica', '', 9)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 5, 'Email: mayureshdarekar2007@gmail.com | LinkedIn: linkedin.com/in/mayuresh-darekar-99555b387 | GitHub:', ln=True)
pdf.cell(0, 5, 'github.com/MayureshDarekar47', ln=True)

pdf.ln(2)
# Line
pdf.set_draw_color(220, 220, 220)
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(6)

# Profile Summary
pdf.set_font('helvetica', 'B', 14)
pdf.set_text_color(0, 120, 200)
pdf.cell(0, 8, 'Profile Summary', ln=True)

pdf.set_font('helvetica', '', 10)
pdf.set_text_color(60, 60, 60)
pdf.multi_cell(0, 5, 'Computer Science student interested in programming, web development, and building clean digital projects.\nCurrently learning Java and DBMS, along with C, C++, HTML, and Python with a focus on logic building, beginner\nprojects, and professional growth.')
pdf.ln(4)

# Education
pdf.set_font('helvetica', 'B', 14)
pdf.set_text_color(0, 120, 200)
pdf.cell(0, 8, 'Education', ln=True)

pdf.set_font('helvetica', 'B', 10)
pdf.set_text_color(60, 60, 60)
pdf.write(6, 'B.Tech in Computer Science Engineering ')
pdf.set_font('helvetica', '', 10)
pdf.write(6, '- D Y Patil International University\n')
pdf.cell(0, 6, 'Current Year: Second Year', ln=True)
pdf.ln(4)

# Technical Skills
pdf.set_font('helvetica', 'B', 14)
pdf.set_text_color(0, 120, 200)
pdf.cell(0, 8, 'Technical Skills', ln=True)

pdf.set_font('helvetica', '', 10)
pdf.set_text_color(60, 60, 60)
pdf.multi_cell(0, 6, '- Programming Languages: Java, C, C++, Python basics\n- Web Technologies: HTML, CSS, JavaScript basics\n- Tools: VS Code, GitHub\n- Core Skills: DBMS, Logic building, problem solving, project documentation')
pdf.ln(4)

# Projects
pdf.set_font('helvetica', 'B', 14)
pdf.set_text_color(0, 120, 200)
pdf.cell(0, 8, 'Projects', ln=True)

pdf.set_font('helvetica', 'B', 10)
pdf.set_text_color(60, 60, 60)
pdf.write(6, 'Personal Portfolio Website ')
pdf.set_font('helvetica', '', 10)
pdf.write(6, '- Responsive website to showcase education, skills, certificates, projects, and\ncontact links.\n')

pdf.ln(2)

pdf.set_font('helvetica', 'B', 10)
pdf.write(6, 'C / C++ Practice Programs ')
pdf.set_font('helvetica', '', 10)
pdf.write(6, '- Beginner programs based on variables, operators, loops, conditions, functions...\n')

pdf.output('portfolio/resume.pdf')
