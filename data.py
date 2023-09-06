import gspread
import pandas as pd

def get_data(spreadsheet, worksheet):

  # Connect to Google Sheets using the provided credentials
  gspread_client = gspread.service_account(filename="credentials.json")

  # Open the specific spreadsheet by title
  spreadsheet = gspread_client.open(spreadsheet)

  # Select the "Bucket Number Collection" sheet by title
  worksheet = spreadsheet.worksheet(worksheet)

  # Get all data from the selected sheet
  all_data = worksheet.get_all_values()

  # Convert the data to a Pandas DataFrame
  df = pd.DataFrame(all_data[1:], columns=all_data[0])  # Assuming the first row contains column headers

  return df

