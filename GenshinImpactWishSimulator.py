'''

GenshinImpactWishSimulator 
Made_By_kimx
2023/03/05

'''

from random import randint
import matplotlib.pyplot as plt
import numpy as np

#  FunctionDefinition

NumberOfTrial=10000 # change the number if it takes longer
WishType=True # True:Character,False:Weapons

Constellation =0
WishTotallPull=0
AllSumTotalPull=0
SumTotalPull=0
NotPu=True
MaxPull=0
MinPull=0
Temp=0

ResultList=[]


def CharactarWish(NumberOfTrial,Constellation,WishTotallPull,SumTotalPull,NotPu,MaxPull,MinPull,Temp,WishType):

    for i in range(NumberOfTrial):
    
        while Constellation < 8:

            WishTotallPull += 1
            Wish = randint(0 , 100000)

            if NotPu:

                if Wish <= 599 + max (0,WishTotallPull-73) * 6000:
                    #  50:50
                    if randint(0,1) == 1:

                        Constellation += 1
                        SumTotalPull += 1
                        WishTotallPull = 0

                    else:

                        NotPu=False
                        SumTotalPull +=1
                        WishTotallPull = 0

                else:
                    SumTotalPull += 1

            else:

                if Wish <= 599 + max(0,WishTotallPull-73) * 6000:

                    NotPu = True
                    Constellation += 1
                    SumTotalPull += 1
                    WishTotallPull = 0

                else:
                
                    SumTotalPull+=1
    
        MaxPull=max(MaxPull,SumTotalPull-Temp)
        MinPull=min(MinPull,SumTotalPull-Temp)

        ResultList.append(SumTotalPull-Temp) #Get the value of pulling the Wish
        Temp=SumTotalPull

        Constellation=0

    print(f"6C ave:{SumTotalPull/NumberOfTrial}primogem:{SumTotalPull/NumberOfTrial*160}")
    print(f"1C ave:{SumTotalPull/NumberOfTrial/7}primogem:{SumTotalPull/NumberOfTrial*160/7}")

    MakeGraph(MaxPull,MinPull,ResultList,WishType)

def WeaponWish(NumberOfTrial,Constellation,WishTotallPull,SumTotalPull,NotPu,MaxPull,MinPull,Temp,WishType):

    NotPu2=True

    for i in range(NumberOfTrial):
    
        while Constellation < 6:

            WishTotallPull += 1
            Wish = randint(0 , 100000)

            if NotPu and NotPu2:

                if Wish <= 699 + max (0,WishTotallPull-62) * 7000:
                    #  27.5%
                    if randint(0,7) <= 2:

                        Constellation += 1
                        SumTotalPull += 1
                        WishTotallPull = 0

                    else:

                        NotPu2=False
                        SumTotalPull +=1
                        WishTotallPull = 0

                else:
                    SumTotalPull += 1

            elif NotPu:
                    if Wish <= 699 + max (0,WishTotallPull-62) * 7000:
                    #  50:50
                        if randint(0,1) == 1:
                            NotPu=True
                            Constellation += 1
                            SumTotalPull += 1
                            WishTotallPull = 0

                        else:

                            NotPu=False
                            SumTotalPull +=1
                            WishTotallPull = 0

                    else:
                        SumTotalPull += 1

            else:

                if Wish <= 699 + max(0,WishTotallPull-73) * 7000:

                    NotPu = True
                    NotPu2  = True
                    Constellation += 1
                    SumTotalPull += 1
                    WishTotallPull = 0

                else:
                
                    SumTotalPull+=1

        MaxPull=max(MaxPull,SumTotalPull-Temp)
        MinPull=min(MinPull,SumTotalPull-Temp)

        ResultList.append(SumTotalPull-Temp) #Get the value of pulling the Wish
        Temp=SumTotalPull

        Constellation=0

    print(f"R5 ave:{SumTotalPull/NumberOfTrial}primogem:{SumTotalPull/NumberOfTrial*160}")
    print(f"R1 ave:{SumTotalPull/NumberOfTrial/5}primogem:{SumTotalPull/NumberOfTrial*160/5}")

    MakeGraph(MaxPull,MinPull,ResultList,WishType)


def MakeGraph(MaxPull,MinPull,ResultList,WishType):

    TotalPulList = []
    RateList = []

    for i in range(MinPull,MaxPull+1):
        TotalPulList.append(i)

    for i in range(MinPull,MaxPull+1):
        RateList.append(ResultList.count(i)/NumberOfTrial*100)

    if WishType:
        plt.title("6C")
    else:
        plt.title("R5")
        
    plt.xlabel('Total Pull')
    plt.ylabel('Rate(%)')
    plt.bar(np.array(TotalPulList),np.array(RateList))
    plt.show()

if __name__ == "__main__":
    
    if WishType:
        CharactarWish(NumberOfTrial,Constellation,WishTotallPull,SumTotalPull,NotPu,MaxPull,MinPull,Temp,WishType)
    else:
        WeaponWish(NumberOfTrial,Constellation,WishTotallPull,SumTotalPull,NotPu,MaxPull,MinPull,Temp,WishType)

