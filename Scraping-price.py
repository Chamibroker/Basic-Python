import urllib.request
import datetime

# Create get stock quote Function
def get_stock_price(stock,from_dt,to_dt):
    ###################### 1. Histrorical Price Link
    #get Histrorical link from Yahoo Finance web site
    #https://query1.finance.yahoo.com/v7/finance/download/PTT.BK?period1=1649030400&period2=1649462400&interval=1d&events=history&includeAdjustedClose=true
    
    #link = "https://query1.finance.yahoo.com/v7/finance/download/PTT.BK?period1=1649030400&period2=1649462400&interval=1d&events=history&includeAdjustedClose=true"
    
    ###################### 2. Histrorical Dividen Yeild  Link
    link2_DV = "https://query1.finance.yahoo.com/v7/finance/download/PTT.BK?period1=1491696000&period2=1649462400&interval=1d&events=div&includeAdjustedClose=true"
    
    # Open file from link and Read file
    #with urllib.request.urlopen(link) as f: # Scraping Histrorical Price
    with urllib.request.urlopen(link2_DV) as f: # Scraping Dividen Yeild 
        s = f.read()
    # print without decode("utf8") will generate data form b data (byte Sequence)
    print(s)
    # print with decode("utf8") will generate data like a pd.dataFrame
    print(s.decode("utf8"))
    # You can Write download file to EXcel or CSV file
    with open("ptt_diveden yeild.csv","w") as fw: # "w" = Mode Write file
        fw.write(s.decode("utf8")) # Write with Excecute Decoder("utf8") we will Get csv File shown in left Explore windows
    return s
# Call function 
ptt = get_stock_price("","","")

