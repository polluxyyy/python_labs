price = float(input("price: ").replace(",", "."))
discount = float(input("discount: ").replace(",", "."))
nalog = float(input("vat: ").replace(",", "."))
base = price * (1 - discount / 100)
fin_nalog = base * nalog / 100
total = base + fin_nalog

print(f"База после скидки: {base:.2f}")
print(f"НДС:               {fin_nalog:.2f}")
print(f"Итого к оплате:    {total:.2f}")
