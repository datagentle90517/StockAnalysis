import yfinance as yf
import sqlite3

def outputStockKline(stockCode:str,startDate:str,endDate:str):
    """
    :param stockCode:請輸入股票代碼
    :param startDate: 起始日期(格式YYYY-MM-DD)
    :param endDate: 結束日期(格式YYYY-MM-DD)
    :return:df
    """
    global df
    df = yf.download(stockCode+".TW", start=startDate, end=endDate)
    df.to_csv('historyKline.csv', index=True, sep=',')
    print(df)
    return df

def creatDataTable():
    global conn,cursor
    conn = sqlite3.connect('stock_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stockTable (
            Date DATE PRIMARY KEY,
            Open FLOAT NOT NULL,
            High FLOAT NOT NULL,
            Low FLOAT NOT NULL,
            Close FLOAT NOT NULL,
            `Adj Close` FLOAT NOT NULL,
            Volume FLOAT NOT NULL
        )
    ''')
    conn.commit()

def importCSVToDataTable():
    df.to_sql('stockTable', conn, if_exists='append', index=True, index_label='Date')


#outputStockKline("2330","2020-12-01","2023-12-03")
#creatDataTable()
#importCSVToDataTable()


