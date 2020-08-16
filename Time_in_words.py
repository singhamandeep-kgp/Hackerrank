def timeInWords(h, m):
    my_dict = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty"}
    hour = my_dict[h]
    if m == 0:
        return ("%s o' clock" % (hour))
    if m == 1:
        return ("%s minute past %s" % (my_dict[m], hour))
    elif m == 15:
        return ("quarter past %s" % (hour))
    elif m == 30:
        return ("half past %s" % (hour))
    elif m == 45:
        return ("quarter to %s" % (my_dict[h+1]))
    elif m < 30:
        if m <= 20:
            return ("%s minutes past %s" % (m, hour))
        elif m > 20:
            return ("%s minutes past %s" % (" ".join("twenty",my_dict[m%10]), hour))
    elif m > 30:
        if m < 40:
            return ("%s minutes to %s" % (" ".join("twenty",my_dict[(60-m)%10]), (my_dict[h + 1])))
        elif m == 59:
            return ("%s minute to %s" % (my_dict[(60-m)], my_dict[(h+1)]))
        elif m >= 40:
            return ("%s minutes to %s" % (my_dict[(60-m)], my_dict[(h+1)]))

print(timeInWords(1,1))