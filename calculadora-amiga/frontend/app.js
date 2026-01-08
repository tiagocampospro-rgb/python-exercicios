const API_BASE = "http://127.0.0.1:8000";

let catalogo = [];
let selecionado = null;

const elSearch = document.getElementById("search");
const elCards = document.getElementById("cards");
const elStatus = document.getElementById("status");

const overlay = document.getElementById("overlay");
const elPanelTitle = document.getElementById("panelTitle");
const elPanelDesc = document.getElementById("panelDesc");
const elPanelTag = document.getElementById("panelTag");
const elPanelEndpoint = document.getElementById("panelEndpoint");
const elForm = document.getElementById("calcForm");

const resultBox = document.getElementById("resultBox");
const elErr = document.getElementById("err");
const elBig = document.getElementById("bigResult");
const elJson = document.getElementById("jsonResult");

document.getElementById("refresh").addEventListener("click", carregarCatalogo);
document.getElementById("btnFechar").addEventListener("click", fecharModal);
document.getElementById("btnFecharX").addEventListener("click", fecharModal);
document.getElementById("btnCalcular").addEventListener("click", calcular);

elSearch.addEventListener("input", () => renderCards(filtrar(elSearch.value)));

function normalizar(txt) {
  return (txt || "")
    .toLowerCase()
    .normalize("NFD")
    .replace(/\p{Diacritic}/gu, "");
}

function filtrar(q) {
  const nq = normalizar(q);
  if (!nq) return catalogo;

  return catalogo.filter((item) => {
    const alvo = normalizar(`${item.titulo} ${item.descricao} ${item.id}`);
    return alvo.includes(nq);
  });
}

function fmtNumero(n) {
  if (typeof n !== "number") return String(n);
  // Formata com separador brasileiro: 1.234,56
  return new Intl.NumberFormat("pt-BR", { maximumFractionDigits: 2 }).format(n);
}

function fmtMoedaBRL(n) {
  if (typeof n !== "number") return String(n);
  return new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" }).format(n);
}

function limparResultado() {
  resultBox.style.display = "none";
  elErr.style.display = "none";
  elBig.style.display = "none";
  elJson.style.display = "none";
  elErr.textContent = "";
  elBig.textContent = "";
  elJson.textContent = "";
}

function mostrarErro(msg) {
  resultBox.style.display = "block";
  elErr.style.display = "block";
  elErr.textContent = msg;
  elBig.style.display = "none";
  elJson.style.display = "none";
}

function mostrarResultado(data) {
  resultBox.style.display = "block";
  elErr.style.display = "none";

  // Exibir “bonito” para algumas operações
  let textoBonito = null;

  if (data?.operacao === "aumento" && typeof data.novo_salario === "number") {
    textoBonito = fmtMoedaBRL(data.novo_salario);
  } else if (data?.operacao === "tinta" && typeof data.litros_necessarios === "number") {
    textoBonito = `${fmtNumero(data.litros_necessarios)} L`;
  } else if (typeof data?.resultado === "number") {
    textoBonito = fmtNumero(data.resultado);
  }

  if (textoBonito !== null) {
    elBig.style.display = "block";
    elBig.textContent = textoBonito;
  } else {
    elBig.style.display = "none";
  }

  // Sempre mostrar JSON para transparência (portfólio)
  elJson.style.display = "block";
  elJson.textContent = JSON.stringify(data, null, 2);
}

function renderCards(lista) {
  elCards.innerHTML = "";

  if (!lista.length) {
    elCards.innerHTML = `
      <div class="card">
        <div class="pill">🔎 Nenhum resultado</div>
        <h3>Nada encontrado</h3>
        <p>Tente pesquisar por: <b>soma</b>, <b>tinta</b>, <b>salário</b>, <b>divisão</b>…</p>
        <p class="small">Dica: use Ctrl + K para focar no campo de busca.</p>
      </div>`;
    return;
  }

  for (const item of lista) {
    const div = document.createElement("div");
    div.className = "card";

    div.innerHTML = `
      <div class="pill">🧮 ${item.id}</div>
      <h3>${item.titulo}</h3>
      <p>${item.descricao}</p>
      <div class="row">
        <span class="small">${item.endpoint}</span>
        <button class="btn btn-primary">Usar</button>
      </div>
    `;

    div.querySelector("button").addEventListener("click", () => abrirModal(item));
    elCards.appendChild(div);
  }
}

async function carregarCatalogo() {
  elStatus.textContent = "Carregando catálogo...";
  try {
    const res = await fetch(`${API_BASE}/catalogo`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();

    catalogo = data.itens || [];
    elStatus.textContent = `Catálogo carregado: ${catalogo.length} calculadoras.`;
    renderCards(filtrar(elSearch.value));
  } catch (err) {
    elStatus.textContent = "";
    elCards.innerHTML = `
      <div class="card">
        <div class="pill">⚠️ Erro</div>
        <h3>Não consegui falar com o backend</h3>
        <p>Confirme se o FastAPI está rodando em <b>${API_BASE}</b>.</p>
        <p class="small">Dica: no terminal do backend deve aparecer “Uvicorn running on http://127.0.0.1:8000”.</p>
      </div>`;
  }
}

function abrirModal(item) {
  selecionado = item;

  elPanelTitle.textContent = item.titulo;
  elPanelDesc.textContent = item.descricao;
  elPanelTag.textContent = item.id;
  elPanelEndpoint.textContent = item.endpoint;

  elForm.innerHTML = "";
  limparResultado();

  for (const campo of item.campos) {
    const wrapper = document.createElement("div");
    wrapper.innerHTML = `
      <label for="${campo.nome}">${campo.label}</label>
      <input
        id="${campo.nome}"
        name="${campo.nome}"
        type="${campo.tipo || "number"}"
        step="${campo.step || "any"}"
        placeholder="Ex: ${campo.exemplo ?? ""}"
        required
      />
    `;
    elForm.appendChild(wrapper);
  }

  overlay.classList.add("show");
  setTimeout(() => {
    const first = item.campos?.[0]?.nome;
    if (first) document.getElementById(first)?.focus();
  }, 20);
}

function fecharModal() {
  selecionado = null;
  overlay.classList.remove("show");
}

async function calcular() {
  if (!selecionado) return;
  limparResultado();

  const params = new URLSearchParams();
  for (const campo of selecionado.campos) {
    const el = document.getElementById(campo.nome);
    const val = el.value.trim();

    if (!val) {
      mostrarErro("Preencha todos os campos.");
      return;
    }
    params.append(campo.nome, val);
  }

  const url = `${API_BASE}${selecionado.endpoint}?${params.toString()}`;

  try {
    const res = await fetch(url);
    const data = await res.json();

    if (!res.ok) {
      mostrarErro(data?.detail ? String(data.detail) : "Erro ao calcular.");
      return;
    }

    mostrarResultado(data);
  } catch {
    mostrarErro("Falha ao conectar no backend. Ele está rodando?");
  }
}

/* Atalhos e UX */
window.addEventListener("keydown", (e) => {
  if (e.key === "Escape") fecharModal();

  // Ctrl + K -> focar busca
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
    e.preventDefault();
    elSearch.focus();
  }
});

// Clique fora fecha modal
overlay.addEventListener("click", (e) => {
  if (e.target === overlay) fecharModal();
});

// Inicial
carregarCatalogo();

