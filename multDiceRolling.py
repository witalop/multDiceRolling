from itertools import product
import matplotlib.pyplot as plt

def multDiceRolling(numberOfDices, numberOfSides):
    listSides = [i for i in range(numberOfSides +1)]
    del(listSides[0])
    listCombinations = list(product(listSides, repeat = numberOfDices))

    probDict = {}
    porcentEachResult = 100/len(listCombinations)
    for i in listCombinations:
        if str(sum(i)) in probDict:
            probDict[str(sum(i))] += porcentEachResult
        else:
            probDict[str(sum(i))] = porcentEachResult
    
    return probDict


if __name__ == "__main__":
    probDictD6=multDiceRolling(4,6)
    probDictD8=multDiceRolling(3,8)

    resultsD6 = list(probDictD6.keys())
    percentagesD6 = list(probDictD6.values())
    resultsD8 = list(probDictD8.keys())
    percentagesD8 = list(probDictD8.values())
    
    plt.plot(resultsD8, percentagesD8, color='blue', label='D8')
    plt.plot(resultsD6, percentagesD6, color='red', label='D6')
    plt.ylim(0, 12)
    plt.title('3xD8 vs 4xD6')
    plt.xlabel('Resultados')
    plt.ylabel('Probabilidade')
    plt.legend()
    plt.show()
