# !/usr/bin/python3




"""

[4, 3, 2, 5, 4, 3, 2, 6]
[[6], [5, 4],[5, 4,3], [5, 4, 3, 2]]
bin soke?

"""

# coding=utf-8
import random
import itertools

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nedre, og muligheten for å generere
# tilfeldige instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å justere på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = False
# Antall tilfeldige tester som genereres.
random_tests = 10
# Laveste mulige antall tall i generert instans.
numbers_lower = 4
# Høyest mulig antall tall i generert instans.
# NB: Om denne verdien settes høyt (>25) vil det ta veldig lang tid å
# generere testene.
numbers_upper = 10
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0

"""
Plan:
mot hogre blir mindre og mindre for hver gang
o(n^2)?
[8,7,3,4,6,5]
[8, [8,7],[8,7,6], [8, 7, 6, 5], [8]]
[8, [8,7],[8,7,6], [8, 7, 6, 5], [8]]
[[8], [8,7],[8,7,6], [8, 7, 6, 5], [8]]
[9, 6, 7, 3, 2, 1, 10, 8]
[[10], [10,8],[9, 7, 3],[9, 7, 2],[9,7,3,2,1], [INF]]



viss storre enn den forrige men mindre enn den nåverende
#lagrer beste for dei ulike vilkårlige lengdene
"""



def longest_decreasing_subsequence(s):
    l = [[1e9]*len(s)]*len(s)
    l[0] = s[0]
    end = 1
    print(l[end-1])
    # for i in range(len(s)):
    #     cur = s[i]
    #     l[0] = max(l[0], cur)
    #     if cur<l[end][-1]:
    #         end+=1
    #         l[end] = l[end-1]
    #         l[end].append(cur)
    #         continue
    #     for j in range(end):
    #         if(cur>l[j][-1] and cur<l[j][-2]):
    #             l[j][-1] = cur
    # print(l)



longest_decreasing_subsequence([6, 3, 4])
            





# # Hardkodete tester
# tests = [
#     [1],
#     [1, 2],
#     [1, 2, 3],
#     [2, 1],
#     [3, 2, 1],
#     [1, 3, 2],
#     [3, 1, 2],
#     [1, 1],
#     [1, 2, 1],
#     [8, 7, 3, 6, 2, 6],
#     [10, 4, 2, 1, 7, 5, 3, 2, 1],
#     [3, 7, 2, 10, 3, 3, 3, 9],
# ]


# # Treg bruteforce løsning som tester alle delfølger
# def find_optimal_length(s):
#     for k in range(len(s), 1, -1):
#         for perm in itertools.combinations(range(len(s)), k):
#             z = [s[x] for x in perm]
#             if z == sorted(set(z), reverse=True):
#                 return k
#     return 1


# def verify(sequence, subsequence, optimal_length):
#     if subsequence is None:
#         return False, "Svaret er ikke en følge."

#     # Test if the subsequence is actually a subsequence
#     index = 0
#     for element in sequence:
#         if element == subsequence[index]:
#             index += 1
#             if index == len(subsequence):
#                 break

#     if index < len(subsequence):
#         return False, "Svaret er ikke en delfølge av følgen."

#     # Test if the subsequence is decreasing
#     for index in range(1, len(subsequence)):
#         if subsequence[index] >= subsequence[index - 1]:
#             return False, "Den gitte delfølgen er ikke synkende."

#     # Test if the solution is optimal
#     if len(subsequence) != optimal_length:
#         return (
#             False,
#             "Delfølgen har ikke riktig lengde. Riktig lengde er"
#             + "{:}, mens delfølgen har lengde ".format(optimal_length)
#             + "{:}".format(len(subsequence)),
#         )

#     return True, ""


# def gen_examples(k, lower, upper):
#     for _ in range(k):
#         yield [
#             random.randint(0, 9999) for _ in range(random.randint(lower, upper))
#         ]


# if generate_random_tests:
#     if seed:
#         random.seed(seed)
#     tests += list(gen_examples(
#         random_tests,
#         numbers_lower,
#         numbers_upper,
#     ))


# failed = False
# for test in tests:
#     student = longest_decreasing_subsequence(test[:])
#     optimal_length = find_optimal_length(test)
#     correct, error_message = verify(test, student, optimal_length)

#     if not correct:
#         if failed:
#             print("-"*50)
#         failed = True
#         print(f"""
# Koden feilet for følgende instans:
# s: {test}

# Ditt svar: {student}
# Feilmelding: {error_message}
# """)

# if not failed:
#     print("Koden ga riktig svar for alle eksempeltestene")
