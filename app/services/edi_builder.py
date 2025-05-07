# edi_builder.py
from app.models import user_input
from app.utils.edi_utils import pad;
from datetime import datetime, timedelta;

def build_registros(user_input, ctes):
    registros = []

    # Registro 000
    registros.append(build_registro_000(user_input))

    # Registro 350
    registros.append(build_registro_350())

    # Registro 351 e 352 (conteúdo fictício fixo por enquanto)
    registros.append(build_registro_351())
    registros.append(build_registro_352(ctes, user_input))

    total_valor = 0
    for cte in ctes:
        registros.append(build_registro_353(cte))
        registros.append(build_registro_354(cte))
        total_valor += float(cte.valor_prestacao or 0)

    registros.append(build_registro_355(total_valor))
    return registros

def build_registro_000(user_input):
    now = datetime.now();
    remetente = pad("Bialog Transportes e Logística S.A.", 35, 'left', ' ')
    destinatario = pad(user_input.nome_cliente, 35, 'left', ' ')
    data = now.strftime("%d%m%Y")
    hora = now.strftime("%H%M%S")
    identificacao_intercambio = f"COB{now.strftime('%d%m%H%M')}0"
    filler = pad("", 75, 'left', ' ');
    return f"000{remetente}{destinatario}{data}{hora}{identificacao_intercambio}{filler}"

def build_registro_350():
    now = datetime.now()
    identificacao_documento = f"COBRA{now.strftime('%d%m%H%M')}0"
    filler = pad("", 153, 'left', ' ')
    return f"350{pad(identificacao_documento, 14)}{filler}"

def build_registro_351():
    cgcBialog = pad("35285109000105", 14, 'left', ' ')
    razaoBialog = pad("Bialog Transportes e Logística S.A.", 40, 'left', ' ')
    filler = pad("", 113, 'left', ' ')
    return f"351{cgcBialog}{razaoBialog}{filler}"

def build_registro_352(ctes, user_input):
    if ctes:
        filial = pad('010101', 10, 'left', ' ')
        tipo_doc_cobranca = pad("0", 1, 'left', ' ')
        serie_doc_cobranca = pad("0", 3, 'left', ' ')
        fatura = pad(user_input.numero_fatura, 10, 'left', ' ')
        data_emissao = datetime.strptime(ctes[0].data_emissao[:10], "%Y-%m-%d").strftime("%d%m%Y")
        data_vencimento = (datetime.strptime(ctes[0].data_emissao[:10], "%Y-%m-%d") + timedelta(days=30)).strftime("%d%m%Y")
        valor_total = sum([float(cte.valor_receber) for cte in ctes if cte.valor_receber])
        valor_total_fmt = pad(f"{valor_total:.2f}".replace(".", ""), 13, 'right', '0') # ajustar para 15 ao invés de 13
        tipo_cobranca = pad("BCO", 3)
        valor_icms = pad("0", 13, 'right', '0')
        juros = pad("", 13, 'right', '0')
        limite_desc = pad("", 8)
        valor_desc = pad("", 13)
        banco = pad("BANCO COOPERATIVO SICREDI", 35, 'left', ' ')
        agencia = pad("2601", 4)
        dig_ag = pad("0", 1)
        conta = pad("123456", 10)
        dig_cc = pad("0", 2)
        acao = "I"
        filler = pad("", 3)
        return f"352{filial}{tipo_doc_cobranca}{serie_doc_cobranca}{fatura}{data_emissao}{data_vencimento}{valor_total_fmt}{tipo_cobranca}{valor_icms}{juros}{limite_desc}{valor_desc}{banco}{agencia}{dig_ag}{conta}{dig_cc}{acao}{filler}"
    else:
        # Caso não haja CTes, retornar um registro vazio ou com valores padrão
        return f"Não há registro de CTE na tabela cte_info com o ID {user_input.id}"

def build_registro_353(cte):
    return f"353{pad(cte.numero_cte, 10)}{cte.data_emissao[:10].replace('-', '')}{pad(cte.valor_mercadoria, 13)}"

def build_registro_354(cte):
    return f"354{pad(cte.peso_mercadoria, 13)}{pad(cte.valor_prestacao, 13)}"

def build_registro_355(total_valor):
    return f"355{pad(total_valor, 13)}"