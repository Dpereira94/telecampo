
# Requisitos Funcionais — TeleCampo

## Objetivo
Organizar atendimentos FTTH e registrar validações dos reparos realizados pelos técnicos de campo.

## Requisitos obrigatórios

### RF01 — Cadastrar atendimento
Permitir o cadastro de atendimentos com código único, técnico responsável e PON associada.

### RF02 — Consultar atendimento
Permitir a consulta dos dados do atendimento e da PON pelo código informado.

### RF03 — Registrar validação
Permitir registrar o resultado NORMALIZADA ou PERSISTE_FALHA, associado ao atendimento.

### RF04 — Consultar histórico
Apresentar as validações anteriores, organizadas da mais recente para a mais antiga.

## Requisito desejável

### RF05 — Filtrar atendimentos
Permitir filtrar atendimentos pelos status ABERTO, EM_VALIDACAO e CONCLUIDO.

## Tecnologias previstas
- Python 3.12
- Flask
- Jinja2
- Bootstrap 5
- SQLite 3

## Situação
Requisitos documentados e aguardando implementação.
