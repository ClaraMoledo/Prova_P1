# Category Domain Entity Example

Este projeto demonstra uma implementação de entidade de domínio `Category` com **serialização** e **eventos de domínio** seguindo princípios de DDD (Domain-Driven Design) em Python.

## Funcionalidades

- **Serialização:**  
  Métodos para exportar (`to_dict`) e reconstruir (`from_dict`) objetos `Category`.
- **Eventos de Domínio:**  
  Eventos automáticos ao criar, atualizar, ativar e desativar categorias, armazenados em `self.events`.
- **Código limpo e orientado ao domínio.**

## Estrutura

```
PROVA P1
├── category.py
├── events/
│   └── category_events.py
└── main.py
```

## Como usar

1. **Instale as dependências:**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute o exemplo:**  
   ```bash
   python main.py
   ```

3. **Veja os resultados:**  
   - Criação, serialização, reconstrução e histórico de eventos da categoria impressos no console.

## Requisitos

- Python 3.7+

> Se quiser adaptar para frameworks como Django ou FastAPI, basta ajustar a modelagem mantendo os princípios de DDD.

## Exemplos de eventos implementados

- `CategoryCreated`
- `CategoryUpdated`
- `CategoryActivated`
- `CategoryDeactivated`

## Autor

Clara Moledo
