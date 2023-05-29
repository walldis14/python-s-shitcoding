import os
import time
import pandas as pd 
import pdfkit 
from selenium import webdriver 

# Получаем абсолютный путь к файлу wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=os.path.abspath('/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'))

# Получаем абсолютный путь к файлу Excel
excel_path = os.path.abspath('test2.xlsx.xlsx')

# Загружаем данные из Excel файла 
df = pd.read_excel(excel_path)

# Инициализируем объект WebDriver для работы с браузером 
with webdriver.Chrome() as driver:
    # Проходимся по каждой строке таблицы 
    for index, row in df.iterrows(): 
        # Получаем URL страницы из соответствующей колонки в Excel 
        url = row['URL'] 
        
        try:
            # Открываем страницу в браузере 
            driver.get(url) 
            
            # Получаем заголовок страницы и используем его в качестве имени файла для PDF 
            title = driver.title 
            filename = url[-10:] + '.pdf'
            
            # Сохраняем страницу в PDF формате 
            pdfkit.from_url(url, filename, configuration=config)
            
            print(f'{url} - Сохранено в {filename}')
        except Exception as e:
            print(f'{url} - Ошибка: {str(e)}')
            
        # Добавляем задержку в 10 секунд между запросами
        time.sleep(10)

print('Завершено!')