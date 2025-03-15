# classifying animals into taxonomic ranks
# 4 March 2022

print("Welcome to the Biology Expert")
print("-----------------------------")
print("Answer the following questions by selecting from among the options.")

skele = input('The skeleton is (internal/external)? \n')
if skele == "external":
    print("Type of animal: Arthropod")
else:
    eggs = input("The fertilisation of eggs occurs (within the body/outside the body)? \n")
    if eggs == "within the body":
        young = input("Young are produced by (waterproof eggs/live birth)? \n")
        if young == "waterproof eggs":
            skin = input("The skin is covered by (scales/feathers)? \n")
            if skin == "scales":
                print("Type of animal: Reptile")
            else:
                print("Type of animal: Bird")
        else:
            print("Type of animal: Mammal")
    else:
        lives = input("It lives (in water/near water)? \n")
        if lives == "in water":
            print("Type of animal: Fish")
        else:
            print("Type of animal: Amphibian")