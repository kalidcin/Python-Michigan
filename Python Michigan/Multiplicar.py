from multiprocessing import resource_tracker


num = int(input("Numero a multiplicar: "))
resultado = 0
for i in range(11):
    resultado = i*num
    if resultado != 0:
        print("{} x {} = {}".format(num, i, resultado))

