"""
Format of file:

CELL_TO_TARGET
DEFAULT_NUMBER
EXPR:VALUE

Example of file:

J3
0


Format of IF chain:



Initial:
=IF({EXPR},{VALUE},{IF-CHAIN})

Middle / IF-CHAIN:
IF({EXPR},{VALUE},{IF-CHAIN})

End:
IF({EXPR},{VALUE},{DEFAULT-END})
"""

IF_CHAIN = "IF({expr},{value},{if_chain})"
INITIAL_IF = "=" + IF_CHAIN
FINAL_IF = "IF({expr},{value},{DEFAULT_VALUE})"
CELL = None
DEFAULT_VALUE = None

end_result = ""
length = 0  # length of file

file_name = input("File name: ")

with open(file_name, "r") as f:
    length = len(f.readlines())

with open(file_name, "r") as f:
    # length = len(f.readlines())

    for i, line in enumerate(f):
        # print(f"line {i}: {line.strip()}")

        if i == 0:
            CELL = line.strip()
            continue
        elif i == 1:
            DEFAULT_VALUE = line.strip()
            continue

        [expr, value] = line.strip().split(":")
        # that 3 accounts for lines already read
        
        # print(f"length is {length}!")

        if i == 2:
            # First line
            end_result = INITIAL_IF.format(
                # CELL=CELL,
                expr=expr,
                value=value,
                if_chain="{if_chain}"
            )
        elif i + 1 == length:
            # print("Last line!")
            end_result = end_result.format(
                if_chain = FINAL_IF.format(
                    # CELL=CELL,
                    expr=expr,
                    value=value,
                    DEFAULT_VALUE=DEFAULT_VALUE
                )
            )
        else:
            end_result = end_result.format(if_chain = IF_CHAIN.format(
                CELL=CELL, expr=expr, value=value, if_chain="{if_chain}"
            ))
        
        # print(f"debug: end_result = {end_result}")

print(f"End result:\n{end_result}")
