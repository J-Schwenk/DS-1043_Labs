import json
import statistics


def check_none(dictionary: dict) -> bool:
    for x in dictionary:
        if x is None:
            return True
    return False

def most_temp_stable() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 10**99
    val4 = 10**98
    val3 = 10**97
    val2 = 10**96
    val1 = 10**95
    for x in range(0,numsets):
        try:
            weather = data[x]['noaa']
            stats = [weather['temp-jan'],weather['temp-apr'],weather['temp-jul'],weather['temp-oct']]
            var = statistics.variance(stats)
            if var < val5:
                if var < val4:
                    if var < val3:
                        if var < val2:
                            if var < val1:
                                val1 = var
                                loc1 = x
                            else:
                                val2 = var
                                loc2 = x
                        else:
                            val3 = var
                            loc3 = x
                    else:
                        val4 = var
                        loc4 = x
                else:
                    val5 = var
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def least_temp_stable() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 0
    val4 = 0
    val3 = 0
    val2 = 0
    val1 = 0
    for x in range(0, numsets):
        try:
            weather = data[x]['noaa']
            stats = [weather['temp-jan'],weather['temp-apr'],weather['temp-jul'],weather['temp-oct']]
            var = statistics.variance(stats)
            if var > val5:
                if var > val4:
                    if var > val3:
                        if var > val2:
                            if var > val1:
                                val1 = var
                                loc1 = x
                            else:
                                val2 = var
                                loc2 = x
                        else:
                            val3 = var
                            loc3 = x
                    else:
                        val4 = var
                        loc4 = x
                else:
                    val5 = var
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def fastest_growing() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 0
    val4 = 0
    val3 = 0
    val2 = 0
    val1 = 0
    for x in range(0,numsets):
        try:
            pops = data[x]['population']
            diff = (pops['2019']-pops['2010'])/pops['2010']*100
            if diff > val5:
                if diff > val4:
                    if diff > val3:
                        if diff > val2:
                            if diff > val1:
                                val1 = diff
                                loc1 = x
                            else:
                                val2 = diff
                                loc2 = x
                        else:
                            val3 = diff
                            loc3 = x
                    else:
                        val4 = diff
                        loc4 = x
                else:
                    val5 = diff
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def fastest_declining() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 10**99
    val4 = 10**98
    val3 = 10**97
    val2 = 10**96
    val1 = 10**95
    for x in range(0,numsets):
        try:
            pops = data[x]['population']
            diff = (pops['2019']-pops['2010'])/pops['2010']*100
            if diff < val5:
                if diff < val4:
                    if diff < val3:
                        if diff < val2:
                            if diff < val1:
                                val1 = diff
                                loc1 = x
                            else:
                                val2 = diff
                                loc2 = x
                        else:
                            val3 = diff
                            loc3 = x
                    else:
                        val4 = diff
                        loc4 = x
                else:
                    val5 = diff
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def deadliest() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 0
    val4 = 0
    val3 = 0
    val2 = 0
    val1 = 0
    for x in range(0,numsets):
        try:
            death = data[x]['deaths']
            pops = data[x]['population']
            pop = pops['2019']
            suicides = death['suicides']
            if suicides == None:
                suicides = 0
            homicides = death['homicides']
            if homicides == None:
                homicides = 0
            vehicle = death['vehicle']
            if vehicle == None:
                vehicle = 0
            total = (suicides+homicides+vehicle)/pop*100
            if total > val5:
                if total > val4:
                    if total > val3:
                        if total > val2:
                            if total > val1:
                                val1 = total
                                loc1 = x
                            else:
                                val2 = total
                                loc2 = x
                        else:
                            val3 = total
                            loc3 = x
                    else:
                        val4 = total
                        loc4 = x
                else:
                    val5 = total
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol


def safest() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 10**99
    val4 = 10**98
    val3 = 10**97
    val2 = 10**96
    val1 = 10**95
    for x in range(0,numsets):
        try:
            death = data[x]['deaths']
            pops = data[x]['population']
            pop = pops['2019']
            suicides = death['suicides']
            homicides = death['homicides']
            vehicle = death['vehicle']
            total = (suicides+homicides+vehicle)/pop*100
            if total < val5:
                if total < val4:
                    if total < val3:
                        if total < val2:
                            if total < val1:
                                val1 = total
                                loc1 = x
                            else:
                                val2 = total
                                loc2 = x
                        else:
                            val3 = total
                            loc3 = x
                    else:
                        val4 = total
                        loc4 = x
                else:
                    val5 = total
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def most_educated() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 0
    val4 = 0
    val3 = 0
    val2 = 0
    val1 = 0
    for x in range(0,numsets):
        education = data[x]['edu']
        try:
            grads = education['bachelors+']
            if grads > val5:
                if grads > val4:
                    if grads > val3:
                        if grads > val2:
                            if grads > val1:
                                val1 = grads
                                loc1 = x
                            else:
                                val2 = grads
                                loc2 = x
                        else:
                            val3 = grads
                            loc3 = x
                    else:
                        val4 = grads
                        loc4 = x
                else:
                    val5 = grads
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def least_educated() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 10**99
    val4 = 10**98
    val3 = 10**97
    val2 = 10**96
    val1 = 10**95
    for x in range(0,numsets):
        education = data[x]['edu']
        try:
            grads = education['bachelors+']
            if grads < val5:
                if grads < val4:
                    if grads < val3:
                        if grads < val2:
                            if grads < val1:
                                val1 = grads
                                loc1 = x
                            else:
                                val2 = grads
                                loc2 = x
                        else:
                            val3 = grads
                            loc3 = x
                    else:
                        val4 = grads
                        loc4 = x
                else:
                    val5 = grads
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def skewed_female() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 0
    val4 = 0
    val3 = 0
    val2 = 0
    val1 = 0
    for x in range(0,numsets):
        try:
            tot = data[x]['male']+data[x]['female']
            skew = data[x]['female']/tot*100
            if skew > val5:
                if skew > val4:
                    if skew > val3:
                        if skew > val2:
                            if skew > val1:
                                val1 = skew
                                loc1 = x
                            else:
                                val2 = skew
                                loc2 = x
                        else:
                            val3 = skew
                            loc3 = x
                    else:
                        val4 = skew
                        loc4 = x
                else:
                    val5 = skew
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def skewed_male() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 0
    val4 = 0
    val3 = 0
    val2 = 0
    val1 = 0
    for x in range(0,numsets):
        try:
            tot = data[x]['male']+data[x]['female']
            skew = data[x]['male']/tot*100
            if skew > val5:
                if skew > val4:
                    if skew > val3:
                        if skew > val2:
                            if skew > val1:
                                val1 = skew
                                loc1 = x
                            else:
                                val2 = skew
                                loc2 = x
                        else:
                            val3 = skew
                            loc3 = x
                    else:
                        val4 = skew
                        loc4 = x
                else:
                    val5 = skew
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def oldest_county() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 0
    val4 = 0
    val3 = 0
    val2 = 0
    val1 = 0
    for x in range(0,numsets):
        ages = data[x]['age']
        try:
            elderly = ages['65-69']+ages['70-74']+ages['75-79']+ages['80-84']+ages['85+']
            elderly = elderly*100
            if elderly > val5:
                if elderly > val4:
                    if elderly > val3:
                        if elderly > val2:
                            if elderly > val1:
                                val1 = elderly
                                loc1 = x
                            else:
                                val2 = elderly
                                loc2 = x
                        else:
                            val3 = elderly
                            loc3 = x
                    else:
                        val4 = elderly
                        loc4 = x
                else:
                    val5 = elderly
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def youngest_county() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 0
    val4 = 0
    val3 = 0
    val2 = 0
    val1 = 0
    for x in range(0,numsets):
        ages = data[x]['age']
        try:
            youth = ages['0-4']+ages['5-9']+ages['10-14']+ages['15-19']
            youth = youth*100
            if youth > val5:
                if youth > val4:
                    if youth > val3:
                        if youth > val2:
                            if youth > val1:
                                val1 = youth
                                loc1 = x
                            else:
                                val2 = youth
                                loc2 = x
                        else:
                            val3 = youth
                            loc3 = x
                    else:
                        val4 = youth
                        loc4 = x
                else:
                    val5 = youth
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def most_age_diverse() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 10**99
    val4 = 10**98
    val3 = 10**97
    val2 = 10**96
    val1 = 10**95
    for x in range(0,numsets):
        ages = data[x]['age']
        try:
            stats = [ages['0-4'],ages['5-9'],ages['10-14'],ages['15-19'],ages['20-24'],ages['25-29'],ages['30-34'],ages['35-39'],ages['40-44'],ages['45-49'],ages['50-54'],ages['55-59'],ages['60-64'],ages['65-69'],ages['70-74'],ages['75-79'],ages['80-84'],ages['85+']]
            var = statistics.variance(stats)
            if var < val5:
                if var < val4:
                    if var < val3:
                        if var < val2:
                            if var < val1:
                                val1 = var
                                loc1 = x
                            else:
                                val2 = var
                                loc2 = x
                        else:
                            val3 = var
                            loc3 = x
                    else:
                        val4 = var
                        loc4 = x
                else:
                    val5 = var
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def highest_employed() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 0
    val4 = 0
    val3 = 0
    val2 = 0
    val1 = 0
    for x in range(0,numsets):
        try:
            skew = data[x]['bls']['2020']['employed']/data[x]['bls']['2020']['labor_force']*100
            if skew > val5:
                if skew > val4:
                    if skew > val3:
                        if skew > val2:
                            if skew > val1:
                                val1 = skew
                                loc1 = x
                            else:
                                val2 = skew
                                loc2 = x
                        else:
                            val3 = skew
                            loc3 = x
                    else:
                        val4 = skew
                        loc4 = x
                else:
                    val5 = skew
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def highest_unemployed() -> str:
    with open('counties.json', 'r') as file:
        data = json.load(file)
    numsets = len(data)
    val5 = 0
    val4 = 0
    val3 = 0
    val2 = 0
    val1 = 0
    for x in range(0,numsets):
        try:
            skew = data[x]['bls']['2020']['unemployed']/data[x]['bls']['2020']['labor_force']*100
            if skew > val5:
                if skew > val4:
                    if skew > val3:
                        if skew > val2:
                            if skew > val1:
                                val1 = skew
                                loc1 = x
                            else:
                                val2 = skew
                                loc2 = x
                        else:
                            val3 = skew
                            loc3 = x
                    else:
                        val4 = skew
                        loc4 = x
                else:
                    val5 = skew
                    loc5 = x
        except: continue
    sol = ((data[loc1]['name'],data[loc1]['state'], val1), (data[loc2]['name'],data[loc2]['state'], val2), (data[loc3]['name'],data[loc3]['state'], val3), (data[loc4]['name'],data[loc4]['state'], val4),(data[loc5]['name'],data[loc5]['state'], val5))
    return sol

def data_to_file(file_var,data_list,description):
    ties = check_ties(data_list)
    if ties == 1:
        name = data_list[0][0]
        state = data_list[0][1]
        file_var.write(name+", "+state+" is the county "+description+"\n")
    elif ties == 2:
        name1 = data_list[0][0]
        state1 = data_list[0][1]
        name2 = data_list[1][0]
        state2 = data_list[1][1]
        file_var.write(name1+", "+state1+" and "+name2+", "+state2+ " are the counties "+description+"\n")
    elif ties > 2:
        writestr = ""
        for x in range(0,5):
            if x < ties-1:
                writestr = writestr +data_list[x][0]+", "+data_list[x][1]+", "
            elif x == ties-1:
                writestr = writestr + "and " + data_list[x][0] + ", " + data_list[x][1] + " are the counties "+description+"\n"
        file_var.write(writestr)


def check_ties(data_list):
    data1 = data_list[0][2]
    data2 = data_list[1][2]
    data3 = data_list[2][2]
    data4 = data_list[3][2]
    data5 = data_list[4][2]
    if data1 == data2:
        if data2 == data3:
            if data3 == data4:
                if data4 == data5:
                    return(5)
                else: return(4)
            else: return(3)
        else: return(2)
    else: return(1)

def table_creator(file_var,data_list,data_type,round_val):
    writestr = "| County | "+data_type+" |"+"\n"
    writestr = writestr+"| :---: | :---: |\n"
    for x in range(0,5):
        writestr = writestr+"| "+data_list[x][0]+", "+data_list[x][1]+" | "+str(round(data_list[x][2],round_val))+" |\n"
    file_var.write(writestr)

def function_write(file_var,func,header,description,data_type,round_val):
    file_var.write("### "+header+"\n")
    data_to_file(file_var,func,description)
    file_var.write("\n")
    table_creator(file_var,func,data_type,round_val)
    file_var.write("\n")

file = open("report.md","w")

file.write("# Lab 6 - Data Scavenger Hunt\n")
function_write(file,most_temp_stable(),"Most Temperature Stability","with the most temperature stability","Temperature Variance",1)
function_write(file,least_temp_stable(),"Least Temperature Stability","with the least temperature stability","Temperature Variance",1)
function_write(file,fastest_growing(),"Highest Population Growth (2010-19)","with the highest population growth","Population Change (%)",1)
function_write(file,fastest_declining(),"Greatest Population Decline (2010-19)","with the greatest population decline","Population Change (%)",1)
function_write(file,deadliest(),"Deadliest","with the highest unnatural death rate","Unnatural Death (%)",3)
function_write(file,safest(),"Safest","with the lowest unnatural death rate","Unnatural Death (%)",3)
function_write(file,most_educated(),"Most Educated","with the highest percentage of college graduates","College Graduates (%)",1)
function_write(file,least_educated(),"Least Educated","with the lowest percentage of college graduates","College Graduates (%)",1)
function_write(file,skewed_female(),"Most Females","with the highest percentage of females","Females (%)",1)
function_write(file,skewed_male(),"Most Males","with the highest percentage of males","Males (%)",1)
function_write(file,oldest_county(),"Oldest","with the highest percentage of population over 65","Population Over 65 (%)",1)
function_write(file,youngest_county(),"Youngest","with the highest percentage of population under 20","Population Under 20 (%)",1)
function_write(file,most_age_diverse(),"Most Age Diverse","with the highest age diversity","Age Variance",6)
function_write(file,highest_employed(),"Highest Employment","with the highest employment rate","Employment (%)",1)
function_write(file,highest_unemployed(),"Highest Unemployment","with the highest unemployment rate","Unemployment (%)",1)