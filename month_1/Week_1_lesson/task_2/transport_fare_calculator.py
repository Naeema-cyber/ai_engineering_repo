distance =float(input("How long is the journey? " ))
fare_per_km = float(input("How much is the fare per km?: "))
total = distance * fare_per_km
print(f"₦{total: .2f}")