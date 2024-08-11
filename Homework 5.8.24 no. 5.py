def remove_key_from_dict (dictionary:dict):
    dictionary.popitem()

def clear_all (dictionary:dict):
    dictionary.clear()
a = {'x':1, 'y':2}
remove_key_from_dict(a)
print(a)
clear_all(a)
print(a)

"""
בהפעלת הפונקציה remove_key_from_dict המיולן ישתנה, והאיבר האחרון במילון יימחק. הסיבה לכך היא שפעולת popitem מוציאה את האיבר האחרון מהמילון.
 הפונקציה clear_all לא תשנה את המילון החיצוני, כיוון שהפקודה שניתנה בתוך הפונקציה - {} - לא מוחקת את תוכן המילון, אלא מגדירה מילון חדש וריק. 
 בכדי למחוק את תוכן המילון, יש לבצע את הפעולה שעשיתי כאן - ולהשתמש ב- ()clear. """