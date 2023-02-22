import sqlite3

# Создание базы данных и таблицы Tablets
conn = sqlite3.connect('farma.bd')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Tablets
             (packing_id INTEGER PRIMARY KEY,
              desc_id TEXT,
              prep_id TEXT,
              trade_name_id TEXT,
              trade_name_rus TEXT,
              trade_name_rus_html TEXT,
              lat_name_id TEXT,
              lat_name TEXT,
              dosage_form_id TEXT,
              dosage_form_full_name TEXT,
              dosage_form_short_name TEXT,
              dose TEXT,
              dose_amount TEXT,
              pack1_id TEXT,
              pack1sn TEXT,
              pack1n TEXT,
              amount1 TEXT,
              pack2_id TEXT,
              pack2sn TEXT,
              pack2n TEXT,
              amount2 TEXT,
              pack3_id TEXT,
              amount3 TEXT,
              packing_short TEXT,
              packing_full TEXT,
              as_id TEXT,
              as_name_rus TEXT,
              producer_id TEXT,
              producer_tran TEXT,
              producer_orig TEXT,
              producer_country_id TEXT,
              producer_country TEXT,
              packer_id TEXT,
              packer_country_id TEXT,
              amount TEXT,
              barcode TEXT,
              dfc_id TEXT,
              completeness_id TEXT,
              reg_id TEXT,
              reg_number TEXT,
              reg_date TEXT,
              rereg_date TEXT,
              reg_cancel_date TEXT,
              reg_status_id TEXT,
              reg_status TEXT,
              registrator_id TEXT,
              registrator_tran TEXT,
              registrator_orig TEXT,
              registrator_country_id TEXT,
              registrator_country TEXT,
              ntfr_id TEXT,
              ntfr_name TEXT,
              lt_id TEXT,
              lt_name TEXT,
              lt_month TEXT,
              sc_id TEXT,
              sc_name TEXT,
              sc_short_name TEXT,
              actdate TEXT,
              weight TEXT,
              prep_short TEXT,
              prep_full TEXT,
              registration TEXT,
              firms TEXT)''')


def insert_data_to_tablets_table(data):
    conn = sqlite3.connect('farma.bd')
    c = conn.cursor()

    # Define SQL query for inserting data
    sql = '''INSERT INTO Tablets (packing_id, desc_id, prep_id, trade_name_id, trade_name_rus, trade_name_rus_html, 
            lat_name_id, lat_name, dosage_form_id, dosage_form_full_name, dosage_form_short_name, dose, dose_amount, 
            pack1_id, pack1sn, pack1n, amount1, pack2_id, pack2sn, pack2n, amount2, pack3_id, amount3, packing_short, 
            packing_full, as_id, as_name_rus, producer_id, producer_tran, producer_orig, producer_country_id, 
            producer_country, packer_id, packer_country_id, amount, barcode, dfc_id, completeness_id, reg_id, 
            reg_number, reg_date, rereg_date, reg_cancel_date, reg_status_id, reg_status, registrator_id, 
            registrator_tran, registrator_orig, registrator_country_id, registrator_country, ntfr_id, ntfr_name, 
            lt_id, lt_name, lt_month, sc_id, sc_name, sc_short_name, actdate, weight, prep_short, prep_full, 
            registration, firms) 
            VALUES (:packing_id, :desc_id, :prep_id, :trade_name_id, :trade_name_rus, :trade_name_rus_html, 
            :lat_name_id, :lat_name, :dosage_form_id, :dosage_form_full_name, :dosage_form_short_name, :dose, :dose_amount, 
            :pack1_id, :pack1sn, :pack1n, :amount1, :pack2_id, :pack2sn, :pack2n, :amount2, :pack3_id, :amount3, 
            :packing_short, :packing_full, :as_id, :as_name_rus, :producer_id, :producer_tran, :producer_orig, 
            :producer_country_id, :producer_country, :packer_id, :packer_country_id, :amount, :barcode, :dfc_id, 
            :completeness_id, :reg_id, :reg_number, :reg_date, :rereg_date, :reg_cancel_date, :reg_status_id, 
            :reg_status, :registrator_id, :registrator_tran, :registrator_orig, :registrator_country_id, 
            :registrator_country, :ntfr_id, :ntfr_name, :lt_id, :lt_name, :lt_month, :sc_id, :sc_name, :sc_short_name, 
            :actdate, :weight, :prep_short, :prep_full, :registration, :firms)'''

    # Execute the query with the given data
    c.execute(sql, data)
    conn.commit()
    conn.close()
