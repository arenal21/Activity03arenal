import arenal_script_1_stat as script_1
import arenal_script_2_ev as script_2

"""
Pokemon: Eevee
Level = 40
Nature: Jolly (inc. Stat in Speed, while dec. stat in Sp.Atk)
Based Stats:
    Hp: 55 (iv = 25, ev = 110)
    Attack: 55 (iv = 16, ev = 70)
    Defense: 50 (iv = 10, ev = 60)
    Sp.Atk: 65 (iv = 20, ev = 40)
    Sp.Def: 65 (iv = 24, ev = 50)
    Speed: 55 (iv = 10, ev = 115)
"""

iv = [0,0,0,0,0,0]
ev = [0,0,0,0,0,0]
nature = [1,1,1,0.9,1,1.1]
base = [0,0,0,0,0,0]
ivcal = [0,0,0,0,0,0]
evcal = [0,0,0,0,0,0]

check_ev = 0

add_stat = [0,0,0,0,0,0]

def start():
    print("""
    Please pick a type of Calculation:

    1. Stats calculation
    2. Ev calculation
    3. Exit
    """)
    opt = int(input("Choose an option:"))

    if opt == 1:
        statsCalculation()
    elif opt == 2:
        while True:
            print("""
            1. Perform EV calculation for single stats
            2. perform EV caculation for all stats
            3. Back
            """)
            opt = int(input("Choose an option:"))
            if opt == 1:
                singleStats()
            if opt == 2:
                allStats()
            if opt == 3:
                start()
            print("Invalid choice, Try Again")
    elif opt == 3:
        exit()
    else:
        print("Invalid Choice, Try Again")
        start()                           


def statsCalculation():
    print("\nPlease note that IV values only range from 0 - 31 and EV values to 0 - 255 with a maximum of 510 values in all stats! \n")
    
    print("\nEnter pokemon stat/s: \n")
    lvl = int(input("Enter Level:"))
    hp = int(input("\nEnter based hp:"))
    iv[0] = int(input("Enter IV:"))
    ev[0] = int(input("Enter EV:"))
    
    print("\nOther Stats\n")
    atk = int(input("Enter Attack: "))
    iv[1] = int(input("Enter IV: "))
    ev[1] = int(input("Enter EV: "))
    defense = int(input("Enter Defense: "))
    iv[2] = int(input("Enter IV: "))
    ev[2] = int(input("Enter EV: "))
    spAtk = int(input("Enter SP. Attack: "))
    iv[3] = int(input("Enter IV: "))
    ev[3] = int(input("Enter EV: "))
    spDef = int(input("Enter Sp. Defense: "))
    iv[4] = int(input("Enter IV: "))
    ev[4] = int(input("Enter EV: "))
    spd = int(input("Enter Speed: "))
    iv[5] = int(input("Enter IV: "))
    ev[5] = int(input("Enter EV: "))

    check_ev = ev[0] + ev[1] + ev[2] + ev[3] + ev[4] + ev[5]
    if check_ev > 510:
        print("\nEffort value should not exceed 510 when totaled! Try again")
        statsCalculation()

    print("\nPokemon Stats\n")
    print("Nature: Jolly(inc. Stat in speed, while dec. stat in sp.Atk)")
    totalhp = script_1.pokemonStats.hp_statsfunction(lvl,hp,iv,ev)
    print("\nHp:",round(totalhp, 2), end='\n\n')
    print("Other Stats: \n")
    str = script_1.pokemonStats.other_statsfunction(atk,defense,spAtk,spDef,spd,iv,ev,lvl,nature)
    stats_name = ['Attack:','Defense:','Special Attack:','Special Defense:','Speed']
    for x in range(len(str)):
        print(stats_name[x],round(str[x], 2))
        x = x + 1
    anotherCalculation()

def singleStats():
    basestat = [0,0,0,0,0,0]
    while True:
        print("""
        1. Hp
        2. Attack
        3. Defense
        4. Sp. Attack
        5. Sp. Defense
        6. Speed
        """)
        opt = int(input("Choose an option:"))
        if opt == 1:
            stat_type = 'hp'
            print("\nEnter pokemon stat/s: \n")
            lvl = int(input("Enter Level:"))
            basestat[0] = int(input("Enter base Hp:"))
            iv[0] = int(input("Enter IV:"))
            if iv[0] > 31:
                print("\nIV should range from 0 to 31. Try again!")
                singleStats()
            ev[0] = int(input("Enter EV:"))
            if ev[0] > 255:
                print("\nEV should range from 0 to 255. Try again!")
                singleStats() 
            stat = int(input("Desired increased in hp:"))

            ev_needed = script_2.pokemonEv.singleStatsFunction(stat_type,basestat,lvl,iv,ev,stat,nature)

            print("Pokemon's nature: Jolly(inc. stat in speed, while dec. stat in Sp.Atck)")
            print("\nThe EVs needed to increase the",stat_type,":",round(ev_needed, 2))

            while True:
                print("""
                1.Perform another EVs calculation
                2.Back
                """)  
                opt = int(input("Choose an option"))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anotherCalculation()
                print("Invalid Choice, Try Again")
        if opt == 2:
           stat_type = 'attack'
           print("\nEnter pokemon stat/s: \n")
           lvl = int(input("Enter Level:"))
           basestat[1] = int(input("Enter base attack:"))
           iv[1] = int(input("Enter IV:"))
           ev[1] = int(input("Enter EV:"))
           stat = int(input("Desired increased in attack:"))

           ev_needed = script_2.pokemonEv.singleStatsFunction(stat_type,basestat,lvl,iv,ev,stat,nature)

           print("Pokemon's nature: Jolly(inc. Stat in speed, while dec. stat in Sp.Atk)")
           print("\nThe EVs needed to increase the",stat_type,":", round(ev_needed, 2))

           while True:
               print("""
               1. Perform another EVs calculation
               2.Back
               """)
               opt = int(input("Choose an option"))
               if opt == 1:
                   singleStats()
               if opt == 2:
                    anotherCalculation()
               print("Invalid Choice, Try again")
        if opt == 3:
            stat_type = 'defense'
            print("\Enter pokemon stat\s: \n")
            lvl = int(input("Enter Level:"))
            basestat[2] = int(input("Enter base defense:"))
            iv[2] = int(input("Enter IV:"))
            ev[2] = int(input("Enter EV:"))
            stat = int(input("Desired increased in defense:"))

            ev_needed = script_2.pokemonEv.singleStatsFunction(stat_type,basestat,lvl,iv,ev,stat,nature)

            print("Pokemon's nature: Jolly(inc. Stat in speed, while dec. stat in Sp.Atk)")
            print("\nThe EVs needed to increase the",stat_type,":", round(ev_needed, 2))

            while True:
                print("""
                1. Perform another EVs calculation
                2. Back
                """)
                opt = int(input("Choose an option:"))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anotherCalculation()
                print("Invalid Choice, Try again")
        if opt == 4:
            stat_type = 'special attack'
            print("\nEnter pokemon stat\s: \n")
            lvl = int(input("Enter Level:"))
            basestat[3] = int(input("Enter base sp.attack:"))
            iv[3] = int(input("Enter IV:"))
            ev[3] = int(input("Enter EV:"))
            stat = int(input("Desired increased in sp.attack:"))

            ev_needed = script_2.pokemonEv.singleStatsFunction(stat_type,basestat,lvl,iv,ev,stat,nature)

            print("Pokemon's nature: Jolly(inc. Stat in speed, while dec. stat in Sp.Atk)")
            print("\nThe EVs needed to increase the",stat_type,":", round(ev_needed, 2))

            while True:
                print("""
                1. Perform another EVs calculation
                2. Back
                """)
                opt = int(input("Choose an option:"))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anotherCalculation()
                print("Invalid Choice, Try Again")
        if opt == 5:
            stat_type = 'special defense'
            print("\nEnter pokemon stat\s : \n")
            lvl = int(input("Enter Level:"))
            basestat[4] = int(input("Enter base sp.defense:"))
            iv[4] = int(input("Enter IV:"))
            ev[4] = int(input("Enter EV:"))
            stat = int(input("Desired increased in sp.defense:"))

            ev_needed = script_2.pokemonEv.singleStatsFunction(stat_type,basestat,lvl,iv,ev,stat,nature)

            print("Pokemon's nature: Jolly(inc. Stat in speed, while dec. stat in Sp.Atk)")
            print("\nThe EVs needed to increase the",stat_type,":", round(ev_needed, 2))   

            while True:
                print("""
                1. Perform another EVs calculation
                2. Back
                """)   
                opt = int(input("Choose an option"))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anotherCalculation()
                print("Invalid choice, Try again")
        if opt == 6:
            stat_type = 'speed'
            print("\nEnter pokemon stat/s \n")
            lvl = int(input("Enter Level:"))
            basestat[5] = int(input("Enter base speed:"))
            iv[5] = int(input("Enter IV:"))
            ev[5] = int(input("Enter EV:"))
            stat = int(input("Desired increased in speed:"))

            ev_needed = script_2.pokemonEv.singleStatsFunction(stat_type,basestat,lvl,iv,ev,stat,nature)

            print("Pokemon's nature: Jolly(inc. Stat in speed, while dec. stat in Sp.Atk)")
            print("\nThe EVs needed to increase the",stat_type,":", round(ev_needed, 2))

            while True:
                print("""
                1. Perform another EVs calculation
                2. Back
                """)   
                opt = int(input("Choose an option"))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anotherCalculation()
                print("Invalid choice, Try again")    


def allStats():
    stat_type = ['hp','attack','defense','special attack','special defense','speed']
    print("\nEnter pokemin stat/s \n")
    lvl = int(input("Enter Level:"))
    for x in range(len(stat_type)):
        base[x] = int(input("\nEnter base" + stat_type[x] + ":"))
        ivcal[x] = int(input("Enter IV:"))
        if ivcal[x] > 31:
            print("\nIv should range from 0 to 31... please try again")
            allStats()
        evcal[x] = int(input("Enter EV:"))
        if evcal[x] > 255:
            print("\nEV should range from 0 to 255... please try again")
            allStats()
        add_stat[x] = int(input("Desired increased in" + stat_type[x] + ":"))
        x = x + 1

    check_ev = ev[0] + ev[1] + ev[2] + ev[3] + ev[4] + ev[5]
    if check_ev > 510:
        print("\nInput value should not exceed 510 when totaled! please try again.")
        allStats()

    ev_needed = script_2.pokemonEv.allStatsFunction(lvl,base,ivcal,evcal,add_stat,nature)

    print("Pokemon's nature: Jolly(inc. Stat in speed, while dec. stat in Sp.Atk)")
    print("\nThe EVs needed to increase in: \n")
    
    for i in range(len(stat_type)):
        print(stat_type[i], ":", round(ev_needed[i], 2))
        i = i + 1

    anotherCalculation()



def anotherCalculation():
    while True:
        print("""
        1. Perform another calculation
        2. End
        """)
        opt = int(input("Choose an option:"))
        if opt == 1:
            start()
        if opt == 2:
            exit()
        print("Invalid Choice, please try again")

start()