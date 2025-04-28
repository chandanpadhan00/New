for row in rows2:
    qc_rule_no, qc_rule, count, *_ = row
    
    # Insert into qc_rule_counts_history
    insert_query = f"""
        INSERT INTO asnfdm.qc_rule_counts_history
        (batch_id, vendor_name, qc_rule_no, qc_rule, count)
        VALUES
        ('{batch_id}', '{source_name}', '{qc_rule_no}', '{qc_rule}', {count})
    """
    execute_query(insert_query)
    
    # Insert into weekly_exception_count
    current_week = datetime.now().strftime("%B %d, %Y")
    insert_weekly_query = f"""
        INSERT INTO weekly_exception_count (week, source, qc_rule_no, count)
        VALUES ('{current_week}', '{source_name}', '{qc_rule_no}', {count})
    """
    execute_query(insert_weekly_query)