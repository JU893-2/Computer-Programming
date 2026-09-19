flight_log = [1000, 2500, 4200, 6000, 7800, 9500, 11000, 12500]
print("Initial log:", flight_log)

flight_log.append(13800)
print("After append 1:", flight_log)

flight_log.append(15000)
print("After append 2:", flight_log)

removed_first = flight_log.pop(0)
print("After removing first corrupt entry:", flight_log)

removed_second = flight_log.pop(0)
print("After removing second corrupt entry:", flight_log)

flight_log.insert(1, 5100)
print("After inserting missing mid flight data:", flight_log)

print(f"Reading at index 1: {flight_log[1]}")
print(f"Reading at index 3: {flight_log[3]}")

