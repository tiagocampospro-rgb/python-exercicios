from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import calc

app = FastAPI(
    title="Calculadora Amiga",
    description="API simples para cálculos do dia a dia (portfólio).",
    version="0.3.0",
)

# CORS: permite seu frontend (Live Server, file://, etc.) chamar a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # para desenvolvimento
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TAG = "Calculos"

# -----------------------------
# Catálogo (para o FRONTEND)
# -----------------------------
CATALOGO = [
    {
        "id": "soma",
        "titulo": "Soma",
        "descricao": "Somar dois números (a + b).",
        "endpoint": "/soma",
        "campos": [
            {"nome": "a", "label": "Primeiro número (a)", "tipo": "number", "step": "any", "exemplo": 2},
            {"nome": "b", "label": "Segundo número (b)", "tipo": "number", "step": "any", "exemplo": 3},
        ],
    },
    {
        "id": "subtracao",
        "titulo": "Subtração",
        "descricao": "Subtrair dois números (a - b).",
        "endpoint": "/subtracao",
        "campos": [
            {"nome": "a", "label": "Primeiro número (a)", "tipo": "number", "step": "any", "exemplo": 10},
            {"nome": "b", "label": "Segundo número (b)", "tipo": "number", "step": "any", "exemplo": 4},
        ],
    },
    {
        "id": "multiplicacao",
        "titulo": "Multiplicação",
        "descricao": "Multiplicar dois números (a × b).",
        "endpoint": "/multiplicacao",
        "campos": [
            {"nome": "a", "label": "Primeiro número (a)", "tipo": "number", "step": "any", "exemplo": 6},
            {"nome": "b", "label": "Segundo número (b)", "tipo": "number", "step": "any", "exemplo": 7},
        ],
    },
    {
        "id": "divisao",
        "titulo": "Divisão",
        "descricao": "Dividir dois números (a ÷ b). b não pode ser 0.",
        "endpoint": "/divisao",
        "campos": [
            {"nome": "a", "label": "Numerador (a)", "tipo": "number", "step": "any", "exemplo": 10},
            {"nome": "b", "label": "Denominador (b)", "tipo": "number", "step": "any", "exemplo": 2},
        ],
    },
    {
        "id": "aumento",
        "titulo": "Aumento salarial (%)",
        "descricao": "Calcula o novo salário após um aumento percentual (ex: 15%).",
        "endpoint": "/aumento",
        "campos": [
            {"nome": "salario", "label": "Salário atual (R$)", "tipo": "number", "step": "0.01", "exemplo": 2500},
            {"nome": "percentual", "label": "Percentual de aumento (ex: 15)", "tipo": "number", "step": "any", "exemplo": 15},
        ],
    },
    {
        "id": "tinta",
        "titulo": "Tinta para parede (litros)",
        "descricao": "Calcula litros de tinta pela largura, altura e rendimento (m²/L).",
        "endpoint": "/tinta",
        "campos": [
            {"nome": "largura", "label": "Largura (m)", "tipo": "number", "step": "any", "exemplo": 3},
            {"nome": "altura", "label": "Altura (m)", "tipo": "number", "step": "any", "exemplo": 2.5},
            {"nome": "rendimento_m2_por_litro", "label": "Rendimento (m² por litro)", "tipo": "number", "step": "any", "exemplo": 2.0},
        ],
    },
]


@app.get("/", tags=["Status"], summary="Status da API", operation_id="status")
def home():
    return {"status": "ok", "msg": "Calculadora Amiga rodando!"}


@app.get("/catalogo", tags=[TAG], summary="Lista de calculadoras", operation_id="catalogo")
def catalogo():
    return {"total": len(CATALOGO), "itens": CATALOGO}


# -----------------------------
# Endpoints de cálculo (API)
# -----------------------------

@app.get(
    "/soma",
    tags=[TAG],
    summary="Somar dois números",
    description="Retorna a soma de **a + b**.",
    operation_id="soma",
)
def rota_soma(
    a: float = Query(..., description="Primeiro número", examples=[2]),
    b: float = Query(..., description="Segundo número", examples=[3]),
):
    return {"operacao": "soma", "a": a, "b": b, "resultado": calc.soma(a, b)}


@app.get(
    "/subtracao",
    tags=[TAG],
    summary="Subtrair dois números",
    description="Retorna a subtração de **a - b**.",
    operation_id="subtracao",
)
def rota_subtracao(
    a: float = Query(..., description="Primeiro número", examples=[10]),
    b: float = Query(..., description="Segundo número", examples=[4]),
):
    return {"operacao": "subtracao", "a": a, "b": b, "resultado": calc.subtracao(a, b)}


@app.get(
    "/multiplicacao",
    tags=[TAG],
    summary="Multiplicar dois números",
    description="Retorna a multiplicação de **a × b**.",
    operation_id="multiplicacao",
)
def rota_multiplicacao(
    a: float = Query(..., description="Primeiro número", examples=[6]),
    b: float = Query(..., description="Segundo número", examples=[7]),
):
    return {"operacao": "multiplicacao", "a": a, "b": b, "resultado": calc.multiplicacao(a, b)}


@app.get(
    "/divisao",
    tags=[TAG],
    summary="Dividir dois números",
    description="Retorna a divisão de **a ÷ b**. Se **b = 0**, retorna erro.",
    operation_id="divisao",
)
def rota_divisao(
    a: float = Query(..., description="Numerador", examples=[10]),
    b: float = Query(..., description="Denominador (não pode ser 0)", examples=[2]),
):
    try:
        resultado = calc.divisao(a, b)
        return {"operacao": "divisao", "a": a, "b": b, "resultado": resultado}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get(
    "/aumento",
    tags=[TAG],
    summary="Calcular aumento salarial (%)",
    description="Calcula o novo salário após aplicar um aumento percentual.",
    operation_id="aumento",
)
def rota_aumento(
    salario: float = Query(..., gt=0, description="Salário atual (R$)", examples=[2500]),
    percentual: float = Query(..., gt=0, description="Percentual de aumento (ex: 15)", examples=[15]),
):
    novo = calc.aumento_percentual(salario, percentual)
    return {
        "operacao": "aumento",
        "salario": salario,
        "percentual": percentual,
        "novo_salario": round(novo, 2),
    }


@app.get(
    "/tinta",
    tags=[TAG],
    summary="Calcular litros de tinta para parede",
    description="Calcula os litros de tinta necessários com base na largura, altura e rendimento (m²/L).",
    operation_id="tinta",
)
def rota_tinta(
    largura: float = Query(..., gt=0, description="Largura da parede (m)", examples=[3]),
    altura: float = Query(..., gt=0, description="Altura da parede (m)", examples=[2.5]),
    rendimento_m2_por_litro: float = Query(2.0, gt=0, description="Rendimento (m²/L). Padrão: 2.0", examples=[2.0]),
):
    try:
        litros = calc.litros_tinta(largura, altura, rendimento_m2_por_litro)
        area = round(largura * altura, 2)
        return {
            "operacao": "tinta",
            "largura": largura,
            "altura": altura,
            "area_m2": area,
            "rendimento_m2_por_litro": rendimento_m2_por_litro,
            "litros_necessarios": litros,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
