import datetime as dt

n2wdict_de = {
    1: 'eins',
    2: 'zwei',
    3: 'drei',
    4: 'vier',
    5: 'fünf',
    6: 'sechs',
    7: 'sieben',
    8: 'acht',
    9: 'neun',
    10: 'zehn',
    11: 'elf',
    12: 'zwölf',
}

def num2word(number: int) -> str:
    if number<13:
        return n2wdict_de[number]
    return str(number)

def hour2word(hour: int, language: str = 'de'):
    hour = hour%12
    if hour == 0:
        hour = 12
    match language:
        case 'de':
            return n2wdict_de[hour]
        case _:
            return "unbekannte Sprache"

def time2words(t: dt.datetime, language: str = 'de') -> str:
    if t.minute in (1,16,31,46):
        return shortly_past(minute=t.minute,hour=t.hour, languague=language)
    if t.minute in (14,29,44,59):
        return shortly_before(minute=t.minute,hour=t.hour, languague=language)
    if t.minute in (0,15,30,45):
        return quarter_hours(minute=t.minute,hour=t.hour, languague=language)
    if t.minute < 21:
        return minutes_past(minute=t.minute,hour=t.hour, languague=language)
    if 20 < t.minute < 30:
        return minutes_to_half(minute=t.minute,hour=t.hour, languague=language)
    if 30 < t.minute < 40:
        return minutes_past_half(minute=t.minute,hour=t.hour, languague=language)
    if t.minute == 40:
        return minutes_to(minute=t.minute,hour=t.hour, languague=language)
    if 47 < t.minute < 60:
        return minutes_to(minute=t.minute,hour=t.hour, languague=language)
    return minute_time(minute=t.minute,hour=t.hour, languague=language)

def minute_time(minute: int, hour: int, languague: str = 'de') -> str:
    match languague:
        case 'de':
            return f"{hour2word(hour=hour)} Uhr {num2word(minute)}"
        case _:
            return "unbekannte Sprache"

def minutes_past(minute: int, hour: int, languague: str = 'de') -> str:
    match languague:
        case 'de':
            return f"{num2word(minute)} nach {hour2word(hour=hour)}"
        case _:
            return "unbekannte Sprache"

def minutes_to(minute: int, hour: int, languague: str = 'de') -> str:
    minutes = 60 - minute
    match languague:
        case 'de':
            return f"{num2word(minutes)} vor {hour2word(hour=hour+1)}"
        case _:
            return "unbekannte Sprache"

def minutes_to_half(minute: int, hour: int, languague: str = 'de') -> str:
    minutes = 30 - minute
    match languague:
        case 'de':
            return f"{num2word(minutes)} vor halb {hour2word(hour=hour+1)}"
        case _:
            return "unbekannte Sprache"

def minutes_past_half(minute: int, hour: int, languague: str = 'de') -> str:
    minute = minute - 30
    match languague:
        case 'de':
            return f"{num2word(minute)} nach halb {hour2word(hour=hour+1)}"
        case _:
            return "unbekannte Sprache"

def quarter_hours(minute: int, hour: int, languague: str = 'de') -> str:
    match languague:
        case 'de':
            if minute == 0:
                return f"{hour2word(hour=hour)} Uhr"
            elif minute == 15:
                return f"viertel nach {hour2word(hour=hour)}"
            elif minute == 30:
                return f"halb {hour2word(hour=hour+1)}"
            elif minute == 45:
                return f"viertel vor {hour2word(hour=hour+1)}"
        case _:
            return "unbekannte Sprache"

def shortly_past(minute: int, hour: int, languague: str = 'de') -> str:
    match languague:
        case 'de':
            if minute < 15:
                return f"kurz nach {hour2word(hour=hour)}"
            elif minute < 30:
                return f"kurz nach viertel nach {hour2word(hour=hour)}"
            elif minute < 45:
                return f"kurz nach halb {hour2word(hour=hour+1)}"
            elif minute < 60:
                return f"kurz vor {hour2word(hour=hour+1)}"
        case _:
            return "unbekannte Sprache"

def shortly_before(minute: int, hour: int, languague: str = 'de') -> str:
    match languague:
        case 'de':
            if minute < 15:
                return f"kurz vor viertel nach {hour2word(hour=hour)}"
            elif minute < 30:
                return f"kurz halb {hour2word(hour=hour+1)}"
            elif minute < 45:
                return f"kurz vor viertel vor {hour2word(hour=hour+1)}"
            elif minute < 60:
                return f"kurz vor {hour2word(hour=hour+1)}"
        case _:
            return "unbekannte Sprache"


def main():
    pass

if __name__=="__main__":
    main()