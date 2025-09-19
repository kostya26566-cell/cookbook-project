def read_cook_book(filename):

    cook_book = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден!")
        print("Убедитесь, что файл recipes.txt находится в той же папке, что и программа")
        return cook_book
    
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        dish_name = line
        i += 1
        
        if i >= len(lines):
            break
            
        try:
            ingredients_count = int(lines[i].strip())
            i += 1
        except ValueError:
            break
        
        ingredients = []
        for _ in range(ingredients_count):
            if i >= len(lines):
                break
                
            ingredient_line = lines[i].strip()
            if not ingredient_line:
                i += 1
                continue
                
            parts = ingredient_line.split('|')
            if len(parts) < 3:
                i += 1
                continue
                
            ingredient_name = parts[0].strip()
            try:
                quantity = int(parts[1].strip())
            except ValueError:
                quantity = 0
                
            measure = parts[2].strip()
            
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
            i += 1
        
        cook_book[dish_name] = ingredients
    
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):

    shop_list = {}
    
    for dish in dishes:
        if dish not in cook_book:
            print(f"Внимание: Блюдо '{dish}' не найдено!")
            continue
            
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            
            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {'measure': measure, 'quantity': quantity}
    
    return shop_list


def main():
    cook_book = read_cook_book('recipes.txt')
    
    if not cook_book:
        return
    
    print("Кулинарная книга успешно загружена!")
    print(f"Найдено рецептов: {len(cook_book)}")
    
    print("\nДоступные блюда:")
    for dish in cook_book.keys():
        print(f"- {dish}")
    
    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    
    print(f"Рассчитываем ингредиенты для: {', '.join(dishes)}")
    print(f"Количество персон: {person_count}")
    
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    
    print("\nСписок покупок:")
    for ingredient, info in shop_list.items():
        print(f"{ingredient}: {info['quantity']} {info['measure']}")
    
    dishes2 = ['Фахитос']
    person_count2 = 4
    
    print(f"Рассчитываем ингредиенты для: {', '.join(dishes2)}")
    print(f"Количество персон: {person_count2}")
    
    shop_list2 = get_shop_list_by_dishes(dishes2, person_count2, cook_book)
    
    print("\nСписок покупок:")
    for ingredient, info in shop_list2.items():
        print(f"{ingredient}: {info['quantity']} {info['measure']}")


if __name__ == "__main__":
    main()