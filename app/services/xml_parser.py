from lxml import etree;

def parse_cte_xml(xml_file):
    tree = etree.parse(xml_file);
    root = tree.getroot();

    ns = {'ns': root.nsmap[None]} if None in root.nsmap else {};

    def find_xpath(xpath, root, ns):
        result = root.find(xpath, namespaces=ns);
        return result.text if result is not None else None;

    dados = {
        'data_emissao': find_xpath('.//ns:dhEmi', root, ns),
        'numero_cte': find_xpath('.//ns:nCT', root, ns),
        'serie_cte': find_xpath('.//ns:serie', root, ns),
        'cnpj_cliente': find_xpath('.//ns:rem/ns:CNPJ', root, ns),
        'valor_receber': find_xpath('.//ns:vPrest/ns:vRec', root, ns),
        'valor_prestacao': find_xpath('.//ns:vPrest/ns:vTPrest', root, ns),
        'valor_mercadoria': find_xpath('.//ns:infCarga/ns:vCarga', root, ns),
        'peso_mercadoria': find_xpath('.//ns:infQ/ns:qCarga', root, ns),
        'chave_nfe': find_xpath('.//ns:infNFe/ns:chave', root, ns),
        'cnpj_destinatario': find_xpath('.//ns:dest/ns:CNPJ', root, ns),
        'nome_destinatario': find_xpath('.//ns:dest/ns:xNome', root, ns),
    }
    dados['peso_mercadoria'] = round(float(dados['peso_mercadoria']), 2) if dados['peso_mercadoria'] else None
    dados['valor_receber'] = round(float(dados['valor_receber']), 2) if dados['valor_receber'] else None
    dados['valor_prestacao'] = round(float(dados['valor_prestacao']), 2) if dados['valor_prestacao'] else None
    dados['valor_mercadoria'] = round(float(dados['valor_mercadoria']), 2) if dados['valor_mercadoria'] else None

    return dados;
