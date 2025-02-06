import time
x = 5
ma_variable_globale = "variable globale"

def ma_fonction(ma_variable_argument):
    ma_variable_locale = "variable locale"
    for i in range(3):
        print(ma_variable_globale)
        print(ma_variable_argument)
        print(ma_variable_locale)
        time.sleep(1)

ma_fonction("variable argument")
# ceci est un test de github
