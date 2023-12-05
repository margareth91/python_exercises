def make_sandwich(*additives):
    print(f"\nPrzygotujemy kanapke z ponizszymi dodatkami:")
    for additive in additives:
        print(f"- {additive}")


make_sandwich('serek almette')
make_sandwich('losos wedzony', 'serek almette')
make_sandwich('losos wedzony', 'serek almette', 'ogorek')
make_sandwich('losos wedzony', 'serek almette', 'ogorek', 'ziola')
make_sandwich('losos wedzony', 'serek almette', 'ogorek', 'ziola', 'salata')
