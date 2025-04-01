for row in rows2:
    qc_rule_no, qc_rule, count = row
    insert_query = f"""
        INSERT INTO asnfdm.qc_rule_counts_history
        (batch_id, vendor_name, qc_rule_no, qc_rule, count)
        VALUES
        ('{batch_id}', '{source_name}', '{qc_rule_no}', '{qc_rule}', {count})
    """
    execute_query(insert_query)



 #2. Insert Rule Counts Automatically During Each Run
#📍Place this block in load_report_to_s3(), just after rows2 is created (i.e., after fetching QC rule counts):
