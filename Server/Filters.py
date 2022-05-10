import re

input_file = open("./Results/CrawlerResults.txt", encoding="utf-8", errors='ignore')
input_text = input_file.read()
input_file.close()





# |||||||||||||||||||||||||||||||||||||||||||||| FILTRUL 0 - Prețuri ||||||||||||||||||||||||||||||||||||||||||||||

price_filter = r"(\b\d+([., ]\d+)?)(?=( ?(lei|ron|bani)))"
prices = re.findall(price_filter, input_text, re.I)

# conventie: < primul numar, <= al doilea numar
from0to10, from10to50, from50to250, from250to1000, from1000to5000, from5000to15000, above15000 = 0, 0, 0, 0, 0, 0, 0

for i in range(len(prices)):
    price = prices[i][0].replace(' ', '')  # pentru preturi mari (14 000 lei)
    price = price.replace(',', '.')        # pentru preturi care nu sunt intregi (2,5 lei)
    if len(prices[i][1]) == 4:             # pentru preturi mari ca la #1 (14.000 lei)
        price = price.replace('.', '')
    price = float(price)
    
    if price < 10:
        from0to10 += 1
    elif price < 50:
        from10to50 += 1
    elif price < 250:
        from50to250 += 1
    elif price < 1000:
        from250to1000 += 1
    elif price < 5000:
        from1000to5000 += 1
    elif price < 15000:
        from5000to15000 += 1
    else:
        above15000 += 1
   

result0 = open("./Results/filter0.txt", "w", encoding="utf-8")

result0.write(f"Între 0 și 10 RON: {from0to10}\n")
result0.write(f"Între 10 și 50 RON: {from10to50}\n")
result0.write(f"Între 50 și 250 RON: {from50to250}\n")
result0.write(f"Între 250 și 1000 RON: {from250to1000}\n")
result0.write(f"Între 1000 și 5000 RON: {from1000to5000}\n")
result0.write(f"Între 5000 și 15000 RON: {from5000to15000}\n")
result0.write(f"Peste 15000 RON: {above15000}")

result0.close() 





# |||||||||||||||||||||||||||||||||||||||||||||| FILTRUL 1 - Stare produse ||||||||||||||||||||||||||||||||||||||||||||||

state_filter = r"(?<=stare)(?:(?: de func[tț]ionare)? (?:(f(?:oarte)? bun[aă])|(bun[aă])|(perfect[aă])|(nou[aă])|(excep[tț]ional[aă])))"
states = re.findall(state_filter, input_text, re.I)


fbuna , buna, perfecta, noua, exceptionala = 0, 0, 0, 0, 0

for state in states:
    if state[0]:
        fbuna += 1
    elif state[1]:
        buna += 1
    elif state[2]:
        perfecta += 1
    elif state[3]:
        noua += 1
    elif state[4]:
        exceptionala += 1


result1 = open("./Results/filter1.txt", "w", encoding="utf-8")

result1.write(f"Foarte bună: {fbuna}\n")
result1.write(f"Bună: {buna}\n")
result1.write(f"Perfectă: {perfecta}\n")
result1.write(f"Nouă: {noua}\n")
result1.write(f"Excepțională: {exceptionala}")

result1.close() 





# |||||||||||||||||||||||||||||||||||||||||||||| FILTRUL 2 - Materiale ||||||||||||||||||||||||||||||||||||||||||||||

materials_filter = r"(metal(?:ic[eaă]?)?)|(\bfi?er\b)|(\bo[țt]el\b)|(aluminiu)|(inox\b)|(cupru)|(\blemn)|(piele)"
materials = re.findall(materials_filter, input_text, re.I)


metal, fier, otel, aluminiu, inox, cupru, lemn, piele = 0, 0, 0, 0, 0, 0, 0, 0

for material in materials:
    if material[0]:
        metal += 1 
    elif material[1]:
        fier += 1 
    elif material[2]:
        otel += 1
    elif material[3]:
        aluminiu += 1
    elif material[4]:
        inox += 1
    elif material[5]:
        cupru += 1
    elif material[6]:
        lemn += 1
    elif material[7]:
        piele += 1


result2 = open("./Results/filter2.txt", "w", encoding="utf-8")

result2.write(f"Metal: {metal}\n")
result2.write(f"Fier: {fier}\n")
result2.write(f"Oțel: {otel}\n")
result2.write(f"Aluminiu: {aluminiu}\n")
result2.write(f"Inox: {inox}\n")
result2.write(f"Cupru: {cupru}\n")
result2.write(f"Lemn: {lemn}\n")
result2.write(f"Piele: {piele}")

result2.close() 





# |||||||||||||||||||||||||||||||||||||||||||||| FILTRUL 3 - Firme ||||||||||||||||||||||||||||||||||||||||||||||

companies_filter = r"(bosch)|(makita)|(ingco)|(hilti)|(stanley)|(stihl)"
companies = re.findall(companies_filter, input_text, re.I)

bosch, makita, ingco, hilti, stanley, stihl = 0, 0, 0, 0, 0, 0

for company in companies:
    if company[0]:
        bosch += 1
    elif company[1]:
        makita += 1
    elif company[2]:
        ingco += 1
    elif company[3]:
        hilti += 1
    elif company[4]:
        stanley += 1
    elif company[5]:
        stanley += 1

result3 = open("./Results/filter3.txt", "w", encoding="utf-8")

result3.write(f"Bosch: {bosch}\n")
result3.write(f"Makita: {makita}\n")
result3.write(f"Ingco: {ingco}\n")
result3.write(f"Hilti: {hilti}\n")
result3.write(f"Stanley: {stanley}\n")
result3.write(f"Stihl: {stihl}")

result3.close()     





# |||||||||||||||||||||||||||||||||||||||||||||| FILTRUL 4 - Modalitate de livrare ||||||||||||||||||||||||||||||||||||||||||||||

delivery_filter = r"(\b(?:(?:(?:ridic[aă])|(?:pred[aă]))(?:re)?(?: personal(?:[aă])?)?)\b)|(co?urier(?:at)?)|(po[sș]t[aă])"
deliveries = re.findall(delivery_filter, input_text, re.I)

ridicare, curierat, posta = 0, 0, 0

for delivery in deliveries:
    if delivery[0]:
        ridicare += 1
    elif delivery[1]:
        curierat += 1
    elif delivery[2]:
        posta += 1

result4 = open("./Results/filter4.txt", "w", encoding="utf-8")

result4.write(f"Curierat: {curierat}\n")
result4.write(f"Poștă: {posta}\n")
result4.write(f"Ridicare personală: {ridicare}")

result4.close() 





# |||||||||||||||||||||||||||||||||||||||||||||| FILTRUL 5 - Mobilă (pe camere) ||||||||||||||||||||||||||||||||||||||||||||||

furniture_filter = r"(?:(?<=mobil[aă])|(?<=mobilier)) \w* ?(?:((?:sufragerie)|(?:living))|(dormitor)|(buc[aă]t[aă]rie)|(baie)|(hol)|(teras[aă]))"
furnitureItems = re.findall(furniture_filter, input_text, re.I)

living, dormitor, bucatarie, baie, hol, terasa = 0, 0, 0, 0, 0, 0

for furniture in furnitureItems:
    if furniture[0]:
        living += 1
    elif furniture[1]:
        dormitor += 1
    elif furniture[2]:
        bucatarie += 1
    elif furniture[3]:
        baie += 1
    elif furniture[4]:
        hol += 1
    elif furniture[5]:
        terasa += 1

result5 = open("./Results/filter5.txt", "w", encoding="utf-8")

result5.write(f"Sufragerie: {living}\n")
result5.write(f"Dormitor: {dormitor}\n")
result5.write(f"Bucătărie: {bucatarie}\n")
result5.write(f"Baie: {baie}\n")
result5.write(f"Hol: {hol}\n")
result5.write(f"Terasă: {terasa}")

result5.close()




# |||||||||||||||||||||||||||||||||||||||||||||| FILTRUL 6 - Piese de mobilier ||||||||||||||||||||||||||||||||||||||||||||||

furniture2_filter = r"(\bpat(?:uri)?\b)|(canape(?:(?:a)|(?:le)))|(fotoli[iu])|(dulap(?:uri)?\b)|(sc[aă]un(?:el?)?)"
furniture2Items = re.findall(furniture2_filter, input_text, re.I)

pat, canapea, fotoliu, dulap, scaun = 0, 0, 0, 0, 0

for furniture2 in furniture2Items:
    if  furniture2[0]:
        pat += 1
    elif furniture2[1]:
        canapea += 1
    elif furniture2[2]:
        fotoliu += 1
    elif furniture2[3]:
        dulap += 1
    elif furniture2[4]:
        scaun += 1

result6 = open("./Results/filter6.txt", "w", encoding="utf-8")

result6.write(f"Paturi: {pat}\n")
result6.write(f"Canapele: {canapea}\n")
result6.write(f"Fotolii: {fotoliu}\n")
result6.write(f"Dulapuri: {dulap}\n")
result6.write(f"Scaune: {scaun}")

result6.close()





# |||||||||||||||||||||||||||||||||||||||||||||| FILTRUL 7 - Beneficii ||||||||||||||||||||||||||||||||||||||||||||||

benefits_filter = r"(\bfactur[aăi])|(garan[tț]ie)|(livrarea?)"
benefits = re.findall(benefits_filter, input_text, re.I)

factura, garantie, livrare = 0, 0, 0

for benefit in benefits:
    if benefit[0]:
        factura += 1
    elif benefit[1]:
        garantie += 1
    elif benefit[2]:
        livrare += 1

result7 = open("./Results/filter7.txt", "w", encoding="utf-8")

result7.write(f"Cu emitere de factura: {factura}\n")
result7.write(f"Cu garanție: {garantie}\n")
result7.write(f"Cu livrare asigurată: {livrare}")

result7.close()





# |||||||||||||||||||||||||||||||||||||||||||||| FILTRUL 8 - Flori ||||||||||||||||||||||||||||||||||||||||||||||

flowers_filter = r"(trandafiri?)|(lalea?(?:le)?)|(orhide[ei])|(bujori?)|(mu[sș]cat[aăe])"
flowers = re.findall(flowers_filter, input_text, re.I)

trandafiri, lalele, orhidee, bujori, muscate = 0, 0, 0, 0, 0

for flower in flowers:
    if flower[0]:
        trandafiri += 1
    elif flower[1]:
        lalele += 1
    elif flower[2]:
        orhidee += 1
    elif flower[3]:
        bujori += 1
    elif flower[4]:
        muscate += 1

result8 = open("./Results/filter8.txt", "w", encoding="utf-8")

result8.write(f"Trandafiri: {trandafiri}\n")
result8.write(f"Lalele: {lalele}\n")
result8.write(f"Orhidee: {orhidee}\n")
result8.write(f"Bujori: {lalele}\n")
result8.write(f"Mușcate: {muscate}")

result8.close()





# |||||||||||||||||||||||||||||||||||||||||||||| FILTRUL 9 - Unelte ||||||||||||||||||||||||||||||||||||||||||||||

tools_filter = r"(drujb[aă])|(fier[aă]str[aă]u)|(borma[sș]in[aă])|(burghiu)|(ciocan\b)|(\bflex\b)"
tools = re.findall(tools_filter, input_text, re.I)

drujba, fierastrau, bormasina, burghiu, ciocan, flex = 0, 0, 0, 0, 0, 0

for tool in tools:
    if tool[0]:
        drujba += 1
    elif tool[1]:
        fierastrau += 1
    elif tool[2]:
        bormasina += 1
    elif tool[3]:
        burghiu += 1
    elif tool[4]:
        ciocan += 1
    elif tool[5]:
        flex += 1

result9 = open("./Results/filter9.txt", "w", encoding="utf-8")

result9.write(f"Drujbe: {drujba}\n")
result9.write(f"Fierăstraie: {fierastrau}\n")
result9.write(f"Bormașini: {bormasina}\n")
result9.write(f"Burghie: {burghiu}\n")
result9.write(f"Ciocane: {ciocan}\n")
result9.write(f"Flexuri: {flex}")

result9.close()
