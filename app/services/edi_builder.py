from app.utils.edi_utils import pad;
from datetime import datetime, timedelta;

def build_registros(user_input, ctes):
    registros = []

    # Registro 000
    registros.append(build_registro_000(user_input))

    # Registro 350
    registros.append(build_registro_350())

    # Registro 351 e 352
    registros.append(build_registro_351())
    registros.append(build_registro_352(ctes, user_input))

    total_valor = 0
    for cte in ctes:
            registros.append(build_registro_353(cte))
            registros.extend(build_registro_354(cte))

    total_valor = sum(cte.valor_receber or 0 for cte in ctes)
    registros.append(build_registro_355(total_valor, len(ctes)))
    return registros

def build_registro_000(user_input):
    now = datetime.now();
    remetente = pad("BIALOG TRANSPORTE E LOGISTICA S.A.", 35, 'left', ' ')
    destinatario = pad(user_input.nome_cliente, 35, 'left', ' ')
    data = now.strftime("%d%m%y")
    hora = now.strftime("%H%M")
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
    razaoBialog = pad("BIALOG TRANSPORTE E LOGISTICA S.A.", 40, 'left', ' ')
    filler = pad("", 113, 'left', ' ')
    return f"351{cgcBialog}{razaoBialog}{filler}"

def build_registro_352(ctes, user_input):
    if ctes:
        filial = pad('010101', 10, 'left', ' ')
        tipo_doc_cobranca = pad("0", 1)
        serie_doc_cobranca = pad("0", 3)
        fatura = pad(user_input.numero_fatura, 10, 'left', ' ')
        data_emissao = datetime.strptime(ctes[0].data_emissao[:10], "%Y-%m-%d").strftime("%d%m%Y")
        data_vencimento = (datetime.strptime(ctes[0].data_emissao[:10], "%Y-%m-%d") + timedelta(days = user_input.vencimento_fatura)).strftime("%d%m%Y")
        valor_total = sum([float(cte.valor_receber) for cte in ctes if cte.valor_receber])
        valor_total_fmt = pad(f"{valor_total:.2f}".replace(".", ""), 15, 'right', '0') # ajustar para 15 ao invés de 13
        tipo_cobranca = pad("BCO", 3, 'left', ' ')
        valor_icms = pad("", 15, 'right', ' ')
        juros = pad("", 15, 'right', ' ')
        limite_desc = pad("", 8)
        valor_desc = pad("", 15)
        banco = pad("", 35, 'left', ' ')
        agencia = pad("", 4)
        dig_ag = pad("", 1)
        conta = pad("", 10)
        dig_cc = pad("", 2)
        acao = "I"
        filler = pad("", 3, 'left', ' ')
        return f"352{filial}{tipo_doc_cobranca}{serie_doc_cobranca}{fatura}{data_emissao}{data_vencimento}{valor_total_fmt}{tipo_cobranca}{valor_icms}{juros}{limite_desc}{valor_desc}{banco}{agencia}{dig_ag}{conta}{dig_cc}{acao}{filler}"
    else:
        # Caso não haja CTes, retornar um registro vazio ou com valores padrão
        return f"Não há registro de CTE na tabela cte_info com o ID {user_input.id}"

def build_registro_353(cte):
    filial = pad('010101', 10, 'left', ' ')
    serie_cte = pad(cte.serie_cte, 5, 'left', ' ')
    numero_cte = pad(cte.numero_cte, 12, 'right', '0')
    valor_frete = pad(str(cte.valor_receber).replace(".", ""), 15, 'right', '0')
    data_emissao = datetime.strptime(cte.data_emissao[:10], "%Y-%m-%d").strftime("%d%m%Y")
    cgc_remetente = pad(cte.cnpj_cliente, 14)
    cgc_destinatario = pad(cte.cnpj_destinatario, 14)
    cgc_emissor = pad("35285109000105", 14)
    filler = pad("", 75, 'left', ' ')
    return f"353{filial}{serie_cte}{numero_cte}{valor_frete}{data_emissao}{cgc_remetente}{cgc_destinatario}{cgc_emissor}{filler}"

def build_registro_354(cte):
    registros_nf = []
    serie_nfe = pad('1', 3, 'left', ' ')
    data_nfe = pad(datetime.strptime(cte.data_emissao[:10], "%Y-%m-%d").strftime("%d%m%Y"), 8) 
    cgc_emissor = pad(cte.cnpj_cliente, 14)
    filler = pad("", 112, 'left', ' ')

    chaves = cte.chave_nfe.split(',') if cte.chave_nfe else ['']
    for chave in chaves:
        numero_nfe = pad(chave.strip()[28:34], 8, 'right', '0')
        peso = pad(str(round(float(cte.peso_mercadoria or 0), 2)).replace('.', ''), 7, 'right', '0')
        valor_merc = pad(str(round(float(cte.valor_mercadoria or 0), 2)).replace('.', ''), 15, 'right', '0')
        registro_nf = f"354{serie_nfe}{numero_nfe}{data_nfe}{peso}{valor_merc}{cgc_emissor}{filler}"
        registros_nf.append(registro_nf)

    return registros_nf

def build_registro_355(total_valor, qtde_docs):
    qtde_doc = pad(str(qtde_docs), 4, 'right', '0')
    valor_total = pad(f"{float(total_valor):.2f}".replace(".", ""), 15, 'right', '0')
    filler = pad("", 148, 'left', ' ')
    return f"355{qtde_doc}{valor_total}{filler}"
