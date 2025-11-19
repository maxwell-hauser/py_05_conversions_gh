#!/usr/bin/env python3
"""
Chapter 5: Number System Conversions
Demonstrates conversions between binary, decimal, octal, and hexadecimal
"""

def decimal_to_binary(n):
    """Convert decimal to binary using division method"""
    if n == 0:
        return "0"
    
    binary = ""
    steps = []
    original = n
    
    while n > 0:
        remainder = n % 2
        steps.append(f"{n} ÷ 2 = {n // 2} remainder {remainder}")
        binary = str(remainder) + binary
        n //= 2
    
    return binary, steps

def binary_to_hex(binary_str):
    """Convert binary to hexadecimal by grouping 4 bits"""
    # Pad to multiple of 4
    padding = (4 - len(binary_str) % 4) % 4
    binary_str = "0" * padding + binary_str
    
    # Group into 4-bit chunks
    chunks = [binary_str[i:i+4] for i in range(0, len(binary_str), 4)]
    
    # Convert each chunk
    hex_digits = []
    conversion_table = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    
    for chunk in chunks:
        hex_digits.append(conversion_table[chunk])
    
    return ''.join(hex_digits), chunks

def hex_to_binary(hex_str):
    """Convert hexadecimal to binary"""
    conversion = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    
    binary = ""
    for digit in hex_str.upper():
        binary += conversion[digit]
    
    return binary

def decimal_fraction_to_binary(decimal_fraction, max_digits=10):
    """Convert decimal fraction to binary using multiplication method"""
    binary = ""
    steps = []
    value = decimal_fraction
    
    for _ in range(max_digits):
        if value == 0:
            break
        value *= 2
        bit = int(value)
        steps.append(f"{value/2:.6f} × 2 = {value:.6f} → bit = {bit}")
        binary += str(bit)
        value -= bit
    
    return binary, steps

def main():
    print("=" * 60)
    print("CHAPTER 5: Number System Conversions")
    print("=" * 60)
    
    # Example 1: Decimal to Binary
    print("\n--- Example 1: Decimal to Binary (Division Method) ---")
    decimal = 35
    binary, steps = decimal_to_binary(decimal)
    print(f"Convert ({decimal})_10 to binary:")
    for step in steps:
        print(f"  {step}")
    print(f"Reading remainders bottom-to-top: ({binary})_2")
    
    # Example 2: Binary to Hexadecimal
    print("\n--- Example 2: Binary to Hexadecimal ---")
    binary = "001010011010"
    hex_result, chunks = binary_to_hex(binary)
    print(f"Convert ({binary})_2 to hexadecimal:")
    print("Group into 4-bit chunks:")
    for i, chunk in enumerate(chunks):
        hex_digit = hex_result[i]
        decimal_val = int(chunk, 2)
        print(f"  {chunk} = {decimal_val} = {hex_digit}")
    print(f"Result: ({hex_result})_16")
    
    # Example 3: Hexadecimal to Binary
    print("\n--- Example 3: Hexadecimal to Binary ---")
    hex_num = "3D5"
    binary = hex_to_binary(hex_num)
    print(f"Convert ({hex_num})_16 to binary:")
    for digit in hex_num:
        binary_chunk = hex_to_binary(digit)
        print(f"  {digit} → {binary_chunk}")
    print(f"Result: ({binary})_2")
    
    # Example 4: Decimal Fraction to Binary
    print("\n--- Example 4: Decimal Fraction to Binary ---")
    fraction = 0.625
    binary_frac, steps = decimal_fraction_to_binary(fraction)
    print(f"Convert ({fraction})_10 to binary:")
    print("Multiplication method:")
    for step in steps:
        print(f"  {step}")
    print(f"Result: (0.{binary_frac})_2")
    
    # Example 5: Binary to Decimal (with fraction)
    print("\n--- Example 5: Binary to Decimal (with fraction) ---")
    binary = "110111.101"
    integer_part, fraction_part = binary.split('.')
    
    print(f"Convert ({binary})_2 to decimal:")
    print("\nInteger part:")
    int_value = 0
    for i, bit in enumerate(reversed(integer_part)):
        power = i
        bit_val = int(bit) * (2 ** power)
        int_value += bit_val
        print(f"  {bit} × 2^{power} = {bit_val}")
    
    print("\nFractional part:")
    frac_value = 0
    for i, bit in enumerate(fraction_part):
        power = -(i + 1)
        bit_val = int(bit) * (2 ** power)
        frac_value += bit_val
        print(f"  {bit} × 2^{power} = {bit_val:.3f}")
    
    total = int_value + frac_value
    print(f"\nTotal: {int_value} + {frac_value:.3f} = {total:.3f}")
    
    # Example 6: Quick conversion table
    print("\n--- Example 6: Quick Reference Table ---")
    print("Dec | Bin  | Oct | Hex")
    print("----|------|-----|----")
    for i in range(16):
        binary = format(i, '04b')
        octal = format(i, 'o')
        hexadecimal = format(i, 'X')
        print(f" {i:2d} | {binary} |  {octal}  |  {hexadecimal}")
    
    print("\n" + "=" * 60)
    print("Key Concepts:")
    print("- Decimal → Binary: Division by 2 method")
    print("- Binary → Hex: Group 4 bits")
    print("- Hex → Binary: Each hex digit = 4 bits")
    print("- Fractions: Multiply by base, take integer part")
    print("=" * 60)

if __name__ == "__main__":
    main()
