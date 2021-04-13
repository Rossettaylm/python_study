def describe_pet(animal_type, pet_name = 'harry'):  #设置形参默认值
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')     #位置实参
describe_pet(animal_type = 'hamster', pet_name = 'harry')   #关键字实参
describe_pet('hamster')
