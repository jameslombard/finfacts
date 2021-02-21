import tabula

# df = tabula.read_pdf("./files/0-jan-april-2019.pdf" , pages="all")
# convert PDF into CSV file

tabula.convert_into("./files/0-jan-april-2019.pdf", "output.csv", output_format="csv", pages='all' , stream=True)

# data = df.to_excel('0.xlsx')
# tabula.convert_into_by_batch("input_directory", "output.csv" ,output_format='csv', pages='all' , stream=True)