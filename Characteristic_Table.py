
"""
Program to create a csv with the characteristic of solar cells
"""
import os


DirectorioActual = os.getcwd()
ListaArchivos = os.listdir(DirectorioActual)   
outfile = open(DirectorioActual+'\\'+'PCEs.txt', 'w')
outfile.write("Time,Name,Cell,JSC (mA/cm2),VOC (V),FF (%),Maxim Power Point x cm2(mW/cm2),JSC CORRECTED (mA/cm2),Efficiency (%)\n")
outfile.close()
outfile = open(DirectorioActual+'\\'+'EQEs.txt', 'w')
outfile.write("Time,Name,Cell,Photocurrent (mA/cm2)\n")
outfile.close()




def readfiles(file,name):
    
    with open(file) as in_file, open(DirectorioActual+'\\'+'EQEs.txt', 'a') as EQE_file, open(DirectorioActual+'\\'+'PCEs.txt', 'a') as PCE_file:
       
       data = [temp.strip() for temp in in_file.readlines()[0:30]]
       
       date = data[0]
       
       if data[3] == 'Real Photocurrent (mA/cm2)': #EQE simulador cleanroom
            Photocurrents = data[4].split('\t')
            Photocurrents = [str(round(float(temp),2)) for temp in Photocurrents]
            Cell = 1
            for data in Photocurrents:
                EQE_file.write(date + ',' + name + ',' + str(Cell) + ',' + data + '\n')
                Cell += 1
                
       elif data[4] == 'Maxim Power Point x cm2(mW/cm2)': #IPCE simulador cleanroom
           MPP = data[5].split('\t')
           Voc = data[8].split('\t')
           Jsc = data[11].split('\t')
           FF = data[14].split('\t')
           Jscc = data[17].split('\t')
           EPCE = data[20].split('\t')
           
           Voc = [str(round(float(temp)/1000,3)) for temp in Voc]
           FF = [str(round(float(temp),1)) for temp in FF]
           EPCE = [str(round(float(temp),2)) for temp in EPCE]           
           MPP = [str(round(float(temp),2)) for temp in MPP]
           Jsc = [str(round(float(temp),2)) for temp in Jsc]
           Jscc = [str(round(float(temp),2)) for temp in Jscc]
           
           for cell in range(4):
               PCE_file.write(date + ',' + name + ','+ str(cell+1) + ',' + Jsc[cell] + ',' + Voc[cell] + ',' + FF[cell] + ',' + MPP[cell] + ',' + Jscc[cell] + ',' + EPCE[cell] + '\n')
       
       elif data[11] == 'Go:': #SS LED
           MPP = [data[16].split('=')[1]]
           Voc = [data[13].split('=')[1]]
           Jsc = [data[14].split('=')[1]]
           FF = [data[15].split('=')[1]]
           EPCE = [data[12].split('=')[1]]
           Area = [data[19].split('=')[1]]
           
           
           MPP.append(data[26].split('=')[1])
           Voc.append(data[23].split('=')[1])
           Jsc.append(data[24].split('=')[1])
           FF.append(data[25].split('=')[1])
           EPCE.append(data[22].split('=')[1])
           
           Jsc = [str(round(float(temp)/float(Area[0]),2)) for temp in Jsc]
           MPP = [str(round(float(temp)/float(Area[0]),2)) for temp in MPP]
           Voc = [str(round(float(temp),3)) for temp in Voc]
           FF = [str(round(float(temp),1)) for temp in FF]
           EPCE = [str(round(float(temp),2)) for temp in EPCE]
           
           
           PCE_file.write(date + ',' + name +'_forward' + ','+ 'NaN' + ',' + Jsc[0] + ',' + Voc[0] + ',' + FF[0] + ',' + MPP[0] + ',' + 'NaN' + ',' + EPCE[0] + '\n')
           PCE_file.write(date + ',' + name +'_backward' + ','+ 'NaN' + ',' + Jsc[1] + ',' + Voc[1] + ',' + FF[1] + ',' + MPP[1] + ',' + 'NaN' + ',' + EPCE[1] + '\n')    
 
       elif data[8] == 'Go:': #SS Xenon lamp
           MPP = [data[13].split('=')[1]]
           Voc = [data[10].split('=')[1]]
           Jsc = [data[11].split('=')[1]]
           FF = [data[12].split('=')[1]]
           EPCE = [data[9].split('=')[1]]
           Area = [data[16].split('=')[1]]
           
           
           MPP.append(data[23].split('=')[1])
           Voc.append(data[20].split('=')[1])
           Jsc.append(data[21].split('=')[1])
           FF.append(data[22].split('=')[1])
           EPCE.append(data[19].split('=')[1])
           
           Jsc = [str(round(float(temp)/float(Area[0]),2)) for temp in Jsc]
           MPP = [str(round(float(temp)/float(Area[0]),2)) for temp in MPP]
           Voc = [str(round(float(temp),3)) for temp in Voc]
           FF = [str(round(float(temp),1)) for temp in FF]
           EPCE = [str(round(float(temp),2)) for temp in EPCE]
           
           
           PCE_file.write(date + ',' + name +'_forward' + ','+ 'NaN' + ',' + Jsc[0] + ',' + Voc[0] + ',' + FF[0] + ',' + MPP[0] + ',' + 'NaN' + ',' + EPCE[0] + '\n')
           PCE_file.write(date + ',' + name +'_backward' + ','+ 'NaN' + ',' + Jsc[1] + ',' + Voc[1] + ',' + FF[1] + ',' + MPP[1] + ',' + 'NaN' + ',' + EPCE[1] + '\n')    

    
for i in range (len(ListaArchivos)):   #para todos los archivos donde se encuentre el programa

    readfiles(DirectorioActual+"\\"+ListaArchivos[i],ListaArchivos[i])
