def dpMakeChange(coinValueList,change,minCoins):
    
   for cents in range(change+1):

      coinCount = cents

      for j in [c for c in coinValueList if c <= cents]:

            if minCoins[cents-j] + 1 < coinCount:

               coinCount = minCoins[cents-j]+1

      minCoins[cents] = coinCount

   return minCoins[change]


def main():

    amnt = 72

    clist = [1,5,10,25,50]

    coinCount = [0]*(amnt+1)

    print(dpMakeChange(clist,amnt,coinCount),"moedas")



main()