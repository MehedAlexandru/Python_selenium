from logging import raiseExceptions
import unittest
from selenium import webdriver
import unittest

class WebTable():

    def __init__(self, webtable):
        self.table = webtable
    

    def get_row_count(self):
        return len(self.table.find_elements_by_tag_name("tr")) - 1

    def get_column_count(self):
        return len(self.table.find_elements_by_xpath(f"//tr[{2}]/td"))

    def get_table_size(self):
        return {"rows": self.get_row_count(),
                "columns": self.get_column_count()}
    
    def get_row_data(self, row_nnumber):
        if row_nnumber == 0:
            raise Exception("Rows start from 1")
        row_nnumber += 1
        row = self.table.find_elements_by_xpath(f"//tr[{row_nnumber}]/td")
        row_data = []
        for data in row:
            row_data.append(data.text)
        return row_data

    def get_col_data(self,column_number):
        col = self.table.find_elements_by_xpath("//tr/td["+str(column_number)+"]")
        rData = []
        for webElement in col:
            rData.append(webElement.text)
        return rData

    def get_all_data(self):
        # get number of rows
        noOfRows = len(self.table.find_elements_by_xpath("//tr")) -1
        # get number of columns
        noOfColumns = len(self.table.find_elements_by_xpath("//tr[2]/td"))
        allData = []
        # iterate over the rows, to ignore the headers we have started the i with '1'
        for i in range(2, noOfRows):
            # reset the row data every time
            ro = []
            # iterate over columns
            for j in range(1, noOfColumns) :
                # get text from the i th row and j th column
                ro.append(self.table.find_element_by_xpath("//tr["+str(i)+"]/td["+str(j)+"]").text)

            # add the row data to allData of the self.table
            allData.append(ro)

        return allData



class Test(unittest.TestCase):

    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(3)
    driver.get("https://chercher.tech/practice/table")
    w = WebTable(driver.find_element_by_xpath("//table[@id='webtable']"))


    print("No of rows : ", w.get_row_count())
    print("------------------------------------")
    print("No of cols : ", w.get_column_count())
    print("------------------------------------")
    print("Table size : ", w.get_table_size())
    print("------------------------------------")
    print("Second row data : ", w.get_row_data(2))
    print("------------------------------------")
    print("Second col data : ", w.get_col_data(2))
    print("------------------------------------")
    print("All data : ", w.get_all_data())
    print("------------------------------------")
    driver.close()



if __name__ == "__main__":
    unittest.main()