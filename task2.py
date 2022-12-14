# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

for x0 in range(2):
    for x1 in range(2):
        for x2 in range(2):
            if not (x0 or x1 or x2) == (not x0 and not x1 and not x2):
                print('Утверждение верно при следующих значениях:',{x0}, {x1}, {x2})
