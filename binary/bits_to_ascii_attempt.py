# break entire strings into individual byte strings
separated_bytes = []
number_of_bytes = round(len(binary_text)/8)
i = 0
while(i < number_of_bytes*8):
  separated_bytes.append(binary_text[i:i+8])
  i += 8

# turn individual byte string into integer
def byte_to_integer(byteString):
  bits = []
  powers_of_2 = [128,64,32,16,8,4,2,1]
  for char in byteString:
    if(char == "1"):
      bits.append(1)
    else:
      bits.append(0)
  bits = [0,1,0,0,1,1,1,0]
  output_integer = 0
  for i in range(8):
    output_integer += bits[i] * powers_of_2[i]
  return output_integer

# turn integer into ASCII character
def integer_to_character(integer_to_character):
  return chr(integerValue)
  
# put all of the individual characters together into a message string
outputString = ""
for byte in separated_bytes:
  characterString = ""
  integerValue = byte_to_integer(byte)
  characterString = integer_to_character(integerValue)
  outputString += characterString

# print out the final string
print(outputString)
