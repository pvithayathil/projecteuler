#euler problem 97

non_m_prime = 28433
for i in range(0,7830457):
    non_m_prime = (non_m_prime * 2) % 100000000000

non_m_prime +=1
print non_m_prime
