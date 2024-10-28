def var_type(var):
    completed = False
    if not completed:
        check = isinstance(var,int)
        if check:
            return(int)
    if not completed:
        check = isinstance(var,bool)
        if check:
            return(bool)
    if not completed:
        check = isinstance(var,float)
        if check:
            return(float)
    if not completed:
        check = isinstance(var,str)
        if check:
            return(str)

def alignment(type,width) -> str:
    return(left_colon(type)+"-"*(width-2)+right_colon(type))

def left_colon(type) -> str:
    if type == int:
        return("-")
    elif type == float:
        return("-")
    elif type == str:
        return(":")
    elif type == bool:
        return(":")

def right_colon(type) -> str:
    if type == int:
        return(":")
    elif type == float:
        return(":")
    elif type == str:
        return(":")
    elif type == bool:
        return(":")

def min_width(headers, rows) -> list:
    widths = []
    for i in range(0,len(headers)):
        header_width = len(str(headers[i]))
        row_width = 0
        for n in rows[i]:
            check = len(str(n))
            if check>row_width:
                row_width = check
        if row_width>header_width:
            widths.append(row_width)
        else: widths.append(header_width)
    return(widths)

def left_spaces(width,string) -> str:
    return(" "*(width-len(str(string)))+str(string))

def right_spaces(width,string) -> str:
    return(str(string)+" "*(width-len(str(string))))

def center_spaces(width,string) -> str:
    if (width-len(string))%2 == 0:
        nums = int((width-len(str(string)))/2)
        left = " "*nums
        right = " "*nums
    else:
        nums = int(round((width-len(str(string)))/2))
        left = " "*nums+" "
        right = " "*nums
    return(left+str(string)+right)

def view_table(headers, rows):
    file = open("lab7report.md","w")
    width = min_width(headers,rows)
    header_str = "| "
    for i in range(0,len(headers)):
        var = var_type(headers[i])
        if var == float:
            header = round(headers[i],2)
        else: header = headers[i]
        if var_type(rows[i][0]) == float:
            header_str = header_str + left_spaces(width[i],header)+ " | "
        elif var_type(rows[i][0]) == int:
            header_str = header_str + left_spaces(width[i],header)+ " | "
        elif var_type(rows[i][0]) == str:
            header_str = header_str + center_spaces(width[i],header)+ " | "
        elif var_type(rows[i][0]) == bool:
            header_str = header_str + center_spaces(width[i],header)+ " | "
    file.write(header_str)
    file.write("\n")
    alignment_str = "| "
    for i in range(0,len(headers)):
        alignment_str = alignment_str + alignment(var_type(rows[i][0]),width[i]) + " | "
    file.write(alignment_str)
    file.write("\n")
    for n in range(0,len(rows[0])):
        row_str = "| "
        for i in range(0,len(rows)):
            if var_type(rows[i][n]) == float:
                row_str = row_str + left_spaces(width[i],str(rows[i][n]))+ " | "
            elif var_type(rows[i][n]) == int:
                row_str = row_str + left_spaces(width[i],str(rows[i][n]))+ " | "
            elif var_type(rows[i][n]) == str:
                row_str = row_str + center_spaces(width[i],str(rows[i][n]))+ " | "
            elif var_type(rows[i][n]) == bool:
                row_str = row_str + center_spaces(width[i],str(rows[i][n]))+ " | "
        file.write(row_str)
        file.write("\n")

def merge_sorted_lists(lists):
    num_lists = len(lists)
    final_list = lists[0]
    if num_lists == 1:
        raise Exception("Must input more than one list to be sorted")
    for x in range(1,num_lists):
        new_list = []
        loc = 0
        for var in range(0,len(final_list)):
            next_var = False
            while not next_var:
                if loc < len(lists[x]):
                    if final_list[var] < lists[x][loc]:
                        next_var = True
                        new_list = new_list + [final_list[var]]
                        if var == len(final_list) - 1:
                            for aloc in range(loc,len(lists[x])):
                                new_list = new_list + [lists[x][aloc]]
                    else:
                        new_list = new_list + [lists[x][loc]]
                        if final_list[var] < lists[x][loc]:
                            next_var = True
                            if var == len(final_list) - 1:
                                new_list = new_list+[final_list[var]]
                        loc = loc+1
                else:
                    next_var = True
                    new_list = new_list + [final_list[var]]
                    if var == len(final_list) - 1:
                        for aloc in range(loc, len(lists[x])):
                            new_list = new_list + [lists[x][aloc]]
        final_list = new_list
    return(final_list)

def caesar(plaintext: str, rotation:int = 13):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str_length = len(plaintext)
    print(str_length)
    final_str = ""
    for x in range(0,str_length):
        print(x)
        current = plaintext[x]
        check = ""
        letter = -1
        character = False
        lower = True
        upper = False
        while current != check:
            letter = letter+1
            check = lower_alphabet[letter]
            if letter > 25:
                lower = False
                break
        if not lower:
            letter = -1
            while current != check:
                letter = letter+1
                check = upper_alphabet[letter]
                upper = True
                if letter > 25:
                    upper = False
                    character = False
                    break
        if lower:
            new_letter = letter+rotation
            final_str = final_str + lower_alphabet[new_letter]
        elif upper:
            new_letter = letter+rotation
            final_str = final_str + upper_alphabet[new_letter]
        else: final_str = final_str + current
    return(final_str)
