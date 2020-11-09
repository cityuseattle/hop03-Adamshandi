import openpyxl


wb=openpyxl.Workbook()
sheet= wb.active
sheet.title="Cars"
sheet['A1']="Models"
sheet['B1']="Price"


cars = [('BMW', 40000), ('Audi', 50000), ('Ford', 2500), 
('Mclaren', 1800000), ('Toyorta', 40000)]


for car in cars:
    sheet.append(car)
wb.save('car_data.xlsx')