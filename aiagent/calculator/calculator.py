import sys

if len(sys.argv) > 1:
    expression = sys.argv[1]
    try:
        result = eval(expression)
        print(result)
    except Exception as e:
        print("Invalid input:", e)
else:
    print("No expression provided")

# Note: When running from the command line, ensure the expression is properly quoted,
# e.g., python calculator.py "3 + 7 * 2"