import datetime
from dateutil.parser import parse

def stringToDate(data_str):
    dia = int(data_str[0:2])
    mes = int(data_str[3:4])
    ano = int(data_str[0:4])
    data = datetime.datetime(ano, mes, dia)
    return data

def dateToString(data_obj):
    dia = data_obj.strftime("%d")
    mes = data_obj.strftime("%m")
    ano =data_obj.strftime("%Y")
    return str("{}-{}-{}".format(ano,mes,dia))

def timeToString(time_obj):
    hora = time_obj.strftime("%H")
    minuto = time_obj.strftime("%M")
    return str("{}:{}".format(hora,minuto))


def stringToDatetime(time_str):
    datetime_format = "%Y-%m-%d - %H:%M"
    return datetime.datetime.strptime(time_str, datetime_format)
    #return parse(time_str)

def stringToTime(time_str):
    datetime_format = "%H:%M"
    return datetime.time(int(time_str[:2]),int(time_str[3:]))
    #return parse(time_str)

def stringToBinary(url_str):
    #print(' '.join(format(ord(x), 'b') for x in a))
    return url_str.encode('utf-8')
    

def binaryToString(url_bin):
    if url_bin:
        return url_bin.decode('utf-8')
    return None
    