import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import matplotlib.dates as mdates

from urllib.request import Request, urlopen  # Python 3


def plotCovidFigure(dataCovid):
  print("I'm plotting")
  date=dataCovid['data'].to_numpy()
  lastDateString=date[-1]
  print("lastDate ",lastDateString)
  lastDay=datetime.date(int(lastDateString[0:4]),int(lastDateString[5:7]),int(lastDateString[8:10]))
  ospedalizzati = dataCovid['totale_ospedalizzati'].to_numpy()
  nuovi_positivi=dataCovid['nuovi_positivi'].to_numpy()
  maxLen=len(nuovi_positivi)

  decessiTotali = dataCovid['deceduti'].to_numpy()
  nuovi_decessi = np.zeros(maxLen)
  nuovi_decessi[1:] = decessiTotali[1:]-decessiTotali[:-1]
  nuovi_TI = dataCovid['ingressi_terapia_intensiva'].to_numpy()
  TI = dataCovid['terapia_intensiva'].to_numpy()
  nuovi_decessi_average = np.zeros(maxLen)
  nuovi_decessi_average[6:]= np.convolve(nuovi_decessi,1/7*np.ones(7),'valid')
  nuovi_positivi_average = np.zeros(maxLen)
  nuovi_positivi_average[6:]= np.convolve(nuovi_positivi,1/7*np.ones(7),'valid')
  nuovi_TI_average = np.zeros(maxLen)
  nuovi_TI_average[6:]= np.convolve(nuovi_TI,1/7*np.ones(7),'valid')
  dates=dataCovid['data'].to_numpy()
  dateValues = [datetime.datetime.strptime(dates[d][:10],"%Y-%m-%d").date() for d in range(maxLen)]

  let=0.02;
  ospDeaths=0.013;
  ICUDeaths=0.115;
  deathsShift=13;
  hospShift=10;
  ICUShift=12;
  newICUshift=5;
  newICUDeaths=1.7;

  fig, ax1=plt.subplots(figsize=(12,6),dpi=600)
  minMax=1000
  plt.semilogy([d- datetime.timedelta(days=hospShift) for d in dateValues],
              ospedalizzati*ospDeaths,"-.",linewidth=2,
              label=f'Ospedalizzati per %1.3f %d gg dopo'%(ospDeaths,hospShift))
  minMax=max(minMax,np.max(ospedalizzati*ospDeaths)*1.5)
  plt.semilogy([d- datetime.timedelta(days=ICUShift) for d in dateValues],
              TI*ICUDeaths,":",linewidth=2,
              label=f'Terapia Intensiva per %1.3f %d gg dopo'%(ICUDeaths,ICUShift))
  minMax=max(minMax,np.max(TI*ICUDeaths)*1.5)
  plt.semilogy([d- datetime.timedelta(days=newICUshift) for d in dateValues],
              nuovi_TI_average*newICUDeaths,"--",linewidth=2,
              label=f'Nuovi ingressi in TI per %1.3f %d gg dopo'%(newICUDeaths,newICUshift))


  minMax=max(minMax,np.max(nuovi_TI_average*newICUDeaths)*1.5)
  plt.semilogy(dateValues,
              nuovi_positivi_average*let,"-",linewidth=2,
              label=f'Nuovi casi per %1.3f'%(let))

  minMax=max(minMax,np.max(nuovi_positivi_average*let)*1.5)
  plt.semilogy([d- datetime.timedelta(days=deathsShift) for d in dateValues],
              nuovi_decessi_average, linewidth=2,
              label=f"Nuovi decessi %d gg dopo"%(deathsShift))

  minMax=max(minMax,np.max(nuovi_decessi_average)*1.5)

  plt.semilogy(dateValues[-1]- datetime.timedelta(days=newICUshift-1),
              nuovi_TI[-1]*newICUDeaths,".",color="green",label="Nuove TI oggi %d"%(nuovi_TI[-1]))
  plt.semilogy(dateValues[-1]- datetime.timedelta(days=-1),
              nuovi_positivi[-1]*let,".",color="red",label=f"Nuovi casi oggi {nuovi_positivi[-1]:,}")
  plt.semilogy(dateValues[-1]- datetime.timedelta(days=deathsShift-1),
              nuovi_decessi[-1],".",color="purple",label="Nuovi decessi oggi %d"%(nuovi_decessi[-1]))

  minMax=max(minMax,np.max(nuovi_positivi[-1]*let)*1.2)

  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  plt.text(datetime.date(2020,9,1),minMax/4,f"Nuovi casi media ultimi 7 giorni {int(nuovi_positivi_average[-1]):,}\n"
                                                              f"Nuove TI media ultimi 7 giorni {int(nuovi_TI_average[-1]):,}\n"
                                                              f"Nuovi decessi media ultimi 7 giorni {int(nuovi_decessi_average[-1]):,}\n"
                                                              f"Persone ospedalizzate oggi {int(ospedalizzati[-1]):,}\n"
                                                              f"Persone in TI oggi {int(TI[-1]):,}",ha='left',bbox=props)
#  plt.text(dateValues[-1]- datetime.timedelta(days=newICUshift+10),nuovi_TI_average[-1]*newICUDeaths*1.1,f"Nuove TI  in media {int(nuovi_TI_average[-1]):,}",ha='right',bbox=props)
#  plt.text(dateValues[-1]- datetime.timedelta(days=deathsShift+10),heightDeathBox,f"Nuovi decessi in media {int(nuovi_decessi_average[-1]):,}",ha='right',bbox=props)

  plt.axvline(datetime.date(2020,12,27),linewidth=1,color="k",linestyle="--",label="Inizio Vaccinazioni")
  #plt.axvline(datetime.date(2021,4,18),linewidth=1,color="k",linestyle="-.",label="Vaccinati l'80% di over80 con 1+ dose")
  #plt.axvline(datetime.date(2021,5,12),linewidth=1,color="k",linestyle="--",label="Vaccinati l'80% di over70 con 1+ dose")
  #plt.axvline(datetime.date(2021,6,3),linewidth=1,color="k",linestyle="-.",label="Vaccinati l'80% di over60 con 1+ dose")
  plt.axvline(datetime.date(2021,6,19),linewidth=1,color="k",linestyle="-.",label="Vaccinati l'80% di over50 con 1+ dose")

  xticksMy=[]
  for j in range(2020,2028):
    for k in range(1,13,2):
        xticksMy.append(datetime.date(j,k,1))

  formatter = mdates.DateFormatter("%m/%y")
  ax1.xaxis.set_major_formatter(formatter)
  ax1.set_xticks(xticksMy)
  yticksMy=[2,4,6,8,10,20,40,60,80,100,200,400,600,800,1000,2000,4000,5000]
  ax1.set_yticks(yticksMy)
  ax1.set_yticklabels([str(dig) for dig in yticksMy])

  plt.xlim([datetime.date(2020,8,15), dateValues[-1]+datetime.timedelta(days=10)])
  plt.ylim([1,minMax])
  plt.grid(True)
  plt.title("Covid-19 Italia (scala logaritmica) aggiornato al %d/%d/%d"%(lastDay.day,lastDay.month, lastDay.year))
  plt.text(datetime.date(2020,10,1),0.6,"Grafico di Davide Torlo - Fonte dati: Protezione Civile",
          horizontalalignment='left', verticalalignment='center',
          color=[0.3, 0.3,0.3])

  plt.legend(loc="lower left", framealpha=0.95)
  plt.tight_layout()
  filename="ospedalizzati.png"
  plt.savefig(filename)
  mesiItaliani=["gennaio","febbraio","marzo","aprile","maggio","giugno",
                "luglio","agosto","settembre","ottobre","novembre","dicembre"]
  todayDate=datetime.date.today()
  caption = f"Aggiornamento %d %s %d: dati COVID-19 in media mobile 7gg.\nLa versione interattiva è disponibile su accdavlo-covid-plots-global-app-et40f8.streamlitapp.com"%(lastDay.day,mesiItaliani[lastDay.month-1],lastDay.year)
  return caption, filename
