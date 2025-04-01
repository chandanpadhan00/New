query = f"""
SELECT
    lkp.qc_rule_no,
    lkp.qc_rule,
    COALESCE(curr.count, 0) AS count,
    COALESCE(prev.count, 0) AS last_load_count,
    COALESCE(prev.count, 0) - COALESCE(curr.count, 0) AS difference
FROM {qc_lkp_table} lkp
LEFT JOIN (
    SELECT qc_rule_no, COUNT(*) AS count
    FROM {report_table}
    GROUP BY qc_rule_no
) curr
    ON lkp.qc_rule_no = curr.qc_rule_no
LEFT JOIN (
    SELECT q.qc_rule_no, q.count
    FROM asnfdm.qc_rule_counts_history q
    JOIN (
        SELECT qc_rule_no, MAX(process_time) AS last_time
        FROM asnfdm.qc_rule_counts_history
        WHERE batch_id != '{batch_id}'
          AND vendor_name = '{source_name}'
        GROUP BY qc_rule_no
    ) recent
    ON q.qc_rule_no = recent.qc_rule_no AND q.process_time = recent.last_time
    WHERE q.vendor_name = '{source_name}'
) prev
    ON lkp.qc_rule_no = prev.qc_rule_no
WHERE lkp.vendor = '{source_name}'
ORDER BY lkp.s_no
"""
cursor.execute(query)
rows2 = cursor.fetchall()
headers2 = [col[0] for col in cursor.description]
