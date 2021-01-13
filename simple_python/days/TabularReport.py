from FileHandling import FileHandling
from  html_report import HtmlReport, ReportHeader
import pandas as pd

class TabularReport(object):

    def __init__(self,dataset,column_list,file_name,report_title,table_template):
        self.dataset = dataset
        self.column_list = column_list
        self.file_name = file_name
        self.report_title = report_title
        self.table_template = table_template
        self.fh = FileHandling(file_name)
        self.fh.create_file()

    def geneate_report(self):
        html = HtmlReport(self.dataset,self.column_list)
        header = ReportHeader(self.report_title)
        if not html.columns_list_validate():
           print('There is error while validating columns')

        # Add Header
        self.fh.append_another_file_before('header.html')
        report_header = header.generate_header()
        self.fh.append_file(report_header)

        # add table style template
        self.fh.append_another_file_before(self.table_template)

        table_header = html.gen_table_header()
        self.fh.append_file(table_header)

        table_body = html.gen_table_data()
        self.fh.append_file(table_body)

        footer = header.genrate_footer()
        self.fh.append_file(footer)








if __name__ == "__main__":
    df = pd.read_csv("/Users/nilvarshney/Google Drive/Machine Learning/PythonML/Datasets/foods.csv")
    columns = ['First Name', 'Gender', 'City', 'Frequency', 'Item','Unknown']
    treport  = TabularReport( dataset = df, column_list = columns, file_name = 'welcome.html',report_title = "Welcome Tabular Report",table_template = 'table-template2.css')
    treport.geneate_report()




"""
    <style>
    table {
        width:100%;
    }
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    th, td {
        padding: 5px;
        text-align: left;
    }
    table tr:nth-child(even) {
        background-color: #eee;
    }
    table tr:nth-child(odd) {
       background-color: #ccc;
    }
    table th {
        background-color: black;
        color: white;
    }
    </style>
"""
