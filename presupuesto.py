from fpdf import FPDF

proyecto = input("Ingrese el nombre del proyecto: ")
horas_estimadas = float(input("Ingrese las horas estimadas para el proyecto: "))
valor_hora = float(input("Ingrese el valor por hora de trabajo: ")) 
plazo_dias = int(input("Ingrese el plazo en días para completar el proyecto: "))    
valor_total = horas_estimadas * valor_hora

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=f"Presupuesto para el proyecto '{proyecto}'", ln=True)
pdf.cell(200, 10, txt=f"Valor total del proyecto: ${valor_total:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Plazo para completar el proyecto: {plazo_dias} días", ln=True)
pdf.cell(200, 10, txt="¡Gracias por confiar en nuestros servicios!")
pdf.output(f"presupuesto_{proyecto}.pdf")





