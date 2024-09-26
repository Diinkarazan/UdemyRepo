STR_EXIT = 'exit'
 
# Display result of one conversion
def display_result(val1_f:float, unit1:str, val2_f:float, unit2:str):
    print(f"Conversion: {val1_f} {unit1} = {val2_f} {unit2}")
    print()
 
# Returns a valid float value entered by the user.
# If the exit code is entered, returns this code first.
def get_user_value(unit_s:str):
    while True:
        ans_s = input(f"Please enter a value to convert (in {unit_s}). Type '{STR_EXIT}' to quit the program: ")
 
        if ans_s == STR_EXIT:
            return ans_s
 
        try:
            ans_f = float(ans_s)
        except:
            print("Error : please enter a valid value!")
        else:
            return ans_f
 
# Converter: inch => centimer
def fn_inch_cm(value_f:float) -> float:
    cnv_f = value_f * 2.54
    display_result(value_f, "inch(es)", cnv_f, "cm(s)")
 
# Converter: centimer => inch
def fn_cm_inch(value_f: float) -> float:
    cnv_f = value_f * 0.394
    display_result(value_f, "cm(s)", cnv_f, "inch(es)")
 
# List of available converters
l_converters = [("inch -> centimeters", "inch", fn_inch_cm),
                ("centimeters -> inch", "centimer", fn_cm_inch)]
 
# Returns a converter selected by the user
def select_converter():
    while True:
        index_i = 1
        for item in l_converters:
            print(f"{index_i}. {item[0]}")
            index_i += 1
        try:
            choice_i = int(input("Please select one converter: "))
        except:
            print("Error: please enter a valid number!")
        else:
            if 1 <= choice_i <= len(l_converters):
                return l_converters[choice_i - 1]
            else:
                print("Error: invalid input!")
 
# Main program
converter_item = select_converter()
print()
while True:
    value = get_user_value(converter_item[1])
    if value == STR_EXIT:
        exit(0)
 
    converter_item[2](value)