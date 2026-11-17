# TeleCampo — Plataforma de Apoio ao Técnico de Campo

## Sobre o projeto

O TeleCampo é um projeto acadêmico do curso de Análise e Desenvolvimento de Sistemas, voltado ao apoio na validação de reparos em redes FTTH.

A proposta busca organizar informações de atendimentos, identificar PONs e registrar resultados de conferências técnicas, reduzindo a dependência operacional de supervisores e analistas.

## Funcionalidades planejadas

- Cadastro de atendimentos FTTH.
- Consulta de atendimentos e identificação das PONs.
- Registro de validações: NORMALIZADA ou PERSISTE_FALHA.
- Consulta ao histórico de validações.
- Filtro de atendimentos por situação (funcionalidade desejável).

## Tecnologias previstas

- Python 3.12
- Flask
- Jinja2
- Bootstrap 5
- SQLite 3

## Arquitetura

O projeto adotará uma arquitetura monolítica em camadas:

1. Apresentação: interface web responsiva.
2. Lógica de negócio: processamento e validação de informações.
3. Persistência: armazenamento dos registros no SQLite.

## Protótipo

O repositório contém um protótipo visual demonstrativo com três telas:

1. Entrada e consulta de atendimento.
2. Registro de validação FTTH.
3. Histórico de validações.

Para visualizar o protótipo, baixe o arquivo `prototipo.html` e abra-o em um navegador.

## Segurança e acessibilidade

Estão previstos controles de autenticação, autorização, proteção de dados e prevenção de vulnerabilidades conforme diretrizes OWASP.

A interface será desenvolvida considerando as diretrizes WCAG 2.2, nível AA.

## Situação atual

O projeto está na fase de prototipação e preparação da implementação.

O protótipo utiliza dados fictícios e não possui integração com ferramentas internas de diagnóstico, como GAVA e NAF.

As funcionalidades de backend, autenticação e persistência serão implementadas nas próximas etapas.

## Objetivo de Desenvolvimento Sustentável

ODS 9 — Indústria, Inovação e Infraestrutura.

O projeto busca contribuir indiretamente para a melhoria dos processos de manutenção da infraestrutura de conectividade.

## Finalidade

Projeto desenvolvido para fins acadêmicos e de aprendizagem em engenharia de software.
