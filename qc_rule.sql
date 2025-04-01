query = f"""
WITH last_batch AS (
    SELECT MAX(batch_id) AS last_batch_id
    FROM asnfdm.qc_rule_counts_history
    WHERE batch_id < '{batch_id}'
      AND vendor_name = '{source_name}'
),
prev_counts AS (
    SELECT qc_rule_no, count
    FROM asnfdm.qc_rule_counts_history
    WHERE vendor_name = '{source_name}'
      AND batch_id = (SELECT last_batch_id FROM last_batch)
)
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
LEFT JOIN prev_counts prev
    ON lkp.qc_rule_no = prev.qc_rule_no
WHERE lkp.vendor = '{source_name}'
ORDER BY lkp.s_no
"""
cursor.execute(query)
rows2 = cursor.fetchall()
headers2 = [col[0] for col in cursor.description]
