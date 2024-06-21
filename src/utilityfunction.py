def read_csv(filename):
    data = []  
    with open(filename, 'r') as file:  
        for line in file:  # Iterasi melalui setiap baris dalam file
            values = []  
            current_value = ''  
            in_quotes = False  
            for char in line:  # Iterasi melalui setiap karakter dalam baris
                if char == ';' and not in_quotes:  
                    values.append(current_value)  
                    current_value = ''  
                elif char == '"':  
                    in_quotes = not in_quotes  
                elif char != '\n':  
                    current_value += char  
            values.append(current_value)  
            data.append(values)  
    return data

# Mengubah matrix menjadi csv
def array_to_csv(array_data, csv_file):
    with open(csv_file, 'w') as csvfile:
        for row in array_data:
            csv_line = ';'.join(str(cell) for cell in row) + '\n'
            csvfile.write(csv_line)
# Mencari kolom atribut
def get_atributes_column(matrix : list, type: any):
    for col in range(0, len(matrix[0])):
        if matrix[0][col] == type:
            return col
        
def get_data_by_column_title (matrix, column_title):
    array = []
    for col in range(0, len(matrix[0])):
        if matrix[0][col] == column_title:
            for row in range(1, len(matrix)):
                array.append(matrix[row][col])
    return array

def get_row(matrix : list, type : any, anything : any):
    column = get_atributes_column(matrix, type)
    array = []
    for row in matrix:
        if row[column] == anything:
            array.append(row)
    return array


