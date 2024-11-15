#7. Write a Python program to print the the first alphabet pattern 'A-Z' in your name

alphabet_patterns = {
    'A': [
        "   *   ",
        "  * *  ",
        " ***** ",
        " *   * ",
        " *   * ",
    ],
    'B': [
        " ****  ",
        " *   * ",
        " ****  ",
        " *   * ",
        " ****  ",
    ],
    'C': [
        "  **** ",
        " *     ",
        " *     ",
        " *     ",
        "  **** ",
    ],
    'D': [
        " ****  ",
        " *   * ",
        " *   * ",
        " *   * ",
        " ****  ",
    ],
    'E': [
        " ***** ",
        " *     ",
        " ***** ",
        " *     ",
        " ***** ",
    ],
    'F': [
        " ***** ",
        " *     ",
        " ***** ",
        " *     ",
        " *     ",
    ],
    'G': [
        "  **** ",
        " *     ",
        " *  ** ",
        " *   * ",
        "  ***  ",
    ],
    'H': [
        " *   * ",
        " *   * ",
        " ***** ",
        " *   * ",
        " *   * ",
    ],
    'I': [
        " ***** ",
        "   *   ",
        "   *   ",
        "   *   ",
        " ***** ",
    ],
    'J': [
        " ***** ",
        "    *  ",
        "    *  ",
        " *  *  ",
        "  **   ",
    ],
    'K': [
        " *   * ",
        " *  *  ",
        " ***   ",
        " *  *  ",
        " *   * ",
    ],
    'L': [
        " *     ",
        " *     ",
        " *     ",
        " *     ",
        " ***** ",
    ],
    'M': [
        " *   * ",
        " ** ** ",
        " * * * ",
        " *   * ",
        " *   * ",
    ],
    'N': [
        " *   * ",
        " **  * ",
        " * * * ",
        " *  ** ",
        " *   * ",
    ],
    'O': [
        "  ***  ",
        " *   * ",
        " *   * ",
        " *   * ",
        "  ***  ",
    ],
    'P': [
        " ****  ",
        " *   * ",
        " ****  ",
        " *     ",
        " *     ",
    ],
    'Q': [
        "  ***  ",
        " *   * ",
        " * * * ",
        " *  ** ",
        "  **** ",
    ],
    'R': [
        " ****  ",
        " *   * ",
        " ****  ",
        " *  *  ",
        " *   * ",
    ],
    'S': [
        "  **** ",
        " *     ",
        "  ***  ",
        "     * ",
        " ****  ",
    ],
    'T': [
        " ***** ",
        "   *   ",
        "   *   ",
        "   *   ",
        "   *   ",
    ],
    'U': [
        " *   * ",
        " *   * ",
        " *   * ",
        " *   * ",
        "  ***  ",
    ],
    'V': [
        " *   * ",
        " *   * ",
        " *   * ",
        "  * *  ",
        "   *   ",
    ],
    'W': [
        " *   * ",
        " *   * ",
        " * * * ",
        " ** ** ",
        " *   * ",
    ],
    'X': [
        " *   * ",
        "  * *  ",
        "   *   ",
        "  * *  ",
        " *   * ",
    ],
    'Y': [
        " *   * ",
        "  * *  ",
        "   *   ",
        "   *   ",
        "   *   ",
    ],
    'Z': [
        " ***** ",
        "    *  ",
        "   *   ",
        " *     ",
        " ***** ",
    ],
}

name = input("enter your first letter in your name:")
name= name.upper()
if name in alphabet_patterns:
  for i in alphabet_patterns[name]:
    print(i)
