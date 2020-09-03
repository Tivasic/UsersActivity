import xlsxwriter
from sqlalchemy import extract
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

from database import table_model


def save_results_to_excel(filename: str, year: int, month: int, day: int, db: Session):
    results = db.query(table_model.Post).filter(
        extract('year', table_model.Post.date) == year,
        extract('month', table_model.Post.date) == month,
        extract('day', table_model.Post.date) >= day).all()

    filename_prefix = filename + ".xlsx"

    workbook = xlsxwriter.Workbook(filename_prefix)
    worksheet = workbook.add_worksheet()

    date_format = workbook.add_format({'num_format': 'd-m-yyyy'})
    cell_format = workbook.add_format({'bold': True})
    cell_format.set_align('center')

    worksheet.set_column('A:A', 25)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 15)
    worksheet.set_column('D:D', 15)

    worksheet.write('A1', 'Проект', cell_format)
    worksheet.write('B1', 'Активность', cell_format)
    worksheet.write('C1', 'Длительность', cell_format)
    worksheet.write('D1', 'Дата', cell_format)

    row_count = 1
    for result in results:
        worksheet.write(row_count, 0, result.project)
        worksheet.write(row_count, 1, result.activity)
        worksheet.write(row_count, 2, result.duration)
        worksheet.write(row_count, 3, result.date, date_format)
        row_count += 1
    workbook.close()

    return FileResponse(filename_prefix)
