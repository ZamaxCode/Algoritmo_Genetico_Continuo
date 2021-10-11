from matplotlib import pyplot as plt
import numpy as np
import Functions
import AGC

def main():
    titulo = ""

    print("1.- Sphere")
    print("2.- Rosenbrock")
    print("3.- Rastrigin")
    print("4.- Quartic")
    opc = input("Seleccione que funcion desea realizar: ")

    if opc == "1":
        titulo = "Sphere"
        print("Ejecutando funcion Sphere")
        func = Functions.Sphere()

    elif opc == "2":
        titulo = "Rosenbrock"
        print("Ejecutando funcion Rosenbrock")
        func = Functions.Rosenbrock()

    elif opc == "3":
        titulo = "Rastrigin"
        print("Ejecutando funcion Rastrigin")
        func = Functions.Rastrigin()

    else:
        titulo = "Quartic"
        print("Ejecutando funcion Quartic")
        func = Functions.Quartic()

    dimension = 2
    promedios_matriz =[]
    x = np.arange(0, 2001, 100)

    while dimension<=8:
        mejores_matriz = []
        print(f"{dimension} dimensiones")
        for i in range(5):
            print(f"Ejecucion {i+1}")
            ag = AGC.AGC(64, dimension, 2000, 0.01, func, False)
            mejor_array = ag.run()
            mejores_matriz.append([abs(ele) for ele in mejor_array])

        promedio_mejores = np.mean(mejores_matriz, axis = 0)
        promedios_matriz.append(promedio_mejores)
        plt.plot(x,promedio_mejores)
        plt.title(f"{dimension} dimensiones")
        plt.show()
        dimension*=2

    for array in promedios_matriz:
        plt.plot(x,array)

    plt.title(titulo)
    plt.legend(["2 Dimensiones", "4 Dimensiones", "8 Dimensiones"])
    plt.show()

if __name__ == '__main__':
    main()
