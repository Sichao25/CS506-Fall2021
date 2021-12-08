def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    file=open(csv_file_path,"r")
    data=[]
    for line in file:
        row = []
        elements = line.strip().replace('"', '').split(",")
        for e in elements:
            if e.isdecimal():
                row.append(int(e))
            elif e.isdigit():
                row.append(float(e))
            else:
                row.append(str(e))
        data.append(row)
    return data
