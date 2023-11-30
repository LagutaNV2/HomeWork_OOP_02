import os


def get_shop_list(dishes: list, person: int):
    result = {}
    ingredients = {}
    for dish in dishes:
        for n_dish, recept_list in cook_book.items():
            if n_dish == dish:
               for ingr in recept_list:

                   if ingr['ingredient_name'] not in result:
                       ingredients[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': ingr['quantity']*person}
                       result.update(ingredients)
                   else:
                       x = result.get(ingr['ingredient_name'])
                       y = x.get('quantity') + ingr['quantity'] * person
                       result[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': y}
    return result


file_path = os.path.join(os.getcwd(), 'recipes.txt')
with open(file_path, 'r', encoding='utf-8') as f:
    file_as_list = f.readlines()

cook_book = {}
ingredient_number, quantity_ingredients = 0, 0

for s in file_as_list:
    string_from_file = s.strip()

    if string_from_file.isdigit():
        quantity_ingredients = int(string_from_file)
        ingredient_number = 0
        recept = [{'ingredient_name': '',
                   'quantity': '',
                   'measure': ''} for j in range(quantity_ingredients)]
    else:
        if '|' in string_from_file:
            # print(string_from_file.split('|'), 'ingredient_number', ingredient_number, 'name_dish', name_dish)
            recept_as_list = string_from_file.split('|')
            # ('заполняем словарь рецепта')
            recept[ingredient_number]['ingredient_name'] = recept_as_list[0].strip()
            recept[ingredient_number]['quantity'] = int(recept_as_list[1].strip())
            recept[ingredient_number]['measure'] = recept_as_list[2].strip()
            ingredient_number += 1

            if ingredient_number == quantity_ingredients:
                cook_book[name_dish] = recept
                # ('ingredient_number = quantity_ingredients --> append dict cook_book')

        elif string_from_file != '':
            name_dish = string_from_file
            cook_book.setdefault(name_dish, [])

print('cook_book =')
print(cook_book)

# запуск функции по задаче 2
dishes = ['Омлет', 'Фахитос', 'Утка по-пекински', 'Запеченный картофель']
person = int(input('введите целое число: '))
print('Ваш список продуктов: ', get_shop_list(dishes, person))

