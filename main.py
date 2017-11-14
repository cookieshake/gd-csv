class Table(object):
    def __init__(self):
        self.column_names = list()
        self.column_dtypes = list()
        self.rows = list()

    def read_csv(self, file_name, datatypes=dict()):
        csv_file = open(file_name, 'r')

        first_line = csv_file.readline().strip()
        for col in first_line.split(','):
            self.column_names.append(col)
            self.column_dtypes.append(datatypes.get(col, str))
        
        line = csv_file.readline().strip()
        while line != '':
            row = line.split(',')

            for i in range(len(row)):
                col_dtype = self.column_dtypes[i]
                row[i] = col_dtype(row[i])
            self.rows.append(row)

            line = csv_file.readline().strip()

    def sort_by(self, col_name, reverse=False):
        col_index = self.column_index(col_name)
        self.rows.sort(key=lambda x: x[col_index], reverse=reverse)

    def column_index(self, col_name):
        return self.column_names.index(col_name)

    

if __name__ == '__main__':
    t = Table()
    t.read_csv('hospital_info.csv', {'DISTANCE': int})
    t.sort_by('DISTANCE')
    
    today = input('오늘 날짜는? (YYYY-MM-DD) : ')

    today_col_index = t.column_index(today)
    dist_col_index = t.column_index('DISTANCE')
    name_col_index = t.column_index('HOSPITAL_NAME')

    print('{}에 영업하는 병원'.format(today))
    print('이름\t거리')
    for row in t.rows:
        if row[today_col_index] == 'O':
            print('{}\t{}'.format(row[name_col_index], row[dist_col_index]))




