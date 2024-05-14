import openpyxl
import csv

# Список путей к файлам Excel и соответствующих регионов
excel_files = [
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Shymkent.XLSX", 'region': 'Shymkent city'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Turkistan Region.XLSX", 'region': 'Turkestan region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Ulytau Region.XLSX", 'region': 'Ulytau region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Zhetysu Region.XLSX", 'region': 'West Kazakhstan region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Zhambyl Region.XLSX", 'region': 'Jambyl region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Zhetysu Region.XLSX", 'region': 'Jetisu region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Abay Region.XLSX", 'region': 'Abay region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Akmola Region.XLSX", 'region': 'Akmola region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Aktobe Region.XLSX", 'region': 'Aktobe region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Almaty.XLSX", 'region': 'Almaty city'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Almaty Region.XLSX", 'region': 'Almaty region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Astana.XLSX", 'region': 'Astana city'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Atyrau Region.XLSX", 'region': 'Atyrau region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\East-Kazakhstan Region.XLSX", 'region': 'East Kazakhstan region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Karagandy Region.XLSX", 'region': 'Karaganda region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Kostanay Region.XLSX", 'region': 'Kostanay region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Kyzylorda Region.XLSX", 'region': 'Kyzylorda region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Mangistay Region.XLSX", 'region': 'Mangystau Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\North-Kazakhstan Region.XLSX", 'region': 'North Kazakhstan region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-crime\archive\Pavlodar Region.XLSX", 'region': 'Pavlodar region'},

    # Добавьте остальные файлы и их регионы по аналогии
]


# Имя файла для сохранения данных
output_csv = r'C:\Users\USER\Desktop\practice\city-crime\data\comb.csv'

def get_total_offenses_value(excel_path):
    wb = openpyxl.load_workbook(excel_path, data_only=True)
    sheet = wb.active
    total_offenses = sheet.cell(row=7, column=5).value  # Получаем значение из столбца E, строки 7
    return total_offenses

# Открытие CSV файла для записи
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Region', 'Value'])
    
    for file_info in excel_files:
        total_offenses = get_total_offenses_value(file_info['path'])
        if total_offenses is not None:
            writer.writerow([file_info['region'], total_offenses])
        else:
            print(f"No data found for {file_info['region']}")

print("Data has been written to", output_csv)