# Sistema de Categorias - Flask (Tema Lilás/Light e Dark)

Este projeto é um sistema web de categorias, feito em **Python Flask** com interface moderna (tema escuro/dark e claro/lilás), tabela estilizada, CRUD completo e eventos.

## Funcionalidades

- Cadastro, edição, ativação/desativação e remoção de categorias
- Visualização detalhada de cada categoria e seus eventos
- Tema escuro/dark e tema claro/lilás, com botão de alternância na navbar
- Estilo profissional, responsivo, com fonte Inter e tabelas modernas
- Fácil de customizar

---

## Como rodar localmente

### 1. Pré-requisitos

- **Python 3.8+** instalado  
- **pip** (gerenciador de pacotes do Python)

### 2. Clone o repositório

```bash
git clone https://github.com/ClaraMoledo/Prova_P1.git
cd Prova_P1
```

### 3. Crie um ambiente virtual (opcional, mas recomendado)

No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

No Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Estrutura dos arquivos

```
├── app.py
├── category.py
├── events/
│   └── category_events.py
├── requirements.txt
└── templates/
    ├── base.html
    ├── index.html
    ├── add_category.html
    ├── edit_category.html
    └── category_details.html
```

### 6. Rode a aplicação

```bash
python app.py
```

### 7. Acesse no navegador

Abra [http://localhost:5000](http://localhost:5000) em seu navegador.

---

## Personalização de Tema

- Use o botão de lua/sol na barra superior para alternar entre tema dark (preto/roxo) e tema claro (lilás).
- A escolha do tema é salva no navegador.

---
