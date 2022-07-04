##print(data.iloc[6,170]) #specific index of column and row
##for index, row in data.iterrows():
import re
import pandas as pd

#path = r"C:\Users\Jouni Kinnunen\Documents\Python Scripts\Master data_työversio 1.xlsx" # full list
#path = r"E:\koodit\Git\Mpmp.xlsx" #testilista
path = r"E:\koodit\Git\Master data_työversio_din_iso.xlsx" #worklist

col_list = ["Item No.", "Item description (local 1)","Specification (local 2)","Part Description","Item Group",
            "Part Description Spec","MrtlSubGroup","Cert Purchase Doc Description","Item type 1"]

data = pd.read_excel(path, usecols=col_list)

data['MrtlSubGroup'] = data['MrtlSubGroup'].str.replace('/','|')
data['MrtlSubGroup'] = data['MrtlSubGroup'].str.replace('Steel other with lead content <0,1%','|')
data['Item type 1'] = data['Item type 1'].str.replace(r'Geomet, Geoblack,Delta, Magni \(Zinc Flak','')
data['MrtlSubGroup'] = data['MrtlSubGroup'].str.replace(r'Steel 4\.6-6\.8 \(4-6\)',r'Steel 4\|6-6\|8 \(4-6\)')
data['Specification (local 2)'] = data['Specification (local 2)'].str.replace(r'\xB5',r'MY')

global otsikot #tiedoston otsikoiden määrä
otsikot = len(data.columns)
indexi = data.index
print("otsikkojen maara=",otsikot)
rivit = len(indexi) #tiedoston rivimäärä
print("rivien maara=",rivit)
linsainfo_index = otsikot + 1


#iso taulut sisältävät vain 4 ja 5 kirjaimiset koodit
#din taulut sisältävät vain 3 ja 4 kirjaimiset koodit


taul_en = ['14399']
taul_iso = ['2339','2338','1207','1580','1234','7089','7090','7091',
            '8737','7435','2342','7092','7436','4036','4035','8675',
            '7094','4766','7434','4034','4018','4016','8677','8678',
            '2936','4762','4026','4027','4028','4029','4014','4017',
            '4032','4033','7035','7036','7037','7038','8765','8676',
            '2009','2010','7046','7047','8673','8674','7042','7719',
            '7040','8738','2340','2341','8739','8744','8745','8740',
            '8741','8742','8752','8734','2491','3912','7411','7412',
            '4775','7413','7414','7415','8102','4162','4161','7041',
            '7043','7044','7053','8750','8751','8748','1481','1482',
            '1483','8736','8733','8735','7049','7050','7051',
            '7045','7093','7046',"1581","7048","7379","7380"]
taul_iso2 = ['21269','10513','10512','10669','10673','12125','12126',
            '10509','13337','15480','15481','15482','15483','10642',
            '13918','14579','10511','10642','14580','14586',
            '14581','14583',"14584","14585",'15071']
taul_iso3 = []
taul_din = ['134','124','125','126','127','128','258','417','427','433','438','439','440',
            '551','553','555','558',"653","660",'601','603','911','912','913',
            '914','915','916','931','933','934','935','936','937','137',
            '960','961','963','964','965','966','970','971','972',
            '980','982','985','186','261','976',"314","315","316",
            "436","443","444","463","464","466","467","470","471",
            "472","508","318","557","561","562","564","571","580",
            "582","604","605","608","609","610","763","787","835",
            "741","172","522","529","661","705","939","939","928",
            "923","929","968","975","988"]
taul_din2 = ['1440','1443','1444','1446','1470','1471','1472','1473','1474',
            '1475','1481',"6336","6334","6340","6796","6797","6798",
            '6799','6325',"6880",'6885','6886','6887','6888',
            '6902','6903','6904','6905','6906','6907','6908','6914',
            '6915','6916','6921','6922','6923','6924','6925','6926',
            '6927','6928','7343','7344','7346','7504','7971','7972',
            '7973','7976','7977','7978','7979','7981','7982','7983',
            '7985','7991','9021','2093','1434','1441','1592','1593',
            '1804','2510',"1476","1478","1479","1480","1587","6331"
            "2990","2991","3017","3404","3567","3570","5406","6330",
            "7603","7604","7964","7967","7968","7980","7984","7990",
            "7993","7995","7996","7997","3760","7989","7340","7500",
            "6899","7337","7513","5401","6319","6332","6912","7349"]
taul_din3 = ['15058','15237','16903',"15058","46234","82101","11024",'11023',
            "71412","71752"]

taul_material = ['UC6S',"BRASS","messinki","TOL","ACIER","MS","POLYAMIDE","POLYAM.",
                "polyamid","PA","POLYAM"]
taul_kovuus = ['NR',"PTFE","johdin",'GT','F6S','clevis pin',
            "U6M","1/2","1/2\"","1/8","1/4","5/8","7/8","1\\.4547",
            "4\\.6","4\\.8","5\\.2","5\\.6","5\\.8","6\\.0","6\\.3","6\\.6","8\\.8",
            "12\\.9","10\\.9","1/4","3/4","9/16",
            "1\\.1181","1\\.4401","1\\.4404","1\\.4410","1\\.4305","1\\.4462","3\\.7035",
            "3/8","7/16","CL10","CL\\.10","CL\\.8","CL\\.6","CL\\.12","C35E","CL\\.5","ANSI"
            ,"B18.2.2","B18.22.2","B18.2.1","B18.21.1","B18.3","B18.3\"","B18.17"]
taul_a = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10",
        "A11","A12","A13","A14","A15","A16","A17","A22","A30","A32","A34","A36","A38","A46","A52","A64","A82","A94","A45",
        "A60","A2-50","A2-70",
        "A2-80","A2-100","A4-50","A4-70","A4-80","A4-100"]
taul_m = ["H6","M1","M1,6","M1\\.6","M2","M2,3",
        "M2\\.3","M2,5","M2\\.5","M2,6","M2\\.6",
        "M3","M3,5","M3\\.5","M4","M4,5","M4\\.5","M5","M6","M7",
        "M8","M9","M10","M11","M12","M13","M14","M15","M16",
        "M17","M18","M19","M20","M21","M22","M23","M24","M25",
        "M26","M27","M28","M29","M30","M31","M32","M33","M34",
        "M35","M36","M37","M38","M39","M40","M41","M42","M43",
        "M44","M45","M46","M47","M48","M49","M50","M51","M52",
        "M53","M54","M55","M56","M57","M58","M59","M60","M61",
        "M62","M63","M64","M65","M66","M67","M68","M69","M70",
        "M71","M72","M73","M74","M75","M76","M77","M78","M79",
        "M80","M81","M82","M83","M84","M85","M86","M87","M88",
        "M89","M90","M100","kw",'h6','h8','h9','h10']
taul_colors = ["KERB","POZ","PZ","VH301GZ","C45","C15E","C15","FZB","BODYCOTE","SMO254","Moventa","Grade A","bronze","SANTOPRENE","YELLOW","YELLOWZPL","YELL","musta","black","harmaa","grey","punainen","pun","red","sininen",
            "siniharmaa","silver","ZPL","ZPL\\.","ZN-NI","ZNNI","ZNC","ZINK-IRON","ZINCP","ZINC\\.PL",
            "znk","sinkitty","zincfl","ZINCNICKEL","ZINCPLATED","kuuma","KUUMASINKITTY","alum","geo","geomet","500b",
            "ZINCPL","torx","CSK","100 HV","100HV","HV100","HV 100","HV140","HV 140","140HV","140 HV","-140HV","HV200","HV 200","200HV","200 HV",
            "-200HV","HV300","HV 300","300HV","300 HV","-300HV","HB200","HB 200","200HB","200 HB","HB250",
            "HB 250","250HB","250 HB","HB300","HB 300","300HB","300 HB","MPS","MP","NIKLATTU","NICKELPL","nickel",
            "DEL","CU","kopper","copperpl","KUPAROITU","DACRO","DACRO\\.","DAC","DACROMET","nylon","Messinki","delta",
            "del","SAF2205","HDG","36CrNiMo4","22CRMOV12","24CrMo5","25CrMo4","42CRMO4","21CRMOV57","40CRMOV47","21CRMO57","SINKKINIKKELI","ZINC PLATED",
            "ZINK FLAKE","ZINCFL","FLZNNC","flZn/nc","mustapass","BLACK","OXIDE","GLEITMO",
            "BLACKCHROME","ZN/FE","ZINC-IRON","GEO500","ZINKFLAKE","BLACK+","H\\.D\\.G","H\\.D\\.G,","kl100","DELTAKL100","FE/ZN-NI",
            "ZINCPL\\.","left","vasen","HOT DIP","FOSFATED","FOSF\\.","IRON","ASTM","TITAN","zing","No6","No8","No10","UNC","UNF","TOP COAT","TOP","TOPCOAT",
            "wax","waxed","BUMAX 88","BUMAX88","BUMAX 109","BUMAX109","NICKIEL","transparent","tran","TRANSP","HOT","DIP","Galvanizing","H\\.D\\.G","kuumazn","GALVANIZED","H\\.D\\.G\\.",
            "DIPP","GALV","GAL\\.","ZINC FLAKE","Flake","Silv","RAUTA","passi","delt","GEO5B","DRI-LOCK","DRI-LOC","DRILOCK","tuflok","Nordlock","znfl",
            "SINKKI-NIKKELI","ZNPL","NIKKELI","sink","zinc","VAHATTU","PLTD","zn","ZP","6az","QT","240h","480h","500h","720h","cer","SDX109",
            "nitro","LDX","SDX","HDX","ULTRA","HEP","HARD","Special","PLASTIC","bner","nerinox","mech","MEK\\.","F105","BROWN","gr2","WHITE","ORANGE","MEC\\.","zib","SVART",'316',"aisi",
            "HOLO-CHROME","PRECOTE 80","TAPTITE","sealer","duplex","VAXADE","S235JR"]

skip_match = ['zn','mp','mps','zp','tx','cu','c15','gt','316','nr','ansi',"pz","poz","kerb"]

taul_gleitmo = ["720","627","625","605","603","1:5"]
taul_hv = ["100","200","140","300"]
taul_oxide = ["OXIDE"]
flake_lopulliset = ["FLZNNC","FLZN"]
taul_flake_kesto = ["240h","480h","720h"]
taul_zinc = ["zinc","zincp","zinc\\.pl","zincfl","zincplated","zincpl","zincpl\\.","zing","znc","sink","znk","sinkitty","ZPL\\.",
            "ZNPL","zn","zp","PLTD","ZPL"]
taul_feznni = ["FE/ZN-NI"]
taul_znni = ["ZN-NI","ZINCNICKEL","ZNNI","SINKKI-NIKKELI","SINKKINIKKELI"]
taul_nickel = ["NICKELPL","nickel","NICKIEL","NIKKELI","NIKLATTU"]
taul_zinc_iron = ["ZINK-IRON","ZINC-IRON","ZN/FE","FZB","ZIB"]
taul_iron = ["iron","RAUTA"]
taul_topc = ["TOP COAT","TOP","TOPCOAT"]
taul_pass = ["passi","mp","mps"]
taul_waxed = ["wax","waxed","VAHATTU","VAXADE"]
taul_tran = ["transparent","tran","TRANSP"]
taul_hdg =["HDG","GAL\\.","HOT","DIP","Galvanizing","H\\.D\\.G","H\\.D\\.G\\.","HOT DIP","kuuma","KUUMASINKITTY","kuumazn","GALVANIZED","DIPP","GALV"]
taul_flake = ["ZINKFLAKE","ZINK FLAKE","ZINC FLAKE","Flake","FLZN","znfl","ZINCFL","zinkflake"]
taul_flakenc = ["FLZNNC","flZn/nc"]
taul_geo = ["geo","geomet"]
taul_geo500b = ["geo500b","500b","GEO5B"]
taul_delta = ["delta","del","delt","deltakl100","kl100"]
taul_poly = ["POLYAMIDE","POLYAM\\.","polyamid","PA","POLYAM","POLYAM."]
taul_black = ["Black","musta","Musta","BLACK+","BLAC","SVART"]
taul_silver = ["Silver","Harmaa","grey","Silv"]
taul_yellow = ["YELLOW","YELL"]

def generate_others(a): ## Ohjelma etsii arvoja: HDG, geo, delta,TX, polyamide, HV(ei etsi "xxx HV")
    HDG = False
    geo = False
    delta = False
    silver = False
    black = False
    poly = False
    oxide = False

    poly_index = 2
    text_string = a.split()
    ii = len(text_string)

#    for i in text_string:
#        if i.casefold() == 'TX':
#            text_string.append('TORX')
#            text_string.pop(text_string.index(i))
#            break
    
    for i in text_string:

        if len(i) > 1:

            if i.casefold() == 'HV'.casefold() and text_string.index(i) +1 < ii:

                for j in taul_hv:
                    if text_string[text_string.index(i)+1] == j:

                        text_string.append('HV'+j)
                        text_string.pop(text_string.index(i)+1)
                        text_string.pop(text_string.index(i))
                        ii -= 1

                        break
            elif i[len(i) - 2:].casefold() == 'HV'.casefold():
                for j in taul_hv:

                    if i[0:3] == j:

                        text_string[text_string.index(i)] = 'HV'+i[0:3]

                        break
                    elif text_string[text_string.index(i)-1] == j:
                  

                        text_string.append('HV'+j)

                        text_string.pop(text_string.index(i)-1)

                        text_string.pop(text_string.index(i))

                        
                        ii -= 1
                        break

            else:
                pass

    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_oxide) > j:    
            if text_string[i].casefold() == taul_oxide[j].casefold():
                oxide = True
#                print("Match loydetty=",text_string[i],taul_hdg[j])
                text_string.pop(i)
                i -= 1
            j += 1
        i += 1

    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_poly) > j:    
            if text_string[i].casefold() == taul_poly[j].casefold():
                poly = True
#                print("Match loydetty=",text_string[i],taul_hdg[j])
                text_string.pop(i)
                i -= 1
            j += 1
        i += 1

    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_hdg) > j:    
            if text_string[i].casefold() == taul_hdg[j].casefold():
                HDG = True
#                print("Match loydetty=",text_string[i],taul_hdg[j])
                text_string.pop(i)
                i -= 1
            j += 1
        i += 1
    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_delta) > j:    
            if text_string[i].casefold() == taul_delta[j].casefold():
                delta = True
#                print("Match loydetty=",text_string[i],taul_delta[j])
                text_string.pop(i)
                i -= 1
            j += 1
        i += 1
    
    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_black) > j:    
            if text_string[i].casefold() == taul_black[j].casefold():
                black = True
#                print("Match loydetty=",text_string[i],taul_black[j])
                text_string.pop(i)
                i -= 1
            j += 1
        i += 1
    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_silver) > j:    
            if text_string[i].casefold() == taul_silver[j].casefold():
                silver = True
                text_string.pop(i)
                i -= 1
            j += 1
        i += 1
    if poly:
        text_string.insert(poly_index,'PA')
    if HDG:
        text_string.append('HDG ISO-FIT')
        for i in text_string: #Jos arvo ZN, poista riviltä ja korvaa hdg
            if i.casefold() == 'ZN'.casefold():
                text_string.pop(text_string.index(i))
#                print(text_string)
                
    if delta:
        if black:
            text_string.append('DELT')
            text_string.append('BL')
            return " ".join(list(dict.fromkeys(text_string)))
        if silver:
            text_string.append('DELT')
            text_string.append('SI')
            return " ".join(list(dict.fromkeys(text_string)))
        text_string.append('DELTA')
        return " ".join(list(dict.fromkeys(text_string)))
    
    if black:
#        if oxide:
#            text_string.append('BL OXIDE')
        text_string.append('Black')    
    if silver:
        text_string.append('SILVER')

    return " ".join(list(dict.fromkeys(text_string)))
    
def generate_zinc(a): ## Ohjelma etsii stringistä arvoja sinkistä josta lopullinen sinkin nimi rakentuu
    zinc = False
    nickel = False
    iron = False
    TOPC = False
    waxed = False
    tran = False
    flake = False
    passivated = False
    yellow = False
    silver = False
    black = False

    text_string = a.split()
#    print(a)
    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_flakenc) > j:    
            if text_string[i].casefold() == taul_flakenc[j].casefold():
                flake = True
                zinc = True
                nickel = True
#                print("Flake loydetty")
                text_string.pop(i)
                i -= 1
            j += 1
        i += 1

    i = 0
   
    while len(text_string) > i:
        j = 0
        while len(taul_feznni) > j:    
            if text_string[i].casefold() == taul_feznni[j].casefold():
                iron = True
                zinc = True
                nickel = True
                text_string.pop(i)
                i -= 1
            j += 1
        i += 1

    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_znni) > j:    
            if text_string[i].casefold() == taul_znni[j].casefold():
                zinc = True
                nickel = True
                text_string.pop(i)
                i -= 1
            j += 1
        i += 1

    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_zinc) > j:    
            if text_string[i].casefold() == taul_zinc[j].casefold():
                if text_string[i].casefold() == 'ZNC'.casefold():
                    yellow = True
                zinc = True
                text_string.pop(i)
                i -= 1
            j += 1
        i += 1
    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_nickel) > j:    
            if text_string[i].casefold() == taul_nickel[j].casefold():
                nickel = True

                text_string.pop(i)
                i -= 1
            j += 1
        i += 1
    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_zinc_iron) > j:    
            if text_string[i].casefold() == taul_zinc_iron[j].casefold():
                iron = True
                zinc = True
                text_string.pop(i)
                i -= 1
            j += 1
        i += 1
    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_iron) > j:    
            if text_string[i].casefold() == taul_iron[j].casefold():
                iron = True
                zinc = True
                text_string.pop(i)
                i -= 1
            j += 1
        i += 1
    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_topc) > j:    
            if text_string[i].casefold() == taul_topc[j].casefold():
                TOPC = True

                text_string.pop(i)
                i -= 1
            j += 1
        i += 1
    i = 0

    while len(text_string) > i:

        j = 0
        while len(taul_black) > j:    
            if text_string[i].casefold() == taul_black[j].casefold():
                black = True

#                text_string.pop(i)
#                i -= 1
            j += 1
        i += 1

    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_pass) > j:    
            if text_string[i].casefold() == taul_pass[j].casefold():
#                print(text_string)
                if text_string[i].casefold() == 'MP'.casefold() or text_string[i].casefold() == 'MPS'.casefold():
                    black = True
                    zinc = True
                passivated = True
                text_string.pop(i)
                i -= 1                   
            j += 1
        i += 1

    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_waxed) > j:    
            if text_string[i].casefold() == taul_waxed[j].casefold():
                waxed = True

                text_string.pop(i)
                i -= 1
            j += 1
        i += 1
    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_tran) > j:    
            if text_string[i].casefold() == taul_tran[j].casefold():
                tran = True

                text_string.pop(i)
                i -= 1
            j += 1
        i += 1

    i = 0



    while len(text_string) > i:
        j = 0
        while len(taul_flake) > j:    
            if text_string[i].casefold() == taul_flake[j].casefold():
                flake = True
                zinc = True
#                print("Flake loydetty")
                text_string.pop(i)
                i -= 1
            j += 1
        i += 1
    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_silver) > j:    
            if text_string[i].casefold() == taul_silver[j].casefold():
                silver = True
 #               print("Silver loydetty")
#                text_string.pop(i)
#                i -= 1
            j += 1
        i += 1
    i = 0

    while len(text_string) > i:
        j = 0
        while len(taul_yellow) > j:    
            if text_string[i].casefold() == taul_yellow[j].casefold():
                yellow = True
 #               print("Silver loydetty")
#                text_string.pop(i)
#                i -= 1
            j += 1
        i += 1
    
#    print("zinc=",zinc,"nickel=",nickel,"iron=",iron,"topc=",TOPC,"black=",black,"wax=",waxed,"tran=",tran,"flake=",flake,"silver=",silver,"passivated=",passivated)

# Sinkin maarittelyt lopulliseen arvoon

    if TOPC:
        text_string.append('TOPCOAT')
    if tran:
        text_string.append('TRAN')

    if zinc and iron:
        if black:
            if waxed:
                text_string.append('ZIBW')
                return " ".join(list(dict.fromkeys(text_string)))
        text_string.append('ZIB')
        return " ".join(list(dict.fromkeys(text_string)))
    if waxed:
        text_string.append('WAX')
    if zinc and nickel:
        if flake:
            text_string.append('FLZNNC')
            
            return " ".join(list(dict.fromkeys(text_string)))
        if black:
            text_string.append('ZINI')
            text_string.append('BL')
            return " ".join(list(dict.fromkeys(text_string)))
        text_string.append('ZINI')
        return " ".join(list(dict.fromkeys(text_string)))
    if zinc:
        if flake:
            if silver:
                text_string.append('FLZN')
                text_string.append('Silver')
                return " ".join(list(dict.fromkeys(text_string)))
            text_string.append('FLZN')
            return " ".join(list(dict.fromkeys(text_string)))
        if yellow:
            text_string.append('YZPL')
            for i in text_string:
                if i.casefold() == "CR3+".casefold():
                    text_string.append(text_string.pop(text_string.index(i)))
                    break
            return " ".join(list(dict.fromkeys(text_string)))
        if passivated:
            if black:
                text_string.append('MP')
                return " ".join(list(dict.fromkeys(text_string)))
        text_string.append('ZN')
        return " ".join(list(dict.fromkeys(text_string)))
    if nickel:
        text_string.append('NI')
        return " ".join(list(dict.fromkeys(text_string)))
    if passivated and black:
        text_string.append('MP')

#    if flake:
#       text_string.append('FLZN')
#        return " ".join(list(dict.fromkeys(text_string)))
    return " ".join(list(dict.fromkeys(text_string)))


def remove_duplicates(a): #poistaa duplikaatit stringistä, funktio ottaa vastaan kokonaisen stringin ja palauttaa stringinä
    new_text = a.casefold().split()
    return " ".join(list(dict.fromkeys(new_text)))

def get_size(tekstisyotto,Lisainfo): # Hakee Lisainfo-kentästä kokotiedot (x-alkavat)

#    print("tekstinsyotto on=",tekstisyotto)
#    print("Lisainfo on=",Lisainfo)
    
    tl_search = False
    add_size = False
    a_arvo = False
    m_arvo = False
    kovuus_arvo = False
    material_arvo = False


    

    k = "X"
    rege = []
    text_string = []
    text_split = tekstisyotto.split()
    x = re.findall(r"(?<!T)[Xx]\s?\d*[.,]?\d*",Lisainfo)
 
    for i in x:
        j = i.replace(' ','')
        j = j.replace("x"," x ")
        j = j.replace("X"," X ")
        j = j.replace(".",",")
        j = j.strip()        
        rege.append(str(j))
    
    while(k in rege): # poistaa listasta stringit jotka sisältää vain x-arvon
        rege.remove(k)
#    print(rege)
    for i in text_split:
        text_string.append(i)
        if i == 'UNC'.casefold() or i == 'UNF'.casefold() :
            text_string.extend(rege)
            add_size = True
        for j in taul_m:
            if i.casefold() == j.casefold(): # Etsii m-taulun perusteella indexin jonka perään syötetään kokotiedot
                add_size = True
                if len(rege) > 0:
                    x1 = rege[-1]

                    x = re.search(x1[2:]+r"/~?\d+[,.]?\d*",Lisainfo) #Etsitaan mittatietoihin thread arvoja merkilla '/'
                    tl_search = True
                    

                    if bool(x) and tl_search == True:
                        string_diff = x.group(0)
                        string_diff = string_diff.split("/",1)
                        if string_diff[0] != string_diff[1]:
                            rege.append(str(x.group(0)).replace(x1[2:],""))
                text_string.extend(rege)
    for i in text_split:
        for j in taul_m:
            if i.casefold() == j.casefold():
                m_arvo = True
    for i in text_split:
        for j in taul_a:
            if i.casefold() == j.casefold():
                a_arvo = True
    for i in text_split:
        for j in taul_kovuus:
            if i.casefold() == j.casefold():
                kovuus_arvo = True
    for i in text_split:
        for j in taul_material:
            if i.casefold() == j.casefold():
                material_arvo = True                           
#    print("m arvo",m_arvo,"a arvo",a_arvo)
    if m_arvo == False and a_arvo == True and add_size == False:
        
        x = re.search(r"\d+[.,]?\d*\s*[x?X?]\s*\d+[.,]?\d*\s*[xX]?\s*\d*[,.]?\d*",Lisainfo)
        if x:
            rege = []
            rege = str("X "+x.group(0)).upper()
            rege = rege.replace(' ','')
            rege = rege.replace("X"," X ")
            rege = rege.strip()
            for i in text_string:
                for j in taul_a:
                    if i.casefold() == j.casefold():
                        text_string.insert(text_string.index(i) + 1,rege)

                        add_size = True
                        break
        else:
            x = re.search(r"\d*[,.]\d*",Lisainfo)
            if bool(x):
                text_string.append(x.group(0))
                add_size = True

    if m_arvo == False and a_arvo == False and add_size == False and kovuus_arvo == True:
        x = re.search(r"\d+[.,]?\d*\s*[x?X?]\s*\d+[.,]?\d*\s*[xX]?\s*\d*[,.]?\d*",Lisainfo)
        if x:
            
            rege = []
            rege = str("X "+x.group(0)).upper()
            rege = rege.replace(' ','')
            rege = rege.replace("X"," X ")
            rege = rege.strip()
            for i in text_string:
                for j in taul_kovuus:
                    if i.casefold() == j.casefold():
                        text_string.insert(text_string.index(i) + 1,rege)

                        add_size = True
                        break
    if m_arvo == False and a_arvo == False and add_size == False and kovuus_arvo == False and material_arvo == True:
        x = re.search(r"\d+[.,]?\d*\s*[x?X?]\s*\d+[.,]?\d*\s*[xX]?\s*\d*[,.]?\d*",Lisainfo)
        if x:
            
            rege = []
            rege = str("X "+x.group(0)).upper()
            rege = rege.replace(' ','')
            rege = rege.replace("X"," X ")
            rege = rege.strip()
            for i in text_string:
                for j in taul_material:
                    if i.casefold() == j.casefold():
                        text_string.insert(text_string.index(i) + 1,rege)

                        add_size = True
                        break
    if m_arvo == False and a_arvo == False and add_size == False and kovuus_arvo == False and material_arvo == False:
        x = re.search(r"\d+[.,]?\d*\s*[x?X?]\s*\d+[.,]?\d*\s*[xX]?\s*\d*[,.]?\d*",Lisainfo)

        if x:
            
            rege = []
#            rege = ("X "+str(x.group(0)))
            rege = str("X "+x.group(0)).upper()
            rege = rege.replace(' ','')
            rege = rege.replace("X"," X ")
            rege = rege.strip()
            if len(rege) > 0:
                x1 = rege[-3:].replace(" ","")
                x = re.search(x1+r"/~?\d+[,.]?\d*",Lisainfo) #Etsitaan mittatietoihin thread arvoja merkilla '/'

                tl_search = True
                if bool(x) and tl_search == True:
                    string_diff = x.group(0)
                    string_diff = string_diff.split("/",1)
                    if string_diff[0] != string_diff[1]:
                        
                        rege = rege.replace(x1,x.group(0))
            text_string.insert(2,rege)
            add_size = True
        else:
            x = re.search(r"\d*[,.]\d*",Lisainfo)
            if bool(x):
                text_string.append(x.group(0))
                add_size = True
            else:
                if len(text_string) > 1:
                    y = re.search(r"\d*",text_string[1])[0]
                    x = re.findall(r"\d+",Lisainfo)
                    if bool(x):
                        for i in x:
                            if i != y:
                                rege.append(i)
                                break

                        if len(rege) > 0:
                            text_string.append(rege[0])
                else:
#                    x = re.findall(r"\d+",Lisainfo)

                    pass
                    

#    print("tekstinsyotto on=",text_string)
#    print("m_arvo",m_arvo,"a_arvo",a_arvo,"add_size",add_size,"kovuus_arvo",kovuus_arvo,"material_arvo",material_arvo)
#    print("tekstinsyotto on=",text_string)
#    print("Lisainfo on=",Lisainfo)
#    print("-----------------------------")
    torx_arvo = False
    k = 0
#    print(Lisainfo)                        
    x = re.findall(r"\b[Tt][-]?[1-9Xx][-]?\d+",Lisainfo)
    
    if len(x) > 0:
        for i in x:
                if k < len(i) and k < 6:
                        k = len(i)
                        index_len = x.index(i)
        x = x[index_len].upper()
        x = x.replace('-','')
        x = x.replace('X','')
        x = x.replace('T','TX')


        for i in text_string:
            if i.upper() == 'TORX':
                torx_arvo = True
                text_string.pop(text_string.index(i))
        if x.upper() == 'TX':
            x = 'TORX'
            text_string.append(x)
            torx_arvo = True
        elif x[0:2].upper() == 'TX0':
            if torx_arvo == False:
                text_string.append('TORX')
                x = 'TORX'
                torx_arvo = True
        else:
            text_string.append(x)
            torx_arvo = True          
    else:
        x = re.search(r" TX ",Lisainfo)

        for i in text_string:
            if i == 'TORX'.casefold():
                torx_arvo = True

        if x and torx_arvo == False:
            text_string.append('TORX')
            torx_arvo = True
            

    for i in flake_lopulliset: # Järjestetään flaken järjestys -> flake -> aika -> väri
        if i in text_string:
            for j in taul_flake_kesto:
                if j in text_string:
                    flake_pop = text_string.pop(text_string.index(j))
                    text_string.insert(text_string.index(i) + 1,flake_pop)

    x = re.search(r"TO RR",Lisainfo)
    if x:
        for i in text_string:
            if i == '240H'.casefold() or i == '480h'.casefold() or i == '720h'.casefold():
                text_string.insert(text_string.index(i) + 1,"RR")
                break
    for i in text_string:
        if i == 'GLEITMO'.casefold():
            for j in taul_gleitmo:
                x = re.search(" "+j+" ",Lisainfo)
                if x:
                    text_string.insert(text_string.index(i) + 1,j)
    x = re.search(r"\d*[,.]?\d+\s?[Mm][Mm]",Lisainfo)

#    Lisainfo = Lisainfo.replace('µ','MY')

    if bool(x):
        x = x[0].replace(" ","")
        text_string.append(x)

    x = re.search(r'\d*UM',Lisainfo)
    if bool(x):
#        print('UM found',x)
        if len(x[0]) > 2:
            x = x[0]
            x = x.replace(" ","")
            x = x.replace('UM','MY')
            text_string.append(x)
    x = re.search(r'\d*-?\d*\s?MY',Lisainfo)
    if bool(x):
#        print('MY found',x)
        if len(x[0]) > 2:
            x = x[0]
            x = x.replace(" ","")
            text_string.append(x)
    x = re.search(r'\d*-?\d*\s?YM',Lisainfo)
    if bool(x):
#        print('MY found',x)
        if len(x[0]) > 1:
            x = x[0]
            x = x.replace(" ","")
            x = x.replace("YM","MY")
            text_string.append(x)     
#    x = re.search(r'\d*-?\d*\s?',Lisainfo)
#    if bool(x):
#        print('µ',x)
#        if len(x[0]) > 1:
#            x = x[0]
#            x = x.replace("µ","MY")
#            text_string.append(x)
    x = re.search(r'PRECOTE\s?\d*-?\d*',Lisainfo)
    if bool(x):
#        print('MY found',x)
        if len(x[0]) > 7:
            x = x[0]
            text_string.append(x)     


    return " ".join(list(dict.fromkeys(text_string)))


def text_split_regexp(text): ## Etsii sanojen sisältä taulujen määrityksiä käyttäen regexia erotellen ne sanoista
    match_text = text.casefold()
    skip_match_bool = False
    t_m = False
    a_arvo = False
    kovuus_arvo = False
    
    for i in range(len(taul_colors)):
        if taul_colors[i].casefold() not in skip_match:  # pienten arvojen määritys pois etsinnästä koska voi rikkoa pidempia sanoja
            pattern = re.compile(taul_colors[i].casefold())
            match_text = pattern.sub(" "+taul_colors[i]+" ",text.casefold())
            text = match_text.strip()


    text = text.split()
    for i in text: #tarkistetaan onko jo kovuus-arvo löydetty
        for j in taul_kovuus:
            if i.casefold() == j.casefold():
                kovuus_arvo = True
                break
    text = " ".join(text)

    for i in reversed(range(len(taul_kovuus))):
        if taul_kovuus[i].casefold() not in skip_match:
            if kovuus_arvo:
                break
            pattern = re.compile(taul_kovuus[i].casefold())
            match_text = pattern.sub(" "+taul_kovuus[i]+" ",text.casefold())
            text = match_text.strip()
    
#    for i in range(len(taul_material)):
#        pattern = re.compile(taul_material[i].casefold())
#        match_text = pattern.sub(" "+taul_material[i]+" ",text.casefold())
#        text = match_text.strip()

    for i in text: #Etsitään m-arvoa tekstistä
        for j in taul_m:
            if i.casefold() == j.casefold():
                t_m = True

    for i in reversed(range(len(taul_m))):
        if taul_m[i].casefold() not in skip_match:
            if taul_m[i].casefold() == "M10".casefold():
                break
            pattern = re.compile(taul_m[i].casefold())
            match_text = pattern.sub(" "+taul_m[i]+" ",text.casefold())
            text = match_text.strip()

    text = text.split()
    for i in text: #tarkistetaan onko jo a-arvo löydetty
        for j in taul_a:
            if i.casefold() == j.casefold():
                a_arvo = True
                break
    text = " ".join(text)

    for i in reversed(range(len(taul_a))): # etsitään a-arvoa jos ei ole jo löydetty
        if taul_a[i].casefold() not in skip_match:
            if a_arvo:
                break
            pattern = re.compile(taul_a[i].casefold())
            match_text = pattern.sub(" "+taul_a[i]+" ",text.casefold())
            if match_text != text:
                text = match_text.strip()
                break
    
    return match_text #palautus stringina

def ansi_struct(a):
#    text_string = (" ".join(a))
    text_string = a
    while text_string:
        if text_string[0] == 'ANSI'.casefold():
            break
        else:
            text_string.append(text_string.pop(0))

    return text_string

def identify(a,b,c): # a = tekstisyotto, b = column-index, c = rivi-index
    insert_index = 2 # alkumäärittely stringin läpikäyntiin (indexin alkuvaiheessa jo mahdollinen din/iso koodi)
    iso_din = False # Määrittely jos tuotenumerossa ei ole iso- / din-koodia
    no_num = False # Määrittely jos iso- / din-koodia ei löytynyt alkuperäisistä tauluista mutta löytyy toisen kolumnin ensimmäisestä sanasta
    t_material = False
    t_kovuus = False
    t_m = False
    t_colors = False
    t_a = False
    en_id = False
    ansi = False
    test_split = ""

    if b == otsikot - 1: ## määrittelee lopullisen rivitiedon ja siirtää löytyvät rakenteet paikoilleen
        a = a.replace("nan ","")
#        print("Arvo ennen text_split_regexp,ilman nan",a)
        
        text_regex = text_split_regexp(a) # Etsii stringin sanojen sisalta mahdollisia maarityksia
        text_split = text_regex.split() # Muuntaa stringin listaksi
        lisainfo = [] ## lista ylijaamille
#        print("Arvo regex jalkeen",text_split)
        for i in text_split:
#            print(i)
            x = re.search(r"(?<!k)ansi",i.casefold())
            if bool(x):
                
                ansi = True
                text_split.insert(insert_index,"ANSI")
                
                text_split = (" ".join(text_split))
                text_split = re.sub(r"ansi",r" ANSI ",text_split)
                text_split = text_split.split()
                for i in text_split:
                    i = i.strip()
                break
#                print(x)


#            print("I=",i,"ISO/DIN TRUE"," index=",text_split.index(i))
        if text_split[0] == 'ISO'.casefold() or text_split[0] == 'DIN'.casefold():
            iso_din = True

            
        
        if text_split[1] == "ISO".casefold() or text_split[1] == "DIN".casefold():
            no_num = True


        if no_num == True and iso_din == False:
            lisainfo.append(text_split.pop(0))
            

        if text_split[0] == 'EN'.casefold():
            en_id = True    
#            print(text_split)
#            iso_din = True
#            insert_index = 1
        if iso_din == False and no_num == False and en_id == False:
            
            while text_split:
                x = text_split[0]
#                print(x)
                if x == 'ISO'.casefold() or x[0:3] == 'ISO'.casefold():
                    break
                elif x == 'DIN'.casefold() or x[0:3] == 'DIN'.casefold():

                    break
                lisainfo.append(text_split.pop(0))
                if len(text_split) == 0:
                    text_split.extend(lisainfo)
                    lisainfo = []
                    break
            if len(lisainfo) != 0:
                while lisainfo:                
                    text_split.append(lisainfo.pop(lisainfo.index(lisainfo[0])))
                    if len(lisainfo) == 0:
                        break
        
        if iso_din:
            x1 = text_split[1]
            if x1[-1].casefold() == 'A'.casefold() or x1[-1].casefold() == 'B'.casefold():
                if x1[-2] == '-':
                    pass
                else:
                    muuta = "-"+x1[-1]
                    x1 = x1.replace(x1[-1],muuta)
                    text_split[1] = x1

            teksti1 = " ".join(text_split)
#            print(teksti1)
#            print(text_split[1])
#            x = re.search(text_split[1]+r"-?\s?[AaBbLlNnfFcCgZzKkMm]\s?-?/?[+]?\s?[bBZzfFhH]?\s",teksti1)
            x = re.findall(text_split[1]+r"-?\s?[AaBbLlNnfFcCgZzKkMmhHPp]\s?-?/?[+]?\s?[bBZzfFhH]?\s",teksti1)
#            print(x)
            if len(x) > 0:
                x1 = x[0]
                for i in x:
                    if len(i) > len(x1):
                        x1 = i
                x = x1
            if x:
                x = str(x)
                x = x.strip()
                x = x.replace(" ","")
                if x[-2] == '-':
                    pass
                elif x.casefold() == text_split[1].casefold():
                    pass
                else:
                    if x[-3] == '-':
                        pass
                    elif x[-2] == '/':


                        muuta = "-"+x[-3:]

                        x = x.replace(x[-3:],muuta)
                    elif x[-2] == '+':

                        muuta = "-"+x[-3:]
                        x = x.replace(x[-3:],muuta)
                      
                    elif len(x) > len(text_split[1])+1:
                        muuta = "-"+x[-2:]
                        x = x.replace(x[-2:],muuta)
                    else:
                        muuta = "-"+x[-1]
                        x = x.replace(x[-1],muuta)

                text_split.insert(1,x)
            else:
                pass
        if en_id:

            teksti1 = " ".join(text_split)
            x = re.search(r"\d*",text_split[1])[0]
            y = re.search(x+r"[-]?\d",teksti1)

            if bool(x) and bool(y):
                text_split[1] = y[0]


                
            
        
        
        for i in range(len(text_split)):
            for j in range(len(taul_material)): ## Rakenteen ensimmainen osa
                if text_split[i].casefold() == taul_material[j].casefold():
                    move_detail = text_split.pop(i)
                    text_split.insert(insert_index,move_detail)
                    t_material = True
                    insert_index += 1
                     

        for i in range(len(text_split)):
            for j in range(len(taul_kovuus)): ## Rakenteen toinen osa
                if text_split[i].casefold() == taul_kovuus[j].casefold():
                    move_detail = text_split.pop(i)
                    text_split.insert(insert_index,move_detail)
                    t_kovuus = True
                    insert_index += 1
#                    print(text_split[i],"kovuus match","text_string =",text_split)
#        print(insert_index,"index",text_split,"teksti") 
        for i in range(len(text_split)):
            if t_a:
#                print("t_a breikki",text_split)
                break
            for j in reversed(range(len(taul_a))): ## Rakenteen kolmas osa
                if text_split[i].casefold() == taul_a[j].casefold():
                    move_detail = text_split.pop(i)
                    text_split.insert(insert_index,move_detail)
                    t_a = True
                    insert_index += 1
#        print("text_split=",text_split)
        for i in range(len(text_split)):
            for j in range(len(taul_m)): ## Rakenteen neljas osa
                if text_split[i].casefold() == taul_m[j].casefold():
                    move_detail = text_split.pop(i)
                    text_split.insert(insert_index,move_detail)
                    t_m = True
#                    print("move_detail=",move_detail)
                    insert_index += 1
#        print(text_split,"HEP!",t_m,"t_m?")
        if t_m == False:
            text_split = (" ".join(text_split))
            x = re.search(r"\bm[M]?[\s+]?\d+[.,]?[\d+]?",text_split)
#            print("T_m == false, pattern etsii nyt =",x)
            
            if x:
                move_detail = str(x.group(0)).replace(" ","")
                move_detail = str(move_detail)
                if move_detail[-1] == ',':
                    move_detail = move_detail[:-1]
                text_split = text_split.replace(str(x.group(0)),"")
                text_split = text_split.split()
                text_split.insert(insert_index,move_detail)
#                insert_index += 1
                for i in range(len(text_split)):
                    for j in range(len(taul_m)):
                        if text_split[i].casefold() == taul_m[j].casefold():                            
                            text_split.insert(insert_index,move_detail)
                            t_m = True
                            insert_index += 1
                            break
            else:
                text_split = text_split.split()
        
        for i in range(len(text_split)):
            for j in range(len(taul_colors)): ## Rakenteen viimeinen osa    
                if text_split[i].casefold() == taul_colors[j].casefold() and i > 1:
                    move_detail = text_split.pop(i)
                    text_split.insert(insert_index,move_detail)
                    t_colors = True
                    insert_index += 1
#        print(insert_index,"index mista splitataan=",text_split[insert_index])
#        text_split = remove_duplicates(" ".join(text_split))
#        text_split = text_split.split()
#        print("Teksti ennen ylijaaman asettamista= ",text_split)
#        if ansi:
#            text_split = ansi_struct(text_split)
#            text_split = (" ".join(text_split))
#            print(text_split)
#            return text_split
        for i in range(insert_index,len(text_split)): # Ylijaamien määrittely lisainfo-kolumnille jotka eivat osuneet rakenteeseen
            
            ylijaama = text_split.pop(insert_index)
#            print("Ylijaamaan siirtymassa= ",ylijaama,"index",insert_index)
            lisainfo.append(ylijaama)
        if ansi:
            ansi_b = True
            lisainfo.append(text_split.pop(0))
            lisainfo.append(text_split.pop(0))

            x = text_split[1]
           
            if x[0:1] != 'b'.casefold():
                ansi_b = False
                for i in text_split:
                    if i[0:1] == 'b'.casefold():
                        ansi_b = True
                        text_split.insert(1,text_split.pop(text_split.index(i)))
                        break
            
#        print(text_split,"rakenne ylijaamien jalkeen")
        lisainfo_join = (" ".join(lisainfo)) #Muutetaan stringiksi
        for i in range(len(taul_colors)): ## Tarkistaa lisäinfo kentästä taul_colors välilyönnilliset määritykset ja siirtää ne päätietoihin
            if lisainfo_join.find(' '+taul_colors[i].casefold()+' ') != -1:
                text_split.append(taul_colors[i])
                lisainfo_join = re.sub(taul_colors[i].casefold(), '', lisainfo_join)
       
        data['Lisainfo'][c] = lisainfo_join.upper() # Vienti lisainfo-kenttaan
        return " ".join(text_split) # Tekstisyoton palautus stringina
    if b == 0: #ensimmainen vaihe, din- ja isotaulujen lapikaynti verraten 3 ja 4 ensimmaiseen item nroon
 
        for i in range(len(taul_din)):
            if a[0:3] == taul_din[i]:
                tekstisyotto = 'DIN ' + taul_din[i]
                return tekstisyotto
        for i in range(len(taul_din2)):
            if a[0:4] == taul_din2[i]:
                tekstisyotto = 'DIN ' + taul_din2[i]
                return tekstisyotto
        for i in range(len(taul_iso)):
            if a[0:4] == taul_iso[i]:
                tekstisyotto = 'ISO ' + taul_iso[i]
                return tekstisyotto
        for i in range(len(taul_din3)):
            if a[0:5] == taul_din3[i]:
                tekstisyotto = 'DIN ' + taul_din3[i]
                return tekstisyotto 
        for i in range(len(taul_iso2)):
            if a[0:5] == taul_iso2[i]:
                tekstisyotto = 'ISO ' + taul_iso2[i]
                return tekstisyotto
        for i in range(len(taul_iso3)):
            if a[0:6] == taul_iso3[i]:
                tekstisyotto = 'ISO ' + taul_iso3[i]
                return tekstisyotto
        for i in range(len(taul_en)):
            if a[0:5] == taul_en[i]:
                tekstisyotto = 'EN ' + taul_en[i]
                return tekstisyotto
            elif a[0:1] == 'EN':
                print("pog",a[2:7])
                print(taul_en[i])
                if a[2:7] == taul_en[i]: #eitoimi, korjaa
                    tekstisyotto = 'EN ' + taul_en[i]
                    print(tekstisyotto)
                    return tekstisyotto
    return a

def cosmetics_mod(a):
    new_list = []
    seen = set()
    text_string = a.upper()
    text_string = text_string.split()
    for i in text_string:
        if i == 'BRASS':
            for j in text_string:
                if j == 'MS':
                    text_string.pop(text_string.index(i))

    text_string = " ".join(text_string)

    text_string = text_string.replace("BRASS","MS")
    text_string = text_string.replace("KOPPER","CU")
    text_string = text_string.replace("KUPAROITU","CU")
    text_string = text_string.replace("COPPERPL","CU")
    text_string = text_string.replace("MEC\\.","MECH")
    text_string = text_string.replace("MEK\\.","MECH")
    text_string = text_string.replace("\\","")
    text_string = text_string.replace("NAN","")
    text_string = text_string.replace(" /","/")
    text_string = text_string.replace("BUMAX 109","BUMAX109")
    text_string = text_string.replace("BUMAX 88","BUMAX88")
    text_string = text_string.replace("BNER","NERINOX BLACK")
    text_string = text_string.replace("x ,","")
    text_string = text_string.replace("F105","FINIGARD 105")

    text_string = text_string.split()
    for i in text_string:
        if i == 'SEALER':
            text_string.pop(text_string.index(i))
            text_string.append('+ SEALER')
            break
    for i in text_string:
        if i not in new_list:
            new_list.append(i)
            seen.add(i)
        elif i == 'X':
            new_list.append(i)

    text_string = new_list

    text_string = " ".join(text_string)
    text_string = text_string.replace(" X "," x ")
    if text_string[-1] == '.' or text_string[-1] == ',':
        text_string = text_string[:-1]
    text_string = text_string.strip()

    return text_string

def analyze_itemnr(a):
    
    itemnro = a
    teksti = ''

    x = re.search(r'HO',itemnro)
    if x:
        teksti = teksti + ' HOLO-CHROME'
    if itemnro[-1] == 'W':
        teksti = teksti + ' WAX'
    if itemnro[-4:] == 'F105':
        teksti = teksti + ' F105'
#    teksti = teksti.replace(itemnro,'')
    return teksti
    

##Main program under this

data['Tekstinsyotto'] = '' ## Rakenne kolumnin luonti
data['Lisainfo'] = '' ## Lisainfo kentan luonti
data['Syotetyt'] = ''
data['Luetut'] = ''
data['Orig standard'] = ''
for i in range(rivit): ## Loopataan rivit
    tekstisyotto = '' ## Maaritellaan tekstikentta tyhjaksi
    orig_std = ''
    for j in range(otsikot): ## Loopataan kolumnit per rivi
        tekstisyotto += str(data.iloc[i,j]) ## Haetaan indexin perusteella rivitieto
        if j == 1: #katsotaan mitä certifikaattiarvoja on laitettu tuotteen descriptioniin joita vertaillaan myöhemmin onko oikea koodi generoitu
            x = re.search(r'din',str(data.iloc[i,j]).casefold())
            if bool(x):
                orig_std += 'DIN'
            x = re.search(r'(?<!g\s)iso(?![-fk])(?!\sf)',str(data.iloc[i,j]).casefold())
            if bool(x):
                if len(orig_std) > 0:    
                    orig_std += ' ISO'
                else:
                    orig_std = 'ISO'   
            x = re.search(r"(?<!k)ansi",str(data.iloc[i,j]).casefold())
            if bool(x):
                if len(orig_std) > 0:    
                    orig_std += ' ANSI'
                else:
                    orig_std = 'ANSI'          
            if len(orig_std) == 0:
                data['Orig standard'][i] = 'Empty'
            else:
                data['Orig standard'][i] = orig_std

        if j == 0:
#            print(tekstisyotto)
            if tekstisyotto[-1].casefold() == 'x':
                tekstisyotto = tekstisyotto[:-1]+'|'
            analyzed_itemnr = analyze_itemnr(tekstisyotto) #etsitään tuotekoodista mahdollisia lisäarvoja (ensimmäinen column)
#            print(analyzed_itemnr,"analysoitu")
        syote = identify(tekstisyotto,j,i) ## Ohjelma joka tunnistaa indexin perusteella toimenpiteet (Alku ja loppu). Lisainfo-kentta viedaan taalla

        if tekstisyotto != syote: ## Tarkistetaan onko identify-ohjelma tehnyt muutoksia tekstisyotto kenttaan, jos on niin maaritellaan arvo uusiksi.
            tekstisyotto = syote ## Korvaa Tekstisyotto stringin jos alkuperainen kolumni-tieto ei tasmaa
#            print(tekstisyotto,"syote korvannut tekstin")
        if len(analyzed_itemnr) > 0 and j == 0:
            tekstisyotto +=' ' + analyzed_itemnr
        tekstisyotto += ' ' ## Lisaa valilyonnin haettujen rivitietojen peraan erotellen kolumnitiedot

    data['Luetut'][i] = len(tekstisyotto.split())
#    print("Tekstisyoton muoto ennen kasittelya=",tekstisyotto,"syote =",syote)
    rem_dupl = remove_duplicates(tekstisyotto) ## Poistaa duplikaatit stringista, hyvaksyy stringin ja palauttaa sen
#    print("Duplikaatio poistojen tuotos=",rem_dupl)
    rem_dupl_index = generate_zinc(rem_dupl) ## Etsii sinkin määrittelyjä ja rakentaa arvon niiden perusteella
#    print("Sinkkigeneraation tuotos=",rem_dupl_index)
    rem_dupl_index1 = generate_others(rem_dupl_index) #rakennetaan muita kuin sinkki variaatioita
#    print("Muiden generaatioiden tuotos",rem_dupl_index1)
    Lisainfo = str(data.iloc[i,linsainfo_index]) #Haetaan lisainfo-kentta
#    print("lisainfo =",Lisainfo)
    sized = get_size(rem_dupl_index1,Lisainfo) # hakee lisainfo-kentasta M-arvon jälkeen löytyvät numerot joissa kriteerinä x-arvo
    cosmetics = cosmetics_mod(sized)
#    print(cosmetics)
    data['Tekstinsyotto'][i] = cosmetics ## Rakenteen vienti kenttaan Tekstisyotto 
    data['Syotetyt'][i] = len(cosmetics.split())

#data.to_csv(r'E:\koodit\Git\Master data_työversio 1_modified.csv')
data.to_csv(r'E:\koodit\Git\Master data_työversio_din_iso_modified.csv') #tallennus
#data.to_csv(r'E:\koodit\Git\Mpmp.csv')

#print('Columnit:\n',data,'\n') #columni check
#print(data.iloc[1635,5],"Arvo m8x") #rivitieto check, ensimmäinen index rivi- ja toinen kolumni-index
#print(data.iloc[25,5],"Arvo M16")
#print(data.iloc[766,5],"Arvo M 8")