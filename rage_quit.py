input_text = input().upper()
output_text = ""
variable = ""

for index in range(0, len(input_text)):
    if input_text[index].isdigit():
        if index < len(input_text) - 1:
            if input_text[index+1].isdigit():
                output_text += variable * int(input_text[index] + input_text[index+1])
                variable = ""
            else:
                output_text += variable * int(input_text[index])
                variable = ''
        else:
            output_text += variable * int(input_text[index])
            variable = ''
    elif input_text[index].isalpha():
        variable += input_text[index]
    else:
        variable += input_text[index]
        # output_text += variable

unique_symbols = set(output_text)
print(f"Unique symbols used: {len(unique_symbols)}")
print(output_text)  