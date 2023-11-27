def convert_to_24(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    """return f"{hour:02d}{minute:02d}" """
    p = f'{hour:02d}{minute:02d}'
    print(p)
convert_to_24(3,45,'pm' )