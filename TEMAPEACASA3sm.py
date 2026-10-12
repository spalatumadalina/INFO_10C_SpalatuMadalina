distanta=float(input("introdu distanta(km):"))
consum=float(input("introdu consumul(L/100 km):"))
combustibil=distanta*consum/100
print(f"combustibil necesar:{combustibil:.2f} L")
