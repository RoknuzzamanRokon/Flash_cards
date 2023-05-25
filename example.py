import pandas

read_csv_file = pandas.read_csv("data/english_words-Sheet_02.csv")

records_file = read_csv_file.to_dict("records")

print(records_file)