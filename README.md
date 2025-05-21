# Enterprise-Challenge---Sprint-1
Enterprise Challenge - Sprint 1 - Reply
# FIAP - Inteligência artificial e data science

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto
Cap 3 - Colheita de Dados e Insights - Cap 1 - Construindo uma máquina agrícola - Enterprise Challenge - Sprint 1

## Nome do grupo
39

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Guilherme Campos Hermanowski </a>
- <a href="https://www.linkedin.com/company/inova-fusca">Gabriel Viel </a>
- <a href="https://www.linkedin.com/company/inova-fusca"> Matheus Alboredo Soares</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Jonathan Willian Luft </a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>


## 📜 Justificativa do problema e descrição da solução proposta

Sistemas de irrigação inteligentes geram uma grande quantidade de dados por meio de sensores que monitoram variáveis como umidade do solo, pH, níveis de fósforo e potássio, além do estado da bomba de irrigação. No entanto, esses dados, quando apresentados apenas em formato bruto, são de difícil interpretação — especialmente para usuários sem conhecimento técnico ou experiência com análise de dados.

Na prática, isso dificulta a resposta a perguntas fundamentais, como:

O solo está suficientemente irrigado?

A bomba está sendo acionada nos momentos corretos?

Os níveis de nutrientes estão dentro da faixa ideal?

Há padrões que indicam falhas ou oportunidades de melhoria no sistema?

Sem uma visualização adequada, essas informações passam despercebidas, atrasando decisões importantes, reduzindo a eficiência do sistema e até colocando em risco a saúde das plantas.

Este projeto busca resolver esse problema ao transformar dados técnicos em informações visuais simples e acessíveis, facilitando o monitoramento, a tomada de decisão e a antecipação de ações corretivas — mesmo para quem não é programador ou especialista em agricultura de precisão.
<br>

Em cenários de produção onde há um grande número de maquinário atuando, é rotineiro que diferentes tipos de erros e falhas que acabem por gerar prejuízos e atrapalhar no andamento da produção aconteçam.
Mas e se esses prejuízos e paradas na produção pudessem ser previstos, e assim, antecipadamente evitados, dessa otimizando os processos de melhorando o fluxo de trabalho da empresa? É a partir dessa visão de negócio que surge nosso projeto. 
</p>
Com foco no monitoramento e previsão de falhas em equipamentos de produção, utilizamos de sensores de temperatura, vibração, umidade e volume de produção, somado a uma arquitetura baseada em serviços AWS, para detecção de falhas antes que elas ocorram, permitindo que alertas sejam gerados e o erro evitado antes de sua incidência.

## 🔧 Funcionamento
Este dashboard foi desenvolvido com **Streamlit** para simular e visualizar dados de um sistema de irrigação inteligente, incluindo umidade do solo, estado da bomba, pH e nutrientes (fósforo e potássio).

- **Configuração da página**:
  - Título da aba: `"Monitoramento de Irrigação"`
  - Layout em tela cheia (`layout="wide"`)
  - Título principal da interface: `"Dashboard de Monitoramento do Sistema de Irrigação 🌱"`

  - Este código gera dados simulados para facilitar visualização
- **Geração de dados simulados** (`generate_data()`):
  - Gera um histórico com intervalos de 10 minutos nas últimas 24 horas.
  - Simula:
    - Umidade do solo (20% a 80%)
    - Estado do relé (ligado/desligado)
    - Nível de pH (5 a 8)
    - Fósforo e potássio (0 a 50 mg/kg)
  - Os dados são armazenados em um DataFrame com o índice baseado no timestamp.

- **Uso de sessão Streamlit**:
  - Verifica se o DataFrame já está salvo no `st.session_state` para persistência dos dados entre interações.
  - Se não existir, inicializa com os dados gerados.

- **Painel lateral de filtros**:
  - Permite ao usuário selecionar um intervalo de datas para análise dos dados.

### 📊 Visualizações com Abas

As informações são organizadas em três abas principais:

#### 1. **Dashboard**
- **Gráfico de Umidade do Solo**:
  - Linha do tempo da umidade em porcentagem.
- **Gráfico de Estado do Relé (Bomba de Irrigação)**:
  - Gráfico de degraus mostrando se a bomba esteve ligada (1) ou desligada (0).
- **Gráficos de Qualidade do Solo**:
  - pH: gráfico de linha contínua.
  - Nutrientes: fósforo e potássio plotados juntos.

#### 2. **Tabela de Dados**
- Exibe os dados brutos em formato de tabela interativa (`st.dataframe`).

#### 3. **Simulação de Nova Leitura**
- O usuário pode inserir manualmente novos valores:
  - Umidade (%)
  - pH
  - Fósforo (mg/kg)
  - Potássio (mg/kg)
- A bomba é simulada como **ligada** se a umidade for **menor que 30%**.
- Ao clicar em “Simular”:
  - Um novo registro é adicionado ao DataFrame.
  - Mensagem de sucesso é exibida.

---

### 🔍 Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/) — para construção do dashboard interativo
- [Pandas](https://pandas.pydata.org/) — para manipulação de dados
- [NumPy](https://numpy.org/) — para geração de dados simulados
- [Matplotlib](https://matplotlib.org/) — para gráficos personalizados


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
