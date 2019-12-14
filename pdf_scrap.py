from pprint import pprint
import tabula
from PyPDF2 import PdfFileReader
import pandas as pd
from pymongo import MongoClient

# Connect mongo db
db = MongoClient('localhost', 27017)['tabula']


def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        number_of_pages = pdf.getNumPages()
        # one way to scrap data is using pdffilereader, You can get complete content using this module
        print("Number of Pages", number_of_pages)
    # scrap data using tabula
    table = tabula.read_pdf(path, pages=1, pandas_options={'header': None})
    one = str(tabula.read_pdf(path, pages=2, area=(80, 65, 90, 200), pandas_options={'header': None})).strip(' 0\n0 ')
    one_ans= str(tabula.read_pdf(path, pages=2, area=(85, 65, 100, 200), pandas_options={'header': None})).strip(' 0\n0 ')
    two = str(tabula.read_pdf(path, pages=2, area=(100, 65, 120, 200), pandas_options={'header': None})).strip(' 0\n0 ')
    two_ans = str(tabula.read_pdf(path, pages=2, area=(120, 65, 130, 200), pandas_options={'header': None})).strip(' 0\n0 ')
    three = str(tabula.read_pdf(path, pages=2, area=(140, 65, 150, 200), pandas_options={'header': None})).strip(' 0\n0 ')
    three_ans = str(tabula.read_pdf(path, pages=2, area=(150, 65, 170, 200), pandas_options={'header': None})).strip(' 0\n0 ')
    three_ans = three_ans.replace('\n1',',')
    four = str(tabula.read_pdf(path, pages=2, area=(170, 65, 190, 200), pandas_options={'header': None})).strip(' 0\n0 ')
    four_ans = str(tabula.read_pdf(path, pages=2, area=(190, 65, 200, 200), pandas_options={'header': None})).strip(' 0\n0 ')
    five = str(tabula.read_pdf(path, pages=2, area=(200, 65, 220, 200), pandas_options={'header': None})).strip(' 0\n0 ')
    five_ans = str(tabula.read_pdf(path, pages=2, area=(220, 65, 230, 200), pandas_options={'header': None})).strip(' 0\n0 ')
    six = str(tabula.read_pdf(path, pages=2, area=(240, 65, 250, 200), pandas_options={'header': None})).strip(' 0\n0 ')
    six_ans = str(tabula.read_pdf(path, pages=2, area=(250, 65, 260, 200), pandas_options={'header': None})).strip(' 0\n0 ')
    seven = str(tabula.read_pdf(path, pages=2, area=(260, 65, 280, 200), pandas_options={'header': None})).strip(' 0\n0 ')
    seven_ans = str(tabula.read_pdf(path, pages=2, area=(280, 85, 330, 750), pandas_options={'header': None})).strip(' 0\n0 ')
    seven_ans = seven_ans.replace('NaN','').replace('0','').replace('\n','').replace('1     2\n','').replace('2','').strip('1       ')
    seven_ans=seven_ans.replace('1                                  ','').strip(' ')
    eight = str(tabula.read_pdf(path, pages=2, area=(330, 65, 360, 750), pandas_options={'header': None})).strip(' 0\n0 ')
    eight_ans = tabula.read_pdf(path, pages=2, area=(350, 80, 600, 1500), pandas_options={'header': None})
    eight_ans = eight_ans.values.tolist()
    eight_ans = str(eight_ans).replace('], [nan,','').replace('\'','').replace('[','').replace(']','')
    nine_ansa = tabula.read_pdf(path, pages=2, area=(600, 80, 720, 950), pandas_options={'header': None})
    nine_ansa = nine_ansa.values.tolist()
    nine_ansb = tabula.read_pdf(path, pages=3, area=(30, 80, 120, 950), pandas_options={'header': None})
    nine_ansb = nine_ansb.values.tolist()
    nine_ans =[nine_ansa,nine_ansb]
    nine_ans = str(nine_ans).replace('nan','').replace('\'','').replace(']','').replace('[','')
    ten_ans = tabula.read_pdf(path, pages=3, area=(120, 85, 250, 950), pandas_options={'header': None})
    ten_ans = ten_ans.values.tolist()
    ten_ans = str(ten_ans).replace('], [nan,','').replace('\'','').replace('[','').replace(']','')
    eleven_ans = tabula.read_pdf(path, pages=3, area=(250, 85, 380, 950), pandas_options={'header': None})
    eleven_ans = eleven_ans.values.tolist()
    eleven_ans = str(eleven_ans).replace('], [nan,','').replace('\'','').replace('[','').replace(']','')
    twelve_ans = tabula.read_pdf(path, pages=3, area=(380, 80, 510, 950), pandas_options={'header': None})
    twelve_ans = twelve_ans.values.tolist()
    twelve_ans = str(twelve_ans).replace('\'','').replace('[','').replace(']','')
    thirteen_ans = tabula.read_pdf(path, pages=3, area=(510, 80, 680, 950), pandas_options={'header': None})
    thirteen_ans = thirteen_ans.values.tolist()
    thirteen_ans = str(thirteen_ans).replace('\'','').replace('[','').replace(']','')
    fourtheen_ans = tabula.read_pdf(path, pages=3, area=(680, 85, 740, 950), pandas_options={'header': None})
    fourtheen_ans = fourtheen_ans.values.tolist()
    thirteen = tabula.read_pdf('JC.pdf', pages=4, area=(30, 80, 185, 950), pandas_options={'header': None})
    thirteen = thirteen.values.tolist()
    merg_g = [fourtheen_ans,thirteen]
    merg_g = str(merg_g).replace('], [nan,','').replace('\'','').replace('[','').replace(']','').replace('0, nan','')
    last = str(tabula.read_pdf(path, pages=4, area=(185, 70, 210, 900), pandas_options={'header': None})).strip(' 0\n0 ')
    last_ans = tabula.read_pdf(path, pages=4, area=(210, 80, 260, 900), pandas_options={'header': None})
    last_ans = last_ans.values.tolist()
    last_ans = str(last_ans).replace('], [nan,','').replace('\'','').replace('[','').replace(']','').replace('nan','')
    last_ansb = tabula.read_pdf(path, pages=4, area=(260, 80, 300, 900), pandas_options={'header': None})
    last_ansb = last_ansb.values.tolist()
    last_ansb = str(last_ansb).replace('], [nan,','').replace('\'','').replace('[','').replace(']','').replace('nan','')

    table.to_csv('table.csv') # insert data or table into csv file

    # insert data into Mongodb
    db.pdf.insert_one({one: one_ans,
                        two:two_ans,
                        three: three_ans,
                        four:four_ans,
                        five:five_ans,
                        six:six_ans,
                        seven:seven_ans,
                        eight:[{'A':eight_ans,'B':nine_ans,'C':ten_ans,'D':eleven_ans,'E':twelve_ans,'F':thirteen_ans,'G':merg_g}],
                        last:[{'A':last_ans,'B':last_ansb}]})

    # prity print data
    pprint({one: one_ans,
            two:two_ans,
            three: three_ans,
            four:four_ans,
            five:five_ans,
            six:six_ans,
            seven:seven_ans,
            eight:[{'A':eight_ans,'B':nine_ans,'C':ten_ans,'D':eleven_ans,'E':twelve_ans,'F':thirteen_ans,'G':merg_g}],
            last:[{'A':last_ans,'B':last_ansb}]})


if __name__ == '__main__':
    path = 'JC.pdf' # specify pdf name here
    text_extractor(path)