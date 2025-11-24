# Chapter 5: Number System Conversions

## Overview

This chapter provides detailed methods and algorithms for converting numbers between different number systems (binary, octal, decimal, and hexadecimal). Mastering these conversions is essential for working with computer systems and digital electronics.

## Key Concepts

### Conversion Methods Overview

Different conversion strategies depending on source and target bases:
- **Decimal to Any Base:** Division method
- **Any Base to Decimal:** Multiplication/position method
- **Binary ↔ Octal/Hex:** Direct grouping (fast and easy)
- **Between Non-Decimal Bases:** Convert through decimal (or use grouping for binary-related bases)

## Decimal to Binary Conversion

### Division Method (Repeated Division by 2)

**Algorithm:**
1. Divide the decimal number by 2
2. Record the remainder (0 or 1)
3. Divide the quotient by 2
4. Repeat until quotient is 0
5. Read remainders from **bottom to top**

**Example: Convert 25₁₀ to binary**
```
25 ÷ 2 = 12 remainder 1  ↑
12 ÷ 2 = 6  remainder 0  |
6  ÷ 2 = 3  remainder 0  |
3  ÷ 2 = 1  remainder 1  |
1  ÷ 2 = 0  remainder 1  |
                         Read upward
Result: 11001₂
```

**Verification:** (1×16) + (1×8) + (0×4) + (0×2) + (1×1) = 16 + 8 + 1 = 25 ✓

## Binary to Decimal Conversion

### Positional Method (Multiply and Add)

**Algorithm:**
1. Write down the binary number
2. Number positions from right to left, starting at 0
3. Multiply each digit by 2^(position)
4. Sum all the products

**Example: Convert 1101₂ to decimal**
```
Position:  3  2  1  0
Binary:    1  1  0  1
Powers:    8  4  2  1

Calculation: (1×8) + (1×4) + (0×2) + (1×1) = 8 + 4 + 0 + 1 = 13₁₀
```

## Decimal to Hexadecimal Conversion

### Division Method (Repeated Division by 16)

**Algorithm:**
1. Divide by 16, record remainder
2. If remainder ≥ 10, convert to letter (10=A, 11=B, ..., 15=F)
3. Continue dividing quotient by 16
4. Read remainders from bottom to top

**Example: Convert 254₁₀ to hexadecimal**
```
254 ÷ 16 = 15 remainder 14 (E)  ↑
15  ÷ 16 = 0  remainder 15 (F)  |
                                Read upward
Result: FE₁₆
```

**Verification:** (15×16) + (14×1) = 240 + 14 = 254 ✓

## Hexadecimal to Decimal Conversion

### Positional Method

**Algorithm:**
1. Convert any letters to decimal values (A=10, B=11, ..., F=15)
2. Multiply each digit by 16^(position)
3. Sum all products

**Example: Convert 2A3₁₆ to decimal**
```
Position:  2    1    0
Hex:       2    A    3
Decimal:   2    10   3
Powers:    256  16   1

Calculation: (2×256) + (10×16) + (3×1) = 512 + 160 + 3 = 675₁₀
```

## Binary ↔ Hexadecimal Conversion

### Direct Grouping Method (No Decimal Needed!)

**Binary to Hex:**
1. Group binary digits in sets of 4 (from right to left)
2. Add leading zeros if needed
3. Convert each group of 4 bits to one hex digit

**Example: Convert 11010110₂ to hexadecimal**
```
Binary:    1101  0110
           13    6
Hex:       D     6

Result: D6₁₆
```

**Hex to Binary:**
1. Convert each hex digit to 4 binary bits
2. Concatenate all groups

**Example: Convert A5₁₆ to binary**
```
Hex:     A      5
Binary:  1010   0101

Result: 10100101₂
```

## Binary ↔ Octal Conversion

### Direct Grouping Method (Groups of 3)

**Binary to Octal:**
1. Group binary digits in sets of 3 (from right to left)
2. Add leading zeros if needed
3. Convert each group of 3 bits to one octal digit

**Example: Convert 11010110₂ to octal**
```
Binary:  011  010  110
         3    2    6

Result: 326₈
```

**Octal to Binary:**
1. Convert each octal digit to 3 binary bits
2. Concatenate all groups

**Example: Convert 75₈ to binary**
```
Octal:   7    5
Binary:  111  101

Result: 111101₂
```

## Decimal to Octal Conversion

### Division Method (Repeated Division by 8)

**Algorithm:**
1. Divide by 8, record remainder
2. Continue dividing quotient by 8
3. Read remainders from bottom to top

**Example: Convert 100₁₀ to octal**
```
100 ÷ 8 = 12 remainder 4  ↑
12  ÷ 8 = 1  remainder 4  |
1   ÷ 8 = 0  remainder 1  |
                          Read upward
Result: 144₈
```

## Octal to Decimal Conversion

### Positional Method

**Example: Convert 144₈ to decimal**
```
Position:  2   1   0
Octal:     1   4   4
Powers:    64  8   1

Calculation: (1×64) + (4×8) + (4×1) = 64 + 32 + 4 = 100₁₀
```

## Fractional Number Conversions

### Decimal Fraction to Binary

**Multiplication Method:**
1. Multiply fraction by 2
2. Record integer part (0 or 1)
3. Keep fractional part
4. Repeat until fraction is 0 or desired precision reached
5. Read integer parts from **top to bottom**

**Example: Convert 0.625₁₀ to binary**
```
0.625 × 2 = 1.25  → integer part = 1, fraction = 0.25
0.25  × 2 = 0.5   → integer part = 0, fraction = 0.5
0.5   × 2 = 1.0   → integer part = 1, fraction = 0.0

Result: 0.101₂
```

**Verification:** (1×½) + (0×¼) + (1×⅛) = 0.5 + 0 + 0.125 = 0.625 ✓

### Binary Fraction to Decimal

**Example: Convert 0.1011₂ to decimal**
```
Position:  -1   -2   -3   -4
Binary:    1    0    1    1
Powers:    ½    ¼    ⅛    1/16

Calculation: (1×0.5) + (0×0.25) + (1×0.125) + (1×0.0625)
           = 0.5 + 0 + 0.125 + 0.0625 = 0.6875₁₀
```

## Conversion Summary Table

| From → To | Method |
|-----------|--------|
| **Decimal → Binary** | Repeated division by 2 |
| **Decimal → Octal** | Repeated division by 8 |
| **Decimal → Hex** | Repeated division by 16 |
| **Binary → Decimal** | Positional multiplication |
| **Octal → Decimal** | Positional multiplication |
| **Hex → Decimal** | Positional multiplication |
| **Binary → Hex** | Group by 4 bits |
| **Hex → Binary** | Each digit to 4 bits |
| **Binary → Octal** | Group by 3 bits |
| **Octal → Binary** | Each digit to 3 bits |
| **Hex ↔ Octal** | Convert via binary |

## Learning Objectives

By the end of this chapter, you should be able to:
- Convert decimal numbers to binary, octal, and hexadecimal
- Convert from any base back to decimal
- Use direct grouping for binary ↔ hex conversions
- Use direct grouping for binary ↔ octal conversions
- Convert fractional numbers between bases
- Choose the most efficient conversion method
- Verify conversion results

## Python Example

Run the interactive example:

```bash
python ch05_conversions.py
```

### What the Example Demonstrates

1. **Decimal to Binary:** Step-by-step division method
2. **Binary to Decimal:** Positional notation breakdown
3. **Decimal to Hexadecimal:** Division by 16 with letter conversion
4. **Hex to Decimal:** Converting A-F and calculating value
5. **Binary to Hex:** Fast grouping method
6. **Hex to Binary:** Expanding each digit to 4 bits
7. **Binary to Octal:** Grouping by 3 bits
8. **Octal to Binary:** Expanding each digit to 3 bits
9. **Fraction Conversions:** Handling decimal points

### Sample Output

```
============================================================
CHAPTER 5: Number System Conversions
============================================================

--- Example 1: Decimal to Binary (Division Method) ---
Convert (35)₁₀ to binary:
  35 ÷ 2 = 17 remainder 1
  17 ÷ 2 = 8  remainder 1
  8  ÷ 2 = 4  remainder 0
  4  ÷ 2 = 2  remainder 0
  2  ÷ 2 = 1  remainder 0
  1  ÷ 2 = 0  remainder 1
Reading remainders bottom-to-top: (100011)₂
...
```

## Real-World Applications

### Software Development
- **Debugging:** Converting memory addresses between hex and decimal
- **Bit Manipulation:** Converting values to binary for bitwise operations
- **File Formats:** Understanding hexadecimal file headers
- **Network Programming:** IP address conversions

### Computer Architecture
- **Memory Addressing:** Hex addresses to decimal offsets
- **Assembly Language:** Machine code in hexadecimal
- **Register Values:** Binary to hex for readability
- **Instruction Encoding:** Understanding opcodes

### Digital Electronics
- **Logic Design:** Binary representations of circuits
- **Data Sheets:** Specifications often use hex
- **Microcontroller Programming:** Register configuration
- **Protocol Analysis:** Packet data in hex format

### System Administration
- **File Permissions:** Octal (755) to binary to understand rwx
- **Color Codes:** Hex color codes (#FF5733) to RGB
- **MAC Addresses:** Hex notation for hardware addresses
- **IPv6 Addresses:** Hexadecimal notation

## Quick Reference: Powers Table

### Powers of 2 (Binary)
```
2⁰ = 1        2⁸  = 256
2¹ = 2        2⁹  = 512
2² = 4        2¹⁰ = 1024 (1K)
2³ = 8        2¹⁶ = 65536 (64K)
2⁴ = 16       2²⁰ = 1048576 (1M)
2⁵ = 32       2³⁰ = 1073741824 (1G)
2⁶ = 64
2⁷ = 128
```

### Powers of 16 (Hexadecimal)
```
16⁰ = 1
16¹ = 16
16² = 256
16³ = 4096
16⁴ = 65536
```

### Powers of 8 (Octal)
```
8⁰ = 1
8¹ = 8
8² = 64
8³ = 512
8⁴ = 4096
```

## Common Mistakes to Avoid

❌ **Reading remainders top to bottom** (should be bottom to top)  
❌ **Forgetting to pad binary groups** when converting to hex/octal  
❌ **Confusing 8 (digit) with 8₈ (invalid in octal)**  
❌ **Not converting A-F to numbers** when working with hex  
❌ **Mixing up fraction conversion** (multiply vs divide)  
❌ **Dropping leading zeros** in binary representations  

## Key Takeaways

- Multiple methods exist; choose the most efficient for your conversion
- Binary ↔ Hex and Binary ↔ Octal are fastest using direct grouping
- 📐 Division method works for decimal to any base
- Positional method works for any base to decimal
- Always verify your conversions by converting back
- Memorize common values (powers of 2, hex digits A-F)
- Show your work step-by-step to avoid errors

## Practice Exercises

### Basic Conversions
1. Convert 156₁₀ to binary, octal, and hexadecimal
2. Convert 10110101₂ to decimal, octal, and hexadecimal
3. Convert 3A7₁₆ to binary, octal, and decimal
4. Convert 755₈ to binary, hexadecimal, and decimal

### Fractional Conversions
5. Convert 0.75₁₀ to binary
6. Convert 0.1101₂ to decimal
7. Convert 12.625₁₀ to binary

### Applied Problems
8. A memory address is 0x2A4F. What is this in decimal?
9. File permissions are 644₈. What is this in binary?
10. An IP address octet is 11010110₂. What is this in decimal?

### Challenge Problems
11. Convert 999₁₀ to all three bases (binary, octal, hex)
12. What is the hex value of binary 1111111111111111₂?
13. Convert 0.1₁₀ to binary (it's a repeating binary fraction!)

## Further Study

- Practice mental conversions for common values
- Learn about two's complement representation (Chapter 6)
- Study binary arithmetic operations (Chapter 8)
- Explore floating-point representation (Chapter 9)
- Investigate BCD encoding (Chapter 10)

---

**Course Navigation:**  
← Previous: [Chapter 4 - Number Systems](../ch4_number_systems/) | Next: [Chapter 6 - Complements](../ch6_complements/) →

---
<!-- License moved to dedicated LICENSE file -->
