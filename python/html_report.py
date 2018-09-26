import pandas as pd
import os
import datetime


filename = "sample.html"

class HtmlReport(object):


    def __init__(self, data_set, columns_list, table_style =''):
        self.data_set = data_set
        self.column_list = columns_list
        self.table_style = table_style

    def open_file(self):
        global f
        try:
            os.remove(filename)  # try to remove it directly
        except OSError as e:
            print("File Does not exists")
        finally:
            f = open(filename, "x")

    def append_file(self, text):
        f.write()

    def close_file(self):
        f.write("Sample text to file")
        f.close()

    """
    this method check the data set and provided list. If there is any extra column provided then it is removed.
    If provided Columns is sorter then it add the column(s) at the end with the "Unknown Columns"
    """
    def columns_list_validate(self):
        # print(self.data_set.shape[1] , len(self.column_list))
        if self.data_set.shape[1] > len(self.column_list):
            for counter in range(self.data_set.shape[1] - len(self.column_list)):
                self.column_list.append("Unknown Columns")
        elif self.data_set.shape[1] < len(self.column_list):
            for counter in range(len(self.column_list) - self.data_set.shape[1] ):
                self.column_list.pop()
        else:
            pass
        return True

    def gen_table_header(self):
        line = '\n<table border="1" class="dataframe">\n'
        line += '<thead>\n'
        line += '<tr style="text-align: center;">\n'
        for counter in range(len(self.column_list)):
            line += '\t<th>' + self.column_list[counter] + '</th>\n'
        line += '\t</tr>\n'
        line += '</thead>\n'
        return line
        # print(line)

    def gen_table_data(self):
        #numerical_data_type = ['int','float32','float64,float128']
        line = '<tbody>\n'
        for counter in range(self.data_set.shape[0]):
            line += '\t<tr>\n'
            for inner_counter in range(self.data_set.shape[1]):
                if issubclass(type(self.data_set.iat[counter, inner_counter]),int) or issubclass(type(self.data_set.iat[counter, inner_counter]),float):
                    line += '\t\t<td ALIGN=RIGHT>' + str(self.data_set.iat[counter, inner_counter]) + '</td>\n'
                else:
                    line += '\t\t<td >' + str(self.data_set.iat[counter, inner_counter]) + '</td>\n'
            line += '\t</tr>\n'
        line += '</tbody>\n'
        return line



class ReportHeader(object):

    def __init__(self,header_text):
        self.header_text = header_text
        self.header_sub_text = datetime.datetime.today().strftime('%B, %d %Y %H:%M:%S')

    def generate_header(self):
        line = '<body>\n'
        line += '\t<h1>' + self.header_text + '</h1>\n'
        line += '\t<h6>' + self.header_sub_text + '</h6>\n'
        return  line


    def genrate_footer(self):
        line = '</body >'
        return line
#
#
#
#
#
#
#
#
#

if __name__ == "__main__":
    df = pd.read_csv("/Users/nilvarshney/Google Drive/Machine Learning/PythonML/Datasets/foods.csv")
    columns = ['First Name', 'Gender', 'City',  'Frequency', 'Item']
    report = HtmlReport(df, columns, file_name='hello.html')
    report.columns_list_validate()
    report.gen_table_header()
    report.gen_table_data()
    report.open_file()
    report.close_file()


