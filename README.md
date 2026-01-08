# 🧮 Calculadora Amiga

**Calculadora Amiga** é um projeto de portfólio desenvolvido em Python com FastAPI, que oferece cálculos comuns do dia a dia por meio de uma API REST e uma interface web simples e amigável.

O objetivo do projeto é **praticar backend, frontend básico, organização de código, consumo de APIs e boas práticas de desenvolvimento**, servindo também como base para estudos em DevOps.

---

## 🚀 Funcionalidades

Atualmente, a Calculadora Amiga oferece:

- ➕ Soma de dois números  
- ➖ Subtração de dois números  
- ✖️ Multiplicação  
- ➗ Divisão (com tratamento de erro para divisão por zero)  
- 📈 Cálculo de aumento salarial percentual  
- 🎨 Cálculo de litros de tinta necessários para pintar uma parede  

Todas as operações são acessadas via **API REST** e também por uma **interface web** que consome essa API.

---

## 🏗️ Arquitetura do Projeto

O projeto é organizado com separação clara de responsabilidades:
```
calculadora-amiga/
├── backend/
│ ├── app.py # API FastAPI (rotas e documentação)
│ ├── calc.py # Regras de negócio e cálculos
│ ├── requirements.txt # Dependências do backend
│ └── .venv/ # Ambiente virtual (não versionado)
│
├── frontend/
│ ├── index.html # Interface web
│ └── app.js # Lógica do frontend (consumo da API)
```

---

## 🧠 Conceitos praticados

- API REST
- FastAPI e Uvicorn
- Separação entre frontend e backend
- Consumo de API com JavaScript (`fetch`)
- Ambiente virtual Python (`venv`)
- Versionamento com Git e GitHub
- Documentação automática com Swagger
- Organização de projetos Python

---

## 🛠️ Tecnologias utilizadas

### Backend
- Python 3.12+
- FastAPI
- Uvicorn

### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla JS)

---

## ▶️ Como executar o projeto localmente

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/tiagocampospro-rgb/python-exercicios.git
cd python-exercicios/calculadora-amiga/backend
