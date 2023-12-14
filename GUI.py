import tkinter as tk
from tkinter import messagebox
from Lib import *
from backtest import *

def startAnalysis():
    guiStockCode=stockCodeText.get()
    guiStartDate=startDateText.get()
    guiEndDate=endDateText.get()
    guiManualorOpt=val.get()
    guiMoney=moneyText.get()
    guiFee=feeText.get()

    if(guiStockCode!="" and guiStartDate!="" and guiEndDate!="" and guiMoney!="" and guiFee!=""):
        if(guiManualorOpt=="手動輸入"):
            guiManualShort = int(manualShortText.get())
            guiManualLong = int(manualLongText.get())
            testdata=outputStockKline(guiStockCode,guiStartDate,guiEndDate)
            result=backtest(True,testdata,int(guiMoney),float(guiFee),guiManualShort,guiManualLong,0,0,0,0)
            messagebox.showinfo('分析結果',str(result)+"\n使用策略:"+str(result["_strategy"]))
        elif(guiManualorOpt=="最佳化"):
            guiOptShortRange1 = int(optShortRange1Text.get())
            guiOptShortRange2 = int(optShortRange2Text.get())
            guiOptLongRange1 = int(optLongRange1Text.get())
            guiOptLongRange2 = int(optLongRange2Text.get())
            testdata = outputStockKline(guiStockCode, guiStartDate, guiEndDate)
            result=backtest(False,testdata,int(guiMoney),float(guiFee),0,0,guiOptShortRange1,guiOptShortRange2,guiOptLongRange1,guiOptLongRange2)
            messagebox.showinfo('最佳化分析結果',str(result)+"\n使用策略:"+str(result["_strategy"]))
    else:
        messagebox.showerror("錯誤","請確認回測資料是否填寫完整")

def manualBtn():
    manualShort.config(state='normal')
    manualShortText.config(state='normal')
    manualLong.config(state='normal')
    manualLongText.config(state='normal')
    optShortRange.config(state='disable')
    optShortRange1Text.config(state='disable')
    optShortRange2Text.config(state='disable')
    optLongRange.config(state='disable')
    optLongRange1Text.config(state='disable')
    optLongRange2Text.config(state='disable')
def optBtn():
    manualShort.config(state='disable')
    manualShortText.config(state='disable')
    manualLong.config(state='disable')
    manualLongText.config(state='disable')
    optShortRange.config(state='normal')
    optShortRange1Text.config(state='normal')
    optShortRange2Text.config(state='normal')
    optLongRange.config(state='normal')
    optLongRange1Text.config(state='normal')
    optLongRange2Text.config(state='normal')

#介面設計------------------------------------------------------------------------------------------------------------------------------
window=tk.Tk()
window.title("台股策略分析")
window.geometry("400x430")
window.resizable(False,False)

stockCode = tk.Label(text='請輸入股票代碼:',font=('標楷體',14))
stockCode.place(x=30,y=20)
stockCodeText = tk.Entry()
stockCodeText.place(x=190,y=25)

dateFormat = tk.Label(text='格式:YYYY-MM-DD',font=('標楷體',14),fg='#f00')
dateFormat.place(x=240,y=110)

startDate = tk.Label(text='請輸入起始日期:',font=('標楷體',14))
startDate.place(x=30,y=50)
startDateText = tk.Entry()
startDateText.place(x=190,y=55)

endDate = tk.Label(text='請輸入結束日期:',font=('標楷體',14))
endDate.place(x=30,y=80)
endDateText = tk.Entry()
endDateText.place(x=190,y=85)

val = tk.StringVar()
manualEntry = tk.Radiobutton(text='策略MA(移動平均線)',variable=val, value='手動輸入',font=('標楷體',14),command=manualBtn)
manualEntry.place(x=30,y=110)

manualShort = tk.Label(text='手動輸入=>短線:',font=('標楷體',14))
manualShort.place(x=80,y=150)
manualShortText=tk.Entry(width=5)
manualShortText.place(x=240,y=155)

manualLong = tk.Label(text='長線:',font=('標楷體',14))
manualLong.place(x=280,y=150)
manualLongText=tk.Entry(width=5)
manualLongText.place(x=340,y=155)

optEntry = tk.Radiobutton(text='最佳化MA策略(短線須小於長線)',variable=val, value='最佳化',font=('標楷體',14),command=optBtn)
optEntry.place(x=30,y=190)

optShortRange = tk.Label(text='請輸入短線範圍:      ~',font=('標楷體',14))
optShortRange.place(x=80,y=230)
optShortRange1Text=tk.Entry(width=5)
optShortRange1Text.place(x=240,y=235)
optShortRange2Text=tk.Entry(width=5)
optShortRange2Text.place(x=320,y=235)

optLongRange = tk.Label(text='請輸入長線範圍:      ~',font=('標楷體',14))
optLongRange.place(x=80,y=255)
optLongRange1Text=tk.Entry(width=5)
optLongRange1Text.place(x=240,y=260)
optLongRange2Text=tk.Entry(width=5)
optLongRange2Text.place(x=320,y=260)

backtestSet=tk.Label(text='回測設定',font=('標楷體',14))
backtestSet.place(x=30,y=300)

money=tk.Label(text='本金:',font=('標楷體',14))
money.place(x=80,y=340)
moneyText=tk.Entry()
moneyText.place(x=140,y=345)

fee=tk.Label(text='手續費:',font=('標楷體',14))
fee.place(x=60,y=370)
feeText=tk.Entry()
feeText.place(x=140,y=375)

Analysis=tk.Button(text="開始分析",font=('標楷體',14),command=startAnalysis)
Analysis.place(x=300,y=350)
Analysis.config(state='normal')

manualEntry.invoke() #預設勾選手動輸入

window.mainloop()
