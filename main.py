from bs4 import BeautifulSoup
from sqlite_tabl import insert_data_to_tablets_table

# открываем XML-файл
with open('aurora_inventory_complete_v2_20230201.xml', 'r') as f:
    xml_text = f.read()

# создаем объект BeautifulSoup для парсинга XML-файла
soup = BeautifulSoup(xml_text, 'lxml')
block = soup.find_all('complete_inventory_v2')


def try_get(str):
    try:
        data = i.find(str).text
        return data
    except:
        data = ''
        return data
data = {}
for i in block:
    packing_id = try_get('packing_id')
    desc_id = try_get('desc_id')
    prep_id = try_get('prep_id')
    trade_name_id = try_get('trade_name_id')
    trade_name_rus = try_get('trade_name_rus')
    trade_name_rus_html = try_get('trade_name_rus_html')
    lat_name_id = try_get('lat_name_id')
    lat_name = try_get('lat_name')
    dosage_form_id = try_get('dosage_form_id')
    dosage_form_full_name = try_get('dosage_form_full_name')
    dosage_form_short_name = try_get('dosage_form_short_name')
    dose = try_get('dose')
    dose_amount = try_get('dose_amount')
    pack1_id = try_get('pack1_id')
    pack1sn = try_get('pack1sn')
    pack1n = try_get('pack1n')
    amount1 = try_get('amount1')
    pack2_id = try_get('pack2_id')
    pack2sn = try_get('pack2sn')
    pack2n = try_get('pack2n')
    amount2 = try_get('amount2')
    pack3_id = try_get('pack3_id')
    amount3 = try_get('amount3')
    packing_short = try_get('packing_short')
    packing_full = try_get('packing_full')
    as_id = try_get('as_id')
    as_name_rus = try_get('as_name_rus')
    producer_id = try_get('producer_id')
    producer_tran = try_get('producer_tran')
    producer_orig = try_get('producer_orig')
    producer_country_id = try_get('producer_country_id')
    producer_country = try_get('producer_country')
    packer_id = try_get('packer_id')
    packer_country_id = try_get('packer_country_id')
    amount = try_get('amount')
    barcode = try_get('barcode')
    dfc_id = try_get('dfc_id')
    completeness_id = try_get('completeness_id')
    reg_id = try_get('reg_id')
    reg_number = try_get('reg_number')
    reg_date = try_get('reg_date')
    rereg_date = try_get('rereg_date')
    reg_cancel_date = try_get('reg_cancel_date')
    reg_status_id = try_get('reg_status_id')
    reg_status = try_get('reg_status')
    registrator_id = try_get('registrator_id')
    registrator_tran = try_get('registrator_tran')
    registrator_orig = try_get('registrator_orig')
    registrator_country_id = try_get('registrator_country_id')
    registrator_country = try_get('registrator_country')
    ntfr_id = try_get('ntfr_id')
    ntfr_name = try_get('ntfr_name')
    lt_id = try_get('lt_id')
    lt_name = try_get('lt_name')
    lt_month = try_get('lt_month')
    sc_id = try_get('sc_id')
    sc_name = try_get('sc_name')
    sc_short_name = try_get('sc_short_name')
    actdate = try_get('actdate')
    weight = try_get('weight')
    prep_short = try_get('prep_short')
    prep_full = try_get('prep_full')
    registration = try_get('registration')
    firms = try_get('firms')

    data['packing_id'] = int(packing_id)
    data['desc_id'] = desc_id
    data['prep_id'] = prep_id
    data['trade_name_id'] = trade_name_id
    data['trade_name_rus'] = trade_name_rus
    data['trade_name_rus_html'] = trade_name_rus_html
    data['lat_name_id'] = lat_name_id
    data['lat_name'] = lat_name
    data['dosage_form_id'] = dosage_form_id
    data['dosage_form_full_name'] = dosage_form_full_name
    data['dosage_form_short_name'] = dosage_form_short_name
    data['dose'] = dose
    data['dose_amount'] = dose_amount
    data['pack1_id'] = pack1_id
    data['pack1sn'] = pack1sn
    data['pack1n'] = pack1n
    data['amount1'] = amount1
    data['pack2_id'] = pack2_id
    data['pack2sn'] = pack2sn
    data['pack2n'] = pack2n
    data['amount2'] = amount2
    data['pack3_id'] = pack3_id
    data['amount3'] = amount3
    data['packing_short'] = packing_short
    data['packing_full'] = packing_full
    data['as_id'] = as_id
    data['as_name_rus'] = as_name_rus
    data['producer_id'] = producer_id
    data['producer_tran'] = producer_tran
    data['producer_orig'] = producer_orig
    data['producer_country_id'] = producer_country_id
    data['producer_country'] = producer_country
    data['packer_id'] = packer_id
    data['packer_country_id'] = packer_country_id
    data['amount'] = amount
    data['barcode'] = barcode
    data['dfc_id'] = dfc_id
    data['completeness_id'] = completeness_id
    data['reg_id'] = reg_id
    data['reg_number'] = reg_number
    data['reg_date'] = reg_date
    data['rereg_date'] = rereg_date
    data['reg_cancel_date'] = reg_cancel_date
    data['reg_status_id'] = reg_status_id
    data['reg_status'] = reg_status
    data['registrator_id'] = registrator_id
    data['registrator_tran'] = registrator_tran
    data['registrator_orig'] = registrator_orig
    data['registrator_country_id'] = registrator_country_id
    data['registrator_country'] = registrator_country
    data['ntfr_id'] = ntfr_id
    data['ntfr_name'] = ntfr_name
    data['lt_id'] = lt_id
    data['lt_name'] = lt_name
    data['lt_month'] = lt_month
    data['sc_id'] = sc_id
    data['sc_name'] = sc_name
    data['sc_short_name'] = sc_short_name
    data['actdate'] = actdate
    data['weight'] = weight
    data['prep_short'] = prep_short
    data['prep_full'] = prep_full
    data['registration'] = registration
    data['firms'] = firms

    insert_data_to_tablets_table(data)