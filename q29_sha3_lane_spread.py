# Q29 - SHA-3 lane diffusion, ignoring the permutation
#
# SHA-3 uses a 5 x 5 array of lanes. With a 1024-bit message block:
#   rate = 1024 bits
#   capacity = 1600 - 1024 = 576 bits
#
# Each lane is 64 bits, so:
#   rate lanes = 1024 / 64 = 16 lanes
#   capacity lanes = 9 lanes
#
# The question says each lane in the first message block P0 has at least
# one nonzero bit. If the permutation is ignored and we only keep track of
# the original zero lanes, then the 16 rate lanes become nonzero immediately
# after absorbing P0, while the 9 capacity lanes remain zero.
#
# Therefore, under the stated "ignore permutation" assumption, it will NEVER
# happen that all 25 lanes have at least one nonzero bit.

LANE_BITS = 64
STATE_LANES = 25
RATE_BITS = 1024
CAPACITY_BITS = 1600 - RATE_BITS

rate_lanes = RATE_BITS // LANE_BITS
capacity_lanes = CAPACITY_BITS // LANE_BITS

print("Q29: SHA-3 lane analysis")
print("State size       :", STATE_LANES * LANE_BITS, "bits")
print("Block/rate size  :", RATE_BITS, "bits")
print("Capacity         :", CAPACITY_BITS, "bits")
print("Rate lanes       :", rate_lanes)
print("Capacity lanes   :", capacity_lanes)

# Represent nonzero/zero status.
state = [True] * rate_lanes + [False] * capacity_lanes

print("\nLane status after absorbing P0:")
for i, nonzero in enumerate(state):
    print(f"Lane {i:2d}: {'nonzero' if nonzero else 'zero'}")

if all(state):
    print("\nAll lanes are nonzero.")
else:
    print("\nResult: All lanes will NEVER become nonzero under the stated")
    print("assumption because the permutation is explicitly ignored.")
    print("The 9 original capacity lanes remain zero forever in this model.")
