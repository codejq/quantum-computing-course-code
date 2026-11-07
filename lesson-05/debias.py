# von Neumann debiasing: turns biased but independent bits into fair bits
# Sommerfeld International Academy · made by Quantum Billing · s-i-u.com

def von_neumann(bits):
    """bits: a string or list of '0'/'1'. Pairs 01 -> 0, 10 -> 1, 00 and 11 are thrown away."""
    out = []
    for a, b in zip(bits[::2], bits[1::2]):
        if a != b:
            out.append(a)
    return "".join(out)

if __name__ == "__main__":
    raw = "0111100010011011"        # paste the bits from your quantum computer here
    print(raw, "->", von_neumann(raw))
