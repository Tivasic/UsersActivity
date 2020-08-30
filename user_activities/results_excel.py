import xlsxwriter
from sqlalchemy.orm import Session

from database import table_model


def save_results_to_excel(filename: str, db: Session):
    results = db.query(table_model.Post).all()
    filename_prefix = filename + ".xlsx"
    workbook = xlsxwriter.Workbook(filename_prefix)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})

    worksheet.set_column('A:A', 14)
    worksheet.set_column('B:B', 14)
    worksheet.set_column('C:C', 10)

    worksheet.write('A1', 'Проект', bold)
    worksheet.write('B1', 'Активность', bold)
    worksheet.write('C1', 'Длительность', bold)

    cell_format = workbook.add_format()
    row_count = 1
    for result in results:
        worksheet.write(row_count, 0, result.project, cell_format)
        worksheet.write(row_count, 1, result.activity, cell_format)
        worksheet.write(row_count, 2, result.duration, cell_format)
        row_count += 1
    workbook.close()

    #  TODO: Почему такой странный формат результатов?
    return ["Отчет", filename, "создан"]
