"""
Format of file:

CELL_TO_TARGET
DEFAULT_NUMBER
EXPR:VALUE

Example of file:

J3
0
Horseback Hourly (Average Speed):8.04672
Horseback Hourly (Maximum Speed):64.3738
Trireme (Maximum Speed):13.6794

Format of IF chain:

=IF(J3="Horseback Hourly (Average Speed)",8.04672,IF(J3="Horseback Hourly
(Maximum Speed)",64.3738,IF(J3="Trireme (Maximum Speed)",13.6794,IF(J3="Chinese
Junk (Maximum Speed)",25.7495,IF(J3="Caravel Hourly (Average
Speed)",7.24205,IF(J3="Caravel Hourly (Maximum Speed)",14.4841,IF(J3="Steamship
Hourly (Average Speed)",40.2336,IF(J3="Kayak Hourly (Average
Speed)",5.6327,IF(J3="Kayak Hourly (Maximum Speed)",8.04672,IF(J3="By Pigeon
Hourly (Average Speed)",80.4672,IF(J3="By Pigeon Hourly (Maximum
Speed)",144.841,0)))))))))))

Initial:
=IF({CELL}=\"{EXPR}\",{VALUE},{IF-CHAIN})

Middle / IF-CHAIN:
IF({CELL}=\"{EXPR}\",{VALUE},{IF-CHAIN})

End:
IF({CELL}=\"{EXPR}\",{VALUE},{DEFAULT-END})
"""

IF_CHAIN = "IF({CELL}=\"{expr}\",{value},{if_chain})"
INITIAL_IF = "=" + IF_CHAIN
FINAL_IF = "IF({CELL}=\"{expr}\",{value},{DEFAULT_VALUE})"
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
                CELL=CELL,
                expr=expr,
                value=value,
                if_chain="{if_chain}"
            )
        elif i + 1 == length:
            # print("Last line!")
            end_result = end_result.format(
                if_chain = FINAL_IF.format(
                    CELL=CELL,
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