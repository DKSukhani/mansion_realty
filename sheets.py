import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("mansionreality").sheet1

# data = sheet.get_all_records()  # Get a list of all records
# # pprint(data)
#
#
# row = sheet.row_values(3)  # Get a specific row
# # pprint(row)
#
# col = sheet.col_values(3)  # Get a specific column
# # pprint(col)
#
# cell = sheet.cell(1,2).value  # Get the value of a specific cell
# # pprint(cell)

insertRow = [8, "RJ", "red"]
sheet.append_row(insertRow)

# sheet.update_cell(2,1, 3)  # Update one cell

# numRows = sheet.row_count  # Get the number of rows in the sheet