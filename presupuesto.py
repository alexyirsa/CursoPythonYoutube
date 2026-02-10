from fpdf import FPDF

proyecto = input("Ingrese el nombre del proyecto: ")
horas_estimadas = float(input("Ingrese las horas estimadas para el proyecto: "))
valor_hora = float(input("Ingrese el valor por hora de trabajo: ")) 
plazo_dias = int(input("Ingrese el plazo en días para completar el proyecto: "))    
valor_total = horas_estimadas * valor_hora
print(f"\nPresupuesto para el proyecto '{proyecto}':")
print(f"Valor total del proyecto: ${valor_total:.2f}")
print(f"Plazo para completar el proyecto: {plazo_dias} días")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=f"Presupuesto para el proyecto '{proyecto}'", ln=True, align='C')
pdf.cell(200, 10, txt=f"Valor total del proyecto: ${valor_total:.2f}", ln=True, align='L')
pdf.cell(200, 10, txt=f"Plazo para completar el proyecto: {plazo_dias} días", ln=True, align='L')
pdf.cell(200, 10, txt="¡Gracias por confiar en nuestros servicios!", ln=True, align='C')
pdf.output(f"presupuesto_{proyecto}.pdf")





