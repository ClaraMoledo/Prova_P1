from category import Category

def print_events(events):
    for e in events:
        print(e)

# Criação de categoria
cat = Category(name="Livros", description="Categoria de livros")
print("Categoria criada:", cat.to_dict())
print("Eventos após criação:")
print_events(cat.events)

# Serialização e reconstrução
cat_dict = cat.to_dict()
cat2 = Category.from_dict(cat_dict)
print("\nCategoria reconstruída:", cat2.to_dict())

# Atualização
cat.update(name="Livros e revistas", description="Livros e revistas de vários gêneros")
print("\nEventos após atualização:")
print_events(cat.events)

# Desativação
cat.deactivate()
print("\nEventos após desativação:")
print_events(cat.events)

# Ativação
cat.activate()
print("\nEventos após ativação:")
print_events(cat.events)
