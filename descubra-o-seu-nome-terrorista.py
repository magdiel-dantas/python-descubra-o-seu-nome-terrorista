meses = {
"janeiro": "Zumbi",
'fevereiro': "Assassino",
'março': "Psicopata",
'abril': "Alienigena",
'maio': "Carniceiro",
'junho': "Matador",
'julho': "Vampiro",
'agosto': "Maluco",
'setembro': "Vingador",
'outubro': "Mostro",
'novembro': "Bruxo",
'dezembro': "Demônio",
    }
 
dias = {
"1": "Endiabrado",
"2": "Radioativo",
"3": "Endemoniado",
"4": "Vermelho",
"5": "Possuido",
"6": "Macabro",
"7": "Negro",
"8": "Sem cabeça",
"9": "Desconhecido",
"10": "Inconciente",
"11": "Oculto",
"12": "Esquecido",
"13": "Obscuro",
"14": "Invocado",
"15": "Caído",
"16": "Costurado",
"17": "Almadiçoado",
"18": "Anormal",
"19": "Pertubado",
"20": "Tenebrese",
"21": "Sanguinario",
"22": "Tenebroso",
"23": "Imortal",
"24": "Ressucitado",
"25": "do Pantano",
"26": "da Encruzilhada",
"27": "do Porão",
"28": "do Velho Poço",
"29": "do cemiterio",
"30": "da meia lua",
"31": "da lua cheia",
    }
 
mes = raw_input("Digite o mês em que você nasceu: ")
dia = raw_input("Digite o dia do seu nascimento: ")
 
mes.lower()
 
print "Seu nome terrorista é : " +  meses[mes] +" "+ dias[dia]
