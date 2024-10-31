s = """PCQ VMJYPD LBYK LYSO KBXBJXWXV BXV ZCJPO EYPD
KBXBJYUXJ LBJOO KCPK. CP LBO LBCMKXPV XPV IYJKL PYDBL,
QBOP KBO BXV OPVOV LBO LXRO CI SX’XJMI, KBO JCKO XPV
EYKKOV LBO DJCMPV ZOICJO BYS, KXUYPD: “DJOXL EYPD, ICJ X
LBCMKXPV XPV CPO PYDBLK Y BXNO ZOOP JOACMPLYPD LC UCM
LBO IXZROK CI FXKL XDOK XPV LBO RODOPVK CI XPAYOPL EYPDK.
SXU Y SXEO KC ZCRV XK LC AJXNO X IXNCMJ CI UCMJ SXGOKLU?”
OFYRCDMO, LXROK IJCS LBO LBCMKXPV XPV CPO PYDBLK"""


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
cypher = {
    "O": "e",
    "B": "h",
    "X": "a",
    "V": "d",
    "L": "t",
    "E": "k",
    "Y": "i",
    "K": "s",
    "N": "v",
    "S": "m",
    "J": "r",
    "P": "n",
    "D": "g",
    "C": "o",
    "M": "u",
    "U": "y",
    "Z": "b",
    "Q": "w",
    "I": "f",
    "R": "l",
    "G": "j",
    "A": "c",
    "F": "p",
    "W": "x"
}
for key in sorted(cypher):
    print(f"{key}: {cypher[key]}")

for i in range(len(s)):
    if s[i] in cypher:
        print(cypher[s[i]], end="")
    else:
        print(s[i], end="")