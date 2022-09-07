# Write code for algorithm 5 below

def reverse(s):
    c = s.replace(" ", "").replace(".", "").replace(
        ",", "").replace("?", "").lower()
    return c == c[::-1]


print(reverse("tee"))
print(reverse("teet"))
print(reverse("do geese see god"))
print(reverse("Was it a car or a cat I saw?"))
print(reverse("Mr. Owl ate my metal worm."))
print(reverse("Live on time, emit no evil."))
