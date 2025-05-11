"""

GenshinImpactWishSimulator
Made_By_kimx
2025/05/11

"""

from random import randint
import matplotlib.pyplot as plt
import numpy as np

#  FunctionDefinition

NumberOfTrial = 10000  # change the number if it takes longer
WishType = True  # True:Character,False:Weapons


class Wish:
    def __init__(self, NumberOfTrial: int, WishType: bool):
        self.NumberOfTrial = NumberOfTrial
        self.Constellation = 0
        self.WishTotallPull = 0
        self.SumTotalPull = 0
        self.MaxPull = 0
        self.MinPull = 0
        self.Temp = 0
        self.ResultList = []
        self.Lose = False
        if WishType:
            self.CaptureingRadiance = 0
            self.Rate = 0.6
            self.MaxConstellation = 7
            self.StartIncrease = 73
            self.IncreaseRate = 5.85
            self.PickRate = 0.5
        else:
            self.CaptureingRadiance = None
            self.Rate = 0.7
            self.MaxConstellation = 5
            self.StartIncrease = 62
            self.IncreaseRate = 5.52
            self.PickRate = 0.375

    def wish(self, Rate, WishTotallPull, StartIncrease, IncreaseRate):
        Wish = randint(0, 100000)
        if (
            Wish
            <= (Rate) * 1000
            - 1
            + max(0, WishTotallPull - StartIncrease) * 1000 * IncreaseRate
        ):
            return True
        else:
            return False

    def all_wish(self):
        for i in range(self.NumberOfTrial):
            while self.Constellation <= self.MaxConstellation:
                self.WishTotallPull += 1
                if not self.Lose:
                    if self.wish(
                        self.Rate,
                        self.WishTotallPull,
                        self.StartIncrease,
                        self.IncreaseRate,
                    ):
                        if (
                            self.CaptureingRadiance is not None
                            and self.CaptureingRadiance == 3
                        ):
                            self.Constellation += 1
                            self.WishTotallPull = 0
                        else:
                            if randint(0, 1000) <= self.PickRate * 1000:
                                self.Constellation += 1
                                self.WishTotallPull = 0
                                if self.CaptureingRadiance is not None:
                                    self.CaptureingRadiance = 0

                            else:
                                if self.CaptureingRadiance is not None:
                                    self.CaptureingRadiance += 1
                                self.Lose = True
                                self.WishTotallPull = 0

                    self.SumTotalPull += 1

                else:
                    if self.wish(
                        self.Rate,
                        self.WishTotallPull,
                        self.StartIncrease,
                        self.IncreaseRate,
                    ):
                        self.Constellation += 1
                        self.SumTotalPull += 1
                        self.WishTotallPull = 0

                    self.SumTotalPull += 1

            self.MaxPull = max(self.MaxPull, self.SumTotalPull - self.Temp)
            self.MinPull = min(self.MinPull, self.SumTotalPull - self.Temp)
            self.ResultList.append(self.SumTotalPull - self.Temp)
            self.Temp = self.SumTotalPull
            self.Constellation = 0
            self.Lose = False
        return self.ResultList, self.MaxPull, self.MinPull


class MakeGraph:
    def __init__(self):
        self.TotalPulList = []
        self.RateList = []

    def makegraph(self, MaxPull, MinPull, ResultList, WishType):
        for i in range(MinPull, MaxPull + 1):
            self.TotalPulList.append(i)

        for i in range(MinPull, MaxPull + 1):
            self.RateList.append(ResultList.count(i) / NumberOfTrial * 100)

        if WishType:
            plt.title("C6")
        else:
            plt.title("R5")

        plt.xlabel("Total Pull")
        plt.ylabel("Rate(%)")
        plt.bar(np.array(self.TotalPulList), np.array(self.RateList))
        plt.show()


if __name__ == "__main__":
    w = Wish(NumberOfTrial, WishType)
    ResultList, MaxPull, MinPull = w.all_wish()
    if WishType:
        print(
            f"C6 ave:{w.SumTotalPull / w.NumberOfTrial}primogem:{w.SumTotalPull / w.NumberOfTrial * 160}"
        )
    else:
        print(
            f"R5 ave:{w.SumTotalPull / w.NumberOfTrial}primogem:{w.SumTotalPull / w.NumberOfTrial * 160}"
        )
    g = MakeGraph()
    g.makegraph(MaxPull, MinPull, ResultList, WishType)
