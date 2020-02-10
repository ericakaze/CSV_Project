def main():
    import matplotlib.pyplot as plt
    #import csv
    from datetime import datetime 

    open_file1= "death_valley_2018_simple.csv"
    open_file= "sitka_weather_2018_simple.csv"
    place_name = [open_file,open_file1] #### this is a list of all the file names we need to use 
    p=0
    
    fig, ax  =plt.subplots(2,1, sharex=False) ### two rows and one column , first row as 0, second row as 1
    fig.suptitle("Temperature Comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US")
    for i in place_name:
        
        a,b,c,d= data(i)   #### for each file, get the dates, highs, lows and station_name
        ax[p].plot(a, b, color='red', alpha=0.5)   #plot, date and highs on row p where p is 0 for the first loop

        ax[p].plot(a, c, color='blue', alpha=0.5) #p is still 0 as it is plotting for the lows and still in the first loop
        ax[p].fill_between(a,c,b ,facecolor="blue", alpha=0.3)
        ax[p].set_title((d[0:-4]),fontsize=12) ## d is the station name and it is being sliced from the back,, 4 places to remove .csv
        p += 1 ### so here it goes back into line 29 and does the same thing 

        fig.autofmt_xdate() ### to format dates 
   
    
    
    plt.show()

def data (x): 
   #import matplotlib.pyplot as plt
    import csv
    from datetime import datetime 

    open_file= open(x, "r")
    csv_file= csv.reader(open_file, delimiter=",")

    header_row= next (csv_file)


    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')



    highs =[]
    dates= []
    lows= []
    
    for row in csv_file:

            try:
                high = int(row[high_index])
                low = int(row[low_index])
                current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
            station_name=row[1]
    return dates, highs ,lows, station_name





main()