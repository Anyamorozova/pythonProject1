rating = [1, 2, 4, 5]
print(f'Текущий рейтинг: {rating}')
number_input = int(input('Введите новый элемент рейтинга (число): '))
new_rating = []

for i, elem in enumerate(rating):
    if i != len(rating) - 1:
        if number_input > elem:
            new_rating.append(elem)
        elif number_input < elem:
            new_rating.append(number_input)
            new_rating = new_rating + rating[i:]
            break
        else:
            new_rating.append(elem)
            new_rating.append(number_input)
            new_rating = new_rating + rating[i+1:]
            break
    else:
        new_rating.append(elem)
        new_rating.append(number_input)
print(f'Новый рейтинг: {new_rating}')
