with open("C:/intel/singer1.csv", "r") as inFp :
    with open("C:/intel/new_singer2.csv", "w") as outFp:
        header = inFp.readline()
        header = header.strip()
        header_list= header.split(',')
        idx1 = header_list.index('아이디')
        print("idx1", idx1)
        idx2 = header_list.index('이름')
        print("idx2", idx2)
        idx3 = header_list.index('평균 키')
        print("idx3", idx3)
        header_list = [header_list[idx1], header_list[idx2], header_list[idx3]]
        header_str = ','.join(map(str, header_list))
        outFp.write(header_str + '\n')
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            if int(row_list[idx3]) >= 165 :
                row_list = [row_list[idx1], row_list[idx2], row_list[idx3]]
                row_str = ','.join(map(str, row_list))
                outFp.write(row_str + '\n')

print('Save. OK~')