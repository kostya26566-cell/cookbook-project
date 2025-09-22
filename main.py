def read_cook_book(filename):
    cook_book = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            current_dish = None
            ingredients_count = 0
            ingredients_read = 0
            
            for line in file:
                line = line.strip()
                
                if not line:
                    current_dish = None
                    ingredients_count = 0
                    ingredients_read = 0
                    continue
                
                if current_dish is None:
                    current_dish = line
                    cook_book[current_dish] = []
                    continue
                
                if ingredients_count == 0: 
                    try:
                        ingredients_count = int(line)
                    except ValueError:
                        print(f"Ошибка: ожидалось число ингредиентов для '{current_dish}'")
                        current_dish = None
                    continue
                
                if ingredients_read < ingredients_count:
                    parts = line.split('|')
                    if len(parts) < 3:
                        print(f"Ошибка в формате ингредиента для '{current_dish}': {line}")
                        continue
                    
                    ingredient_name = parts[0].strip()
                    try:
                        quantity = int(parts[1].strip())
                    except ValueError:
                        quantity = 0
                        print(f"Ошибка: количество должно быть числом для '{ingredient_name}'")
                    
                    measure = parts[2].strip()
                    
                    cook_book[current_dish].append({
                        'ingredient_name': ingredient_name,
                        'quantity': quantity,
                        'measure': measure
                    })
                    ingredients_read += 1
                    
                    if ingredients_read == ingredients_count:
                        current_dish = None
                        ingredients_count = 0
                        ingredients_read = 0
    
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден!")
        print("Убедитесь, что файл recipes.txt находится в той же папке, что и программа")
    
    return cook_book