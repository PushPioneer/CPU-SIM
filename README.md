# CPU Emulator
<hr>

## RAM
## CPU


# Instruction set
<hr>

## cpu instructions
  
  | Opcode | Description                              | Usage                                                                                                 |
  |--------|------------------------------------------|-------------------------------------------------------------------------------------------------------|
  | /      | does absolutely nothing                  | /                                                                                                     |
  | /      | Reserved for GPU                         | /                                                                                                     |
  | INC    | adds 1 to data at address or value       | < data  /  address >                                                                                  |
  | DEC    | decreases data at address or value by 1  | < data  /  address >                                                                                  |
  | ADD    | add                                      | < int or addr > to < int or addr > <br/> < output addr >                                              |
  | SUB    | subtract                                 | < int or addr > from < int or addr > <br/> < output addr >                                            |
  | AND    | bit wise and operation                   | < int or addr > < int or addr > < output addr >                                                       |
  | OR     | bit wise or operation                    | < int or addr > < int or addr > < output addr >                                                       |
  | XOR    | bit wise xor operation                   | < int or addr > < int or addr > <br/>< output addr >                                                  |
  | MSG    | prints a text                            | < text or addr > < V for variable (always in text) <br/> VR for raw data (var) <br/> T used for text> |
  | PUSH   | overwrites value at memory address       | < int or addr > < dst >                                                                               |
  | POP    | clears data at memory address            | < dst >                                                                                               |
  | MOV    | switches values at src and dst           | < src > < dst >                                                                                       |
  | IN     | waits for input, input gets saved in var | < var >                                                                                               |
  | BS     | bit shift                                | < operand  <<< for left <br/> >>> for right > < var / addr >                                          |
  | NOT    | bitwise not                              | < int or addr > < output addr >                                                                       |


# language reference
<hr>

