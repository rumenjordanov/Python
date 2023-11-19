duljina = int(input())
shirochina = int(input())
visochina = int(input())
procent_zaeto_prostranstvo = int(input())

obem = duljina * shirochina * visochina
obem_litri = obem * 0.001

zaeto_prostranstvo = procent_zaeto_prostranstvo / 100

litri = obem_litri * (1-0.17)

print(litri)

