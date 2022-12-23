def Maketxt(csv_name):
    import csv

    read_csv = csv_name
    XSS_list = []
    normal_list = []

    with open(read_csv, encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        data_list = list(csv_reader)


    for data in data_list:
        if data[0] == "1":
            XSS_list.append(data)
        else:
            normal_list.append(data)


    for normal_data in normal_list:
        txt = normal_data[1]
        rm_txt = txt.replace("\n"," newline ").replace("\t"," tub ")
        add_space_txt = rm_txt.replace("<"," < ").replace(">"," > ").replace("("," ( ").replace(")"," ) ").replace("="," = ").replace(","," , ").replace(";"," ; ")
        normal_list[normal_list.index(normal_data)][1] = add_space_txt.split()


    for XSS_data in XSS_list:
        txt = XSS_data[1]
        rm_txt = txt.replace("\n"," ").replace("\t"," ")
        add_space_txt = rm_txt.replace("<"," < ").replace(">"," > ").replace("("," ( ").replace(")"," ) ").replace("="," = ").replace(","," , ").replace(";"," ; ").replace("\\"," \\ ")
        XSS_list[XSS_list.index(XSS_data)][1] = add_space_txt.split()

    data_list = [normal_list,XSS_list]

    return data_list